#!/usr/bin/env python3
"""
================================================================================
LESSON 26 / GITHUB REPOSITORY CRAWLER: FSSPEC OPEN & CACHE_TYPE EXTRACTOR
================================================================================

This module implements a specialized Python AST (Abstract Syntax Tree) crawler
and analyzer designed to crawl remote GitHub repositories via GitHub Trees API,
detect usages of `fsspec.open` and related file API calls, analyze `cache_type`
and `cache_options` parameters, and capture exact line-level GitHub URLs (`file_url`).

--------------------------------------------------------------------------------
FSSPEC CACHE_TYPE OPTIONS EXPLAINED:
--------------------------------------------------------------------------------
1. `cache_type="readahead"` (DEFAULT for sequential reads):
   - Prefetches data in chunks ahead of the reader cursor.
2. `cache_type="none"`:
   - Disables caching completely. Direct HTTP Range GET requests.
3. `cache_type="bytes"`:
   - Caches exact byte ranges in memory dictionary.
4. `cache_type="mmap"`:
   - Spools byte ranges to a temporary local file and memory-maps it (`mmap`).
5. `cache_type="block"` / `cache_type="blockcache"`:
   - Fixed-size block memory cache.
6. `cache_type="parts"`:
   - Parquet section/column block caching (required for `fsspec.parquet` precaching).
7. `cache_type="background"`:
   - Asynchronously prefetches data blocks in background threads.

--------------------------------------------------------------------------------
USAGE EXAMPLES:
--------------------------------------------------------------------------------
1. Crawl a single GitHub repository:
   python projects/26_fsspec_github_crawler.py --repo dask/dask --output-csv report.csv --output-json report.json --output-md report.md

2. Crawl all 12 major Python data science & AI frameworks:
   python projects/26_fsspec_github_crawler.py --all --output-csv report.csv --output-json report.json --output-md report.md
"""

import argparse
import ast
import csv
import json
import re
import sys
import time
import urllib.request
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

# ================================================================================
# DATA STRUCTURES & DEFAULT CONFIGURATION
# ================================================================================

SPECIFIED_CACHE_KEYWORDS = {
    "mmap",
    "readahead",
    "first",
    "blockcache",
    "block",
    "bytes",
    "all",
    "parts",
    "background",
}

DEFAULT_TARGET_REPOS = [
    ("Dask", "dask/dask"),
    ("Intake", "intake/intake"),
    ("pandas", "pandas-dev/pandas"),
    ("xarray", "pydata/xarray"),
    ("zarr", "zarr-developers/zarr-python"),
    ("DVC", "iterative/dvc"),
    ("Kedro", "kedro-org/kedro"),
    ("Hugging Face Datasets", "huggingface/datasets"),
    ("PyTorch", "pytorch/pytorch"),
    ("PyTorch Lightning", "Lightning-AI/pytorch-lightning"),
    ("TorchTitan", "pytorch/torchtitan"),
    ("Ray", "ray-project/ray"),
]


@dataclass
class FsspecUsage:
    """Represents a single detected usage of fsspec.open or related file handle call."""
    file_path: str
    line_number: int
    end_line_number: int
    target_name: str
    enclosing_function: Optional[str] = None
    enclosing_class: Optional[str] = None
    cache_type: str = "NOT_EXPLICIT"  # Extracted cache_type value or default
    is_specified_cache_keyword: bool = False  # True if cache_type in SPECIFIED_CACHE_KEYWORDS
    cache_options: Optional[str] = None  # Extracted cache_options dict string
    repo_url: Optional[str] = None  # Full repository web link
    file_url: Optional[str] = None  # Full line URL
    args: List[str] = field(default_factory=list)
    kwargs: Dict[str, str] = field(default_factory=dict)
    code_snippet: str = ""
    detection_method: str = "ast"  # "ast" or "regex"

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)


@dataclass
class CrawlReport:
    """Summary report of the crawling session."""
    target_source: str
    total_files_scanned: int
    files_with_usages: int
    total_usages_found: int
    repo_url: Optional[str] = None
    cache_type_summary: Dict[str, int] = field(default_factory=dict)
    usages: List[FsspecUsage] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        data = asdict(self)
        data["usages"] = [u.to_dict() for u in self.usages]
        return data


# ================================================================================
# AST VISITOR & PARSER ENGINE
# ================================================================================

class FsspecASTVisitor(ast.NodeVisitor):
    """AST NodeVisitor that inspects Python source trees for fsspec usages."""

    TARGET_FUNCTION_NAMES = {
        "open",
        "open_files",
        "open_local",
        "url_to_fs",
        "filesystem",
        "get_fs_token_paths",
        "open_parquet_file",
    }

    TARGET_OBJECT_METHODS = {
        "open",
        "cat",
        "get",
        "put",
        "read_block",
        "info",
        "ls",
        "exists",
        "isdir",
        "isfile",
        "ukey",
        "relparts",
        "join",
        "parts",
        "getcwd",
        "chdir",
        "isin",
        "normpath",
    }

    def __init__(
        self,
        file_path: str,
        source_code: str,
        repo_url: Optional[str] = None,
        branch: str = "main",
    ):
        self.file_path = file_path
        self.source_lines = source_code.splitlines()
        self.repo_url = repo_url
        self.branch = branch
        self.usages: List[FsspecUsage] = []

        self.current_class: Optional[str] = None
        self.current_function: Optional[str] = None
        self.local_cache_type: Optional[str] = None
        self.imports: Dict[str, str] = {}
        self.filesystem_vars: set = {"fs", "self.fs", "gcs_fs", "s3_fs"}

    def _get_node_source(self, node: ast.AST) -> str:
        """Extract literal source snippet for an AST node."""
        try:
            return ast.unparse(node)
        except Exception:
            return ""

    def _get_snippet(self, start_line: int, end_line: int) -> str:
        """Extract code snippet across specified line range (1-indexed)."""
        s_idx = max(0, start_line - 1)
        e_idx = min(len(self.source_lines), end_line)
        return "\n".join(self.source_lines[s_idx:e_idx])

    def _clean_str_literal(self, val_str: str) -> str:
        """Strip surrounding quotes from a string representation."""
        val_str = val_str.strip()
        if (val_str.startswith('"') and val_str.endswith('"')) or (
            val_str.startswith("'") and val_str.endswith("'")
        ):
            return val_str[1:-1]
        return val_str

    def _build_file_url(self, start_line: int) -> Optional[str]:
        """Construct full line-level web link for GitHub."""
        if self.repo_url:
            clean_repo = self.repo_url.rstrip("/")
            return f"{clean_repo}/blob/{self.branch}/{self.file_path}#L{start_line}"
        abs_p = Path(self.file_path).resolve()
        return f"file://{abs_p}#L{start_line}"

    def visit_ClassDef(self, node: ast.ClassDef):
        """Track class context."""
        old_class = self.current_class
        self.current_class = node.name
        self.generic_visit(node)
        self.current_class = old_class

    def visit_FunctionDef(self, node: ast.FunctionDef):
        """Track function context and local kwargs.pop/get('cache_type', default) assignments."""
        old_func = self.current_function
        old_ct = getattr(self, "local_cache_type", None)
        self.current_function = node.name
        self.local_cache_type = None

        # Inspect function body to detect cache_type = kwargs.pop/get("cache_type", default)
        for child in ast.walk(node):
            if isinstance(child, ast.Assign) and isinstance(child.value, ast.Call):
                func_val = child.value.func
                if isinstance(func_val, ast.Attribute) and func_val.attr in ("pop", "get") and child.value.args:
                    arg0 = child.value.args[0]
                    if isinstance(arg0, ast.Constant) and arg0.value == "cache_type":
                        if len(child.value.args) >= 2 and isinstance(child.value.args[1], ast.Constant):
                            self.local_cache_type = str(child.value.args[1].value)

        self.generic_visit(node)
        self.current_function = old_func
        self.local_cache_type = old_ct

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        """Track async function context."""
        self.visit_FunctionDef(node)

    def visit_Import(self, node: ast.Import):
        """Track module imports like `import fsspec` or `import fsspec.parquet as fsspec_parquet`."""
        for alias in node.names:
            local_name = alias.asname or alias.name
            self.imports[local_name] = alias.name
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        """Track from imports like `from fsspec import open`."""
        module = node.module or ""
        for alias in node.names:
            local_name = alias.asname or alias.name
            full_name = f"{module}.{alias.name}" if module else alias.name
            self.imports[local_name] = full_name
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign):
        """Track filesystem assignments, e.g. `fs = fsspec.filesystem('gcs')`."""
        if isinstance(node.value, ast.Call):
            func = node.value.func
            if isinstance(func, ast.Attribute) and func.attr == "filesystem":
                for target in node.targets:
                    var_name = self._get_node_source(target)
                    if var_name:
                        self.filesystem_vars.add(var_name)
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        """Analyze call sites for fsspec usages."""
        is_match = False
        target_name = ""

        # Case 1: Direct function calls (e.g. `fsspec.open(...)`, `open_files(...)`)
        if isinstance(node.func, ast.Name):
            func_id = node.func.id
            imported_orig = self.imports.get(func_id, "")
            if imported_orig.startswith("fsspec") or func_id in self.TARGET_FUNCTION_NAMES:
                is_match = True
                target_name = func_id

        # Case 2: Attribute calls (e.g. `fsspec.open(...)`, `fs.open(...)`, `self.fs.open(...)`)
        elif isinstance(node.func, ast.Attribute):
            attr = node.func.attr
            val_id = self._get_node_source(node.func.value)
            imported_orig = self.imports.get(val_id, val_id)

            if imported_orig == "fsspec" or imported_orig.startswith("fsspec.") or imported_orig == "gcsfs":
                is_match = True
                target_name = f"{val_id}.{attr}"
            elif (val_id in self.filesystem_vars or val_id.endswith(".fs") or "fs" in val_id) and attr in self.TARGET_OBJECT_METHODS:
                is_match = True
                target_name = f"{val_id}.{attr}"

        if is_match:
            start_line = node.lineno
            end_line = getattr(node, "end_lineno", start_line)
            args_repr = [self._get_node_source(arg) for arg in node.args]
            kwargs_repr = {
                kw.arg: self._get_node_source(kw.value)
                for kw in node.keywords
                if kw.arg is not None
            }

            # Extract cache_type and cache_options explicitly
            raw_cache_type = kwargs_repr.get("cache_type") or kwargs_repr.get("simple_cache")
            if raw_cache_type:
                cache_type = self._clean_str_literal(raw_cache_type)
            elif getattr(self, "local_cache_type", None):
                cache_type = getattr(self, "local_cache_type")
            else:
                cache_type = "NOT_EXPLICIT"
            cache_options = kwargs_repr.get("cache_options")

            file_url = self._build_file_url(start_line)
            snippet = self._get_snippet(start_line, end_line)

            self.usages.append(
                FsspecUsage(
                    file_path=self.file_path,
                    line_number=start_line,
                    end_line_number=end_line,
                    target_name=target_name,
                    enclosing_function=self.current_function,
                    enclosing_class=self.current_class,
                    cache_type=cache_type,
                    is_specified_cache_keyword=cache_type.lower() in SPECIFIED_CACHE_KEYWORDS,
                    cache_options=cache_options,
                    repo_url=self.repo_url,
                    file_url=file_url,
                    args=args_repr,
                    kwargs=kwargs_repr,
                    code_snippet=snippet,
                    detection_method="ast",
                )
            )

        self.generic_visit(node)


# ================================================================================
# REGEX FALLBACK SCANNER
# ================================================================================

class RegexFallbackScanner:
    """Fallback scanner using regular expressions for unparseable Python files or strings."""

    REGEX_PATTERNS = [
        re.compile(r"(?:fsspec|gcsfs)\.open(?:_files|_local)?\s*\("),
        re.compile(r"(?:fs|filesystem|gcs_fs)\.open\s*\("),
        re.compile(r"from\s+fsspec\s+import\s+.*open"),
    ]

    CACHE_TYPE_PATTERN = re.compile(r"cache_type\s*=\s*[\"']?([a-zA-Z0-9_-]+)[\"']?")

    @classmethod
    def scan_content(
        cls, file_path: str, content: str, repo_url: Optional[str] = None, branch: str = "main"
    ) -> List[FsspecUsage]:
        """Scan file text line by line using regex patterns."""
        usages = []
        lines = content.splitlines()
        for idx, line in enumerate(lines, start=1):
            for pattern in cls.REGEX_PATTERNS:
                if pattern.search(line):
                    match_ct = cls.CACHE_TYPE_PATTERN.search(line)
                    ct_val = match_ct.group(1) if match_ct else "NOT_EXPLICIT"
                    file_url = f"{repo_url}/blob/{branch}/{file_path}#L{idx}" if repo_url else f"file://{Path(file_path).resolve()}#L{idx}"
                    usages.append(
                        FsspecUsage(
                            file_path=file_path,
                            line_number=idx,
                            end_line_number=idx,
                            target_name="regex_match",
                            cache_type=ct_val,
                            is_specified_cache_keyword=ct_val.lower() in SPECIFIED_CACHE_KEYWORDS,
                            repo_url=repo_url,
                            file_url=file_url,
                            code_snippet=line.strip(),
                            detection_method="regex",
                        )
                    )
                    break
        return usages


# ================================================================================
# GITHUB CRAWLER ENGINE
# ================================================================================

class FsspecCrawlerEngine:
    """Engine that manages scanning of remote GitHub repositories via GitHub Trees API."""

    def __init__(self, use_regex_fallback: bool = True, include_tests: bool = False):
        self.use_regex_fallback = use_regex_fallback
        self.include_tests = include_tests

    def _build_cache_type_summary(self, usages: List[FsspecUsage]) -> Dict[str, int]:
        """Summarize count of each cache_type found in usages."""
        summary: Dict[str, int] = {}
        for u in usages:
            summary[u.cache_type] = summary.get(u.cache_type, 0) + 1
        return summary

    def scan_code(
        self, file_path: str, source_code: str, repo_url: Optional[str] = None, branch: str = "main"
    ) -> List[FsspecUsage]:
        """Scan a single Python source code string."""
        try:
            tree = ast.parse(source_code, filename=file_path)
            visitor = FsspecASTVisitor(file_path, source_code, repo_url=repo_url, branch=branch)
            visitor.visit(tree)
            return visitor.usages
        except SyntaxError:
            if self.use_regex_fallback:
                return RegexFallbackScanner.scan_content(file_path, source_code, repo_url=repo_url, branch=branch)
            return []
        except Exception:
            return []

    def scan_github_repo(self, repo_name: str, branch: str = "main") -> CrawlReport:
        """
        Crawl a remote GitHub repository via GitHub Trees API and scan all Python files.
        Example repo_name: 'dask/dask' or 'pytorch/pytorch'
        """
        repo_url = f"https://github.com/{repo_name}"
        tree_url = f"https://api.github.com/repos/{repo_name}/git/trees/{branch}?recursive=1"
        req = urllib.request.Request(tree_url, headers={"User-Agent": "Fsspec-Crawler-Python"})
        
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            print(f"Failed to fetch GitHub repository tree for {repo_name}: {e}", file=sys.stderr)
            return CrawlReport(
                target_source=repo_name,
                total_files_scanned=0,
                files_with_usages=0,
                total_usages_found=0,
                repo_url=repo_url,
            )

        tree = data.get("tree", [])
        py_files = [
            f["path"]
            for f in tree
            if f.get("path", "").endswith(".py")
            and (self.include_tests or not Path(f.get("path", "")).name.startswith("test_"))
        ]

        all_usages: List[FsspecUsage] = []
        scanned_count = len(py_files)
        files_with_matches = 0

        from concurrent.futures import ThreadPoolExecutor

        def _fetch_and_scan(rel_path: str):
            raw_url = f"https://raw.githubusercontent.com/{repo_name}/{branch}/{rel_path}"
            try:
                raw_req = urllib.request.Request(raw_url, headers={"User-Agent": "Fsspec-Crawler-Python"})
                with urllib.request.urlopen(raw_req, timeout=10) as raw_resp:
                    content = raw_resp.read().decode("utf-8", errors="ignore")
                return self.scan_code(rel_path, content, repo_url=repo_url, branch=branch)
            except Exception:
                return []

        with ThreadPoolExecutor(max_workers=20) as executor:
            file_usages = executor.map(_fetch_and_scan, py_files)

        for usages in file_usages:
            if usages:
                files_with_matches += 1
                all_usages.extend(usages)

        summary = self._build_cache_type_summary(all_usages)

        return CrawlReport(
            target_source=f"GitHub:{repo_name} ({branch})",
            total_files_scanned=scanned_count,
            files_with_usages=files_with_matches,
            total_usages_found=len(all_usages),
            repo_url=repo_url,
            cache_type_summary=summary,
            usages=all_usages,
        )


# ================================================================================
# EXPORT FORMATTERS (CSV & MARKDOWN)
# ================================================================================

def export_csv_report(reports: Any, output_path: str):
    """Export crawl report(s) to CSV format."""
    if not isinstance(reports, list):
        reports = [reports]
    rows = []
    for r in reports:
        repo_name = r.target_source.replace("GitHub:", "").split()[0]
        for u in r.usages:
            is_spec = u.cache_type.lower() in SPECIFIED_CACHE_KEYWORDS
            rows.append([
                repo_name,
                u.file_path,
                u.line_number,
                u.target_name,
                u.cache_type,
                is_spec,
                u.cache_options or "None",
                u.enclosing_class or "None",
                u.enclosing_function or "global",
                u.file_url,
                u.code_snippet.replace("\n", " ")
            ])

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "repository", "file_path", "line_number", "target_name",
            "cache_type", "is_specified_cache_keyword", "cache_options",
            "enclosing_class", "enclosing_function", "file_url", "code_snippet"
        ])
        writer.writerows(rows)
    print(f"CSV report exported to: {output_path} ({len(rows)} rows)")


def export_markdown_report(reports: Any, output_path: str, include_tests: bool = False):
    """Generate a clean Markdown summary report across one or multiple crawl reports."""
    if not isinstance(reports, list):
        reports = [reports]
    total_files = sum(r.total_files_scanned for r in reports)
    total_matches = sum(r.files_with_usages for r in reports)
    total_usages = sum(r.total_usages_found for r in reports)
    
    global_cache_summary: Dict[str, int] = {}
    for r in reports:
        for ct, cnt in r.cache_type_summary.items():
            global_cache_summary[ct] = global_cache_summary.get(ct, 0) + cnt

    md_lines = [
        f"# Master FSSPEC Usage Report Across GitHub Repositories",
        f"",
        f"- **Repositories Crawled:** `{len(reports)}`",
        f"- **Total Files Scanned:** `{total_files}`",
        f"- **Files with FSSPEC Usages:** `{total_matches}`",
        f"- **Total FSSPEC Usages Detected:** `{total_usages}`",
        f"- **Skipping Test Files (test_*.py):** `{not include_tests}`",
        f"",
        f"---",
        f"",
        f"## 📊 Repository Summary Table",
        f"",
        f"| Project / Repository | Files Scanned | Files w/ Usages | Total Usages | Cache_Types |",
        f"| :--- | :--- | :--- | :--- | :--- |"
    ]

    for r in reports:
        repo_name = r.target_source.replace("GitHub:", "").split()[0]
        ct_str = ", ".join([f"{k}:{v}" for k, v in r.cache_type_summary.items()]) if r.cache_type_summary else "None"
        md_lines.append(f"| [{repo_name}](https://github.com/{repo_name}) | `{r.total_files_scanned}` | `{r.files_with_usages}` | `{r.total_usages_found}` | `{ct_str}` |")

    md_lines.extend([
        f"",
        f"---",
        f"",
        f"## 📈 Global Cache_Type Breakdown",
        f"",
        f"| Cache_Type Option | Total Occurrences | Is Specified Keyword | Description |",
        f"| :--- | :--- | :--- | :--- |"
    ])

    descriptions = {
        "readahead": "Default prefetching chunks for sequential reads",
        "mmap": "Memory-mapped temporary file for random access (Parquet/ORC)",
        "block": "Fixed-size block memory cache",
        "parts": "Parquet section/column block caching (required for fsspec.parquet precaching)",
        "none": "No cache, direct HTTP Range GET requests",
        "bytes": "Dictionary of exact byte ranges in RAM",
        "background": "Async background block prefetching",
        "file": "Downloads complete file to local disk first",
        "NOT_EXPLICIT": "cache_type keyword omitted (uses fsspec default)"
    }

    for ct, cnt in global_cache_summary.items():
        desc = descriptions.get(ct, "Custom cache strategy")
        is_spec = ct.lower() in SPECIFIED_CACHE_KEYWORDS
        md_lines.append(f"| `{ct}` | `{cnt}` | `{is_spec}` | {desc} |")

    md_lines.extend([
        f"",
        f"---",
        f"",
        f"## 🔍 Detailed Usage Breakdown by Repository",
        f""
    ])

    for r in reports:
        repo_name = r.target_source.replace("GitHub:", "").split()[0]
        md_lines.extend([
            f"### [{repo_name}](https://github.com/{repo_name})",
            f"- **Usages Found:** `{r.total_usages_found}` in `{r.files_with_usages}` files.",
            f""
        ])
        if not r.usages:
            md_lines.append("No direct `fsspec` usages detected in this repository.\n")
        else:
            for idx, usage in enumerate(r.usages, start=1):
                func_info = f"`{usage.enclosing_class}.{usage.enclosing_function}`" if usage.enclosing_class else f"`{usage.enclosing_function or 'global'}`"
                file_link_str = f"[{usage.file_path}]({usage.file_url})" if usage.file_url else f"`{usage.file_path}`"
                md_lines.extend([
                    f"#### {idx}. {file_link_str} (Line {usage.line_number})",
                    f"- **Line Link:** {usage.file_url}",
                    f"- **Target Call:** `{usage.target_name}` | **Cache_Type:** `{usage.cache_type}` | **Is Specified Keyword:** `{usage.is_specified_cache_keyword}`",
                    f"- **Context:** {func_info}",
                    f"- **Arguments:** `{', '.join(usage.args)}`",
                    f"- **Keywords:** `{usage.kwargs}`",
                    f"",
                    f"```python",
                    f"{usage.code_snippet}",
                    f"```",
                    f"",
                ])

    Path(output_path).write_text("\n".join(md_lines), encoding="utf-8")
    print(f"Markdown report exported to: {output_path}")


# ================================================================================
# CLI ENTRY POINT
# ================================================================================

def main():
    parser = argparse.ArgumentParser(description="Crawl remote GitHub repositories to extract fsspec open usages, cache_type options, and GitHub file URLs.")
    parser.add_argument("--repo", "-r", nargs="+", help="One or more GitHub repositories (e.g. --repo dask/dask pytorch/pytorch)")
    parser.add_argument("--all", "-a", action="store_true", help="Crawl all 12 default open-source repositories")
    parser.add_argument("--branch", "-b", default="main", help="GitHub branch (default: main)")
    parser.add_argument("--include-tests", action="store_true", help="Include test python files (test_*.py)")
    parser.add_argument("--output-csv", "-c", help="Path to write output CSV report")
    parser.add_argument("--output-json", "-o", help="Path to write output JSON report")
    parser.add_argument("--output-md", "-m", help="Path to write output Markdown report")

    args = parser.parse_args()

    target_repos = []
    if args.all:
        target_repos = [repo for _, repo in DEFAULT_TARGET_REPOS]
    elif args.repo:
        target_repos = args.repo
    else:
        parser.error("Please specify --repo <owner/repo...> or --all")

    engine = FsspecCrawlerEngine(include_tests=args.include_tests)
    reports: List[CrawlReport] = []

    start_time = time.time()
    for repo in target_repos:
        print(f"\n[+] Crawling GitHub repo: {repo}...")
        report = engine.scan_github_repo(repo, branch=args.branch)
        if report.total_files_scanned == 0 and args.branch == "main":
            report = engine.scan_github_repo(repo, branch="master")

        print(f"    - Scanned {report.total_files_scanned} files | Found {report.total_usages_found} usages in {report.files_with_usages} files.")
        print(f"    - Cache_Type Summary: {report.cache_type_summary}")
        reports.append(report)

    elapsed = time.time() - start_time
    print(f"\nCompleted crawling {len(reports)} repositories in {elapsed:.2f} seconds.")

    # Export CSV report
    if args.output_csv:
        export_csv_report(reports, args.output_csv)

    # Export JSON report
    if args.output_json:
        json_data = {
            "summary": {
                "total_repositories": len(reports),
                "total_files_scanned": sum(r.total_files_scanned for r in reports),
                "files_with_usages": sum(r.files_with_usages for r in reports),
                "total_usages_found": sum(r.total_usages_found for r in reports),
                "elapsed_seconds": round(elapsed, 2)
            },
            "per_repository": [r.to_dict() for r in reports]
        }
        Path(args.output_json).write_text(json.dumps(json_data, indent=2), encoding="utf-8")
        print(f"JSON report saved to: {args.output_json}")

    # Export Markdown report
    if args.output_md:
        export_markdown_report(reports, args.output_md, include_tests=args.include_tests)


if __name__ == "__main__":
    main()
