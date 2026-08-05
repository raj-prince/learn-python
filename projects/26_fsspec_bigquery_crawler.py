#!/usr/bin/env python3
"""
================================================================================
LESSON 26 / CRAWLER: FSSPEC OPEN & CACHE_TYPE EXTRACTOR FOR BIGQUERY LIBRARIES
================================================================================

This module implements a Python AST (Abstract Syntax Tree) crawler and analyzer
specifically designed to detect and extract usages of `fsspec.open` and analyze
the `cache_type` and `cache_options` parameters, while capturing exact repository
and line-level URLs (`repo_url`, `file_url`).

--------------------------------------------------------------------------------
FSSPEC CACHE_TYPE OPTIONS EXPLAINED:
--------------------------------------------------------------------------------
When reading files from Google Cloud Storage (`gs://`) or other remote filesystems
via `fsspec.open(url, mode='rb', cache_type=...)`, `fsspec` supports several caching
strategies to optimize performance and network usage:

1. `cache_type="readahead"` (DEFAULT for sequential reads):
   - Prefetches data in chunks ahead of the reader cursor.
   - Ideal for sequential streaming (CSV, JSON, log processing).

2. `cache_type="none"` (or `None`):
   - Disables caching completely. Every `read()` call triggers a direct HTTP Range GET request.
   - Best for single large contiguous reads or memory-constrained environments.

3. `cache_type="bytes"`:
   - Caches exact byte ranges in memory in a dictionary.
   - Best for small random reads where byte ranges repeat or overlap.

4. `cache_type="mmap"`:
   - Spools fetched byte ranges to a temporary local disk file and memory-maps it (`mmap`).
   - Highly efficient for large binary columnar files (Parquet, ORC, HDF5) with random seeking.

5. `cache_type="block"`:
   - Divides files into fixed-size blocks (e.g. 5MB) and caches active blocks in memory up to `max_blocks`.
   - Configured via `cache_options={"block_size": 5 * 1024 * 1024}`.

6. `cache_type="background"`:
   - Asynchronously prefetches data blocks in background threads so CPU computations aren't blocked.

7. `cache_type="file"` / `cache_type="local"`:
   - Downloads the full file to local disk before opening.
   - Ideal for C/C++ native bindings (DuckDB, SQLite, OpenCV) that require a local file path.

8. `cache_type="simplecache"`:
   - Caches whole files locally on disk, refreshing only if modified date or ETag changes.

--------------------------------------------------------------------------------
USAGE EXAMPLES:
--------------------------------------------------------------------------------
1. Scan a local directory:
   python 26_fsspec_bigquery_crawler.py --dir /path/to/repo --output-json report.json

2. Scan a GitHub repository:
   python 26_fsspec_bigquery_crawler.py --repo googleapis/python-bigquery --output-md report.md

3. Run built-in demo mode:
   python 26_fsspec_bigquery_crawler.py --demo
"""

import argparse
import ast
import json
import os
import re
import subprocess
import sys
import urllib.request
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple


# ================================================================================
# DATA STRUCTURES FOR CRAWLER RESULTS
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
        """Convert to dictionary representation."""
        return {
            "target_source": self.target_source,
            "total_files_scanned": self.total_files_scanned,
            "files_with_usages": self.files_with_usages,
            "total_usages_found": self.total_usages_found,
            "repo_url": self.repo_url,
            "cache_type_summary": self.cache_type_summary,
            "usages": [u.to_dict() for u in self.usages]
        }


# ================================================================================
# GIT REMOTE URL HELPER
# ================================================================================

def detect_git_repo_info(dir_path: str) -> Tuple[Optional[str], str]:
    """
    Detect git remote URL and active branch for a local directory.
    Returns (repo_url, branch_name).
    """
    repo_url = None
    branch = "main"

    try:
        # Get remote origin URL
        res_remote = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            cwd=dir_path,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if res_remote.returncode == 0 and res_remote.stdout.strip():
            raw_url = res_remote.stdout.strip()
            if raw_url.endswith(".git"):
                raw_url = raw_url[:-4]
            if raw_url.startswith("git@github.com:"):
                raw_url = "https://github.com/" + raw_url[len("git@github.com:"):]
            repo_url = raw_url

        # Get current branch or commit
        res_branch = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=dir_path,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if res_branch.returncode == 0 and res_branch.stdout.strip():
            b = res_branch.stdout.strip()
            if b != "HEAD":
                branch = b
            else:
                res_hash = subprocess.run(
                    ["git", "rev-parse", "--short", "HEAD"],
                    cwd=dir_path,
                    capture_output=True,
                    text=True,
                    timeout=2,
                )
                if res_hash.returncode == 0:
                    branch = res_hash.stdout.strip()
    except Exception:
        pass

    return repo_url, branch


# ================================================================================
# AST VISITOR FOR FSSPEC USAGE DETECTION
# ================================================================================

class FsspecASTVisitor(ast.NodeVisitor):
    """
    AST Visitor that traverses a Python AST tree to find fsspec open calls.
    Tracks imports, aliasing, variable assignments, enclosing contexts, cache_type options, and URLs.
    """

    def __init__(self, file_path: str, source_code: str, repo_url: Optional[str] = None, branch: str = "main"):
        self.file_path = file_path
        self.source_code = source_code
        self.repo_url = repo_url
        self.branch = branch
        self.lines = source_code.splitlines()
        self.usages: List[FsspecUsage] = []
        self.imports: Dict[str, str] = {}  # local_alias -> original_module/func
        self.fs_variables: Set[str] = set()  # variables holding fsspec.filesystem instances
        self.current_function: Optional[str] = None
        self.current_class: Optional[str] = None

    def _get_node_source(self, node: ast.AST) -> str:
        """Safely unparse an AST node back into Python source string representation."""
        try:
            return ast.unparse(node)
        except Exception:
            return ""

    def _get_snippet(self, start_line: int, end_line: int, radius: int = 1) -> str:
        """Extract lines of code around line numbers for visual context."""
        start_idx = max(0, start_line - 1 - radius)
        end_idx = min(len(self.lines), end_line + radius)
        snippet_lines = self.lines[start_idx:end_idx]
        return "\n".join(snippet_lines)

    def _clean_str_literal(self, value_str: str) -> str:
        """Strip surrounding quotes from Python string representation."""
        val = value_str.strip()
        if (val.startswith("'") and val.endswith("'")) or (val.startswith('"') and val.endswith('"')):
            return val[1:-1]
        return val

    def _build_file_url(self, start_line: int) -> str:
        """Construct web or file link for the line."""
        if self.repo_url:
            return f"{self.repo_url}/blob/{self.branch}/{self.file_path}#L{start_line}"
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
        """Track module imports like `import fsspec` or `import fsspec as fs_pkg`."""
        for alias in node.names:
            local_name = alias.asname or alias.name
            self.imports[local_name] = alias.name
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        """Track from imports like `from fsspec import open` or `from fsspec.core import url_to_fs`."""
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
            if isinstance(func, ast.Attribute) and func.attr in ("filesystem", "GCSFileSystem"):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        self.fs_variables.add(target.id)
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        """Inspect all call expressions to identify fsspec open calls and cache_type settings."""
        is_match = False
        target_name = ""

        # Case 1: Attribute call like `fsspec.filesystem(...)`, `fsspec.open(...)`, `fs.open(...)`, `self.fs.open(...)`
        if isinstance(node.func, ast.Attribute):
            attr = node.func.attr
            val = node.func.value

            # Subcase A: Value is Name (e.g., `fsspec.filesystem`, `fsspec.open`, `fs.open`)
            if isinstance(val, ast.Name):
                val_id = val.id
                imported_orig = self.imports.get(val_id, val_id)
                if imported_orig == "fsspec" or imported_orig.startswith("fsspec.") or imported_orig == "gcsfs":
                    is_match = True
                    target_name = f"{val_id}.{attr}"
                elif (
                    val_id in self.fs_variables or val_id in ("fs", "filesystem", "fsspec_fs", "gcs_fs", "gcs")
                ):
                    is_match = True
                    target_name = f"{val_id}.{attr}"

            # Subcase B: Value is Attribute (e.g., `self.fs.open(...)`)
            elif isinstance(val, ast.Attribute):
                if val.attr in ("fs", "filesystem", "fsspec_fs", "gcs_fs", "gcs"):
                    is_match = True
                    target_name = f"self.{val.attr}.{attr}"

        # Case 2: Direct function call imported from fsspec (e.g. `url_to_fs(...)`, `open(...)`)
        elif isinstance(node.func, ast.Name):
            fn_id = node.func.id
            imported_orig = self.imports.get(fn_id, fn_id)
            if imported_orig.startswith("fsspec.") or imported_orig == "fsspec":
                is_match = True
                target_name = fn_id

        if is_match:
            start_line = getattr(node, "lineno", 1)
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
# CRAWLER ENGINE
# ================================================================================

class FsspecCrawlerEngine:
    """Engine that manages scanning of files, directories, or GitHub repositories."""

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

    def scan_file(
        self, file_path: str, repo_url: Optional[str] = None, branch: str = "main"
    ) -> List[FsspecUsage]:
        """Scan a single local file."""
        try:
            content = Path(file_path).read_text(encoding="utf-8", errors="ignore")
            return self.scan_code(file_path, content, repo_url=repo_url, branch=branch)
        except Exception as e:
            print(f"Error reading file {file_path}: {e}", file=sys.stderr)
            return []

    def scan_directory(self, dir_path: str) -> CrawlReport:
        """Recursively scan a local directory for Python files and detect git repository URL."""
        root_path = Path(dir_path).resolve()
        repo_url, branch = detect_git_repo_info(str(root_path))

        all_usages: List[FsspecUsage] = []
        scanned_count = 0
        files_with_matches = 0

        for path in root_path.rglob("*.py"):
            if not self.include_tests and path.name.startswith("test_"):
                continue
            scanned_count += 1
            usages = self.scan_file(str(path), repo_url=repo_url, branch=branch)
            if usages:
                files_with_matches += 1
                all_usages.extend(usages)

        summary = self._build_cache_type_summary(all_usages)

        return CrawlReport(
            target_source=str(dir_path),
            total_files_scanned=scanned_count,
            files_with_usages=files_with_matches,
            total_usages_found=len(all_usages),
            repo_url=repo_url,
            cache_type_summary=summary,
            usages=all_usages,
        )

    def scan_github_repo(self, repo_name: str, branch: str = "main") -> CrawlReport:
        """
        Crawl a remote GitHub repository via GitHub Trees API and scan all Python files.
        Example repo_name: 'googleapis/python-bigquery'
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
# REPORT GENERATOR & FORMATTER
# ================================================================================

def export_markdown_report(report: CrawlReport, output_path: str):
    """Generate a clean Markdown summary report with clickable repo & file links."""
    repo_link_str = f"[{report.repo_url}]({report.repo_url})" if report.repo_url else "`N/A (Local directory)`"
    md_lines = [
        f"# FSSPEC Open Usage & Cache_Type Crawl Report",
        f"",
        f"- **Target Source:** `{report.target_source}`",
        f"- **Repository URL:** {repo_link_str}",
        f"- **Total Files Scanned:** `{report.total_files_scanned}`",
        f"- **Files with Usages:** `{report.files_with_usages}`",
        f"- **Total Usages Found:** `{report.total_usages_found}`",
        f"",
        f"### Cache_Type Breakdown",
        f"",
    ]

    if report.cache_type_summary:
        md_lines.append("| Cache_Type Option | Occurrences | Description |")
        md_lines.append("| :--- | :--- | :--- |")
        descriptions = {
            "readahead": "Default prefetching chunks for sequential reads",
            "mmap": "Memory-mapped temporary file for random access (Parquet/ORC)",
            "block": "Fixed-size block memory cache",
            "none": "No cache, direct HTTP Range GET requests",
            "bytes": "Dictionary of exact byte ranges in RAM",
            "background": "Async background block prefetching",
            "file": "Downloads complete file to local disk first",
            "NOT_EXPLICIT": "cache_type keyword omitted (uses fsspec default)"
        }
        for ct, cnt in report.cache_type_summary.items():
            desc = descriptions.get(ct, "Custom cache strategy")
            md_lines.append(f"| `{ct}` | `{cnt}` | {desc} |")
        md_lines.append("")

    md_lines.extend([
        f"---",
        f"",
        f"## Detected Usages",
        f"",
    ])

    if not report.usages:
        md_lines.append("No usages of `fsspec.open` or related calls were found in this codebase.")
    else:
        for idx, usage in enumerate(report.usages, start=1):
            func_info = f"`{usage.enclosing_class}.{usage.enclosing_function}`" if usage.enclosing_class else f"`{usage.enclosing_function or 'global'}`"
            file_link_str = f"[{usage.file_path}]({usage.file_url})" if usage.file_url else f"`{usage.file_path}`"
            md_lines.extend([
                f"### {idx}. {file_link_str} (Line {usage.line_number})",
                f"- **Line Link:** {usage.file_url}",
                f"- **Target Call:** `{usage.target_name}`",
                f"- **Cache_Type:** `{usage.cache_type}`",
                f"- **Cache_Options:** `{usage.cache_options or 'None'}`",
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
# BUILT-IN DEMONSTRATION MODE WITH REPO URLS
# ================================================================================

DEMO_MOCK_FILES = {
    "google/cloud/bigquery/exporter.py": """
import fsspec
from google.cloud import bigquery

class BigQueryToGCSExporter:
    def __init__(self, project_id: str):
        self.client = bigquery.Client(project=project_id)
        self.fs = fsspec.filesystem("gcs")

    def export_and_stream_parquet(self, table_id: str, gcs_uri: str):
        # 1. Open with cache_type='mmap' for random seeking across Parquet footer
        with fsspec.open(gcs_uri, mode="rb", cache_type="mmap", compression="snappy") as stream:
            header = stream.read(100)
            return header

    def read_csv_chunks(self, gcs_path: str):
        # 2. Open with cache_type='readahead' for sequential line reading
        with fsspec.open(gcs_path, "r", cache_type="readahead", cache_options={"block_size": 2 * 1024 * 1024}) as f:
            lines = [f.readline() for _ in range(10)]
            return lines

    def read_block_cached(self, gcs_path: str):
        # 3. Open with cache_type='block'
        with fsspec.open(gcs_path, "rb", cache_type="block", cache_options={"block_size": 1048576}) as f:
            return f.read(500)
""",
    "google/cloud/bigquery/custom_fsspec_reader.py": """
from fsspec import open as fs_open
from fsspec.core import url_to_fs

def load_bq_uncached(uri: str):
    # 4. Open with cache_type='none' for direct uncached streaming
    with fs_open(uri, "rb", cache_type="none") as f:
        return f.read()

def load_bq_default_cache(uri: str):
    # 5. Omitted cache_type (defaults to fsspec readahead or filesystem default)
    with fs_open(uri, "rb") as f:
        return f.read()
"""
}


def run_demo():
    """Run a demonstration scan using synthetic BigQuery + fsspec sample files with GitHub repo links."""
    print("=" * 80)
    print("RUNNING DEMO: FSSPEC OPEN & CACHE_TYPE EXTRACTOR FOR BIGQUERY")
    print("=" * 80)

    demo_repo_url = "https://github.com/googleapis/python-bigquery"
    demo_branch = "main"
    engine = FsspecCrawlerEngine()
    all_usages: List[FsspecUsage] = []
    scanned = len(DEMO_MOCK_FILES)
    matches = 0

    for file_path, code in DEMO_MOCK_FILES.items():
        usages = engine.scan_code(file_path, code, repo_url=demo_repo_url, branch=demo_branch)
        if usages:
            matches += 1
            all_usages.extend(usages)

    report = CrawlReport(
        target_source="googleapis/python-bigquery",
        total_files_scanned=scanned,
        files_with_usages=matches,
        total_usages_found=len(all_usages),
        repo_url=demo_repo_url,
        cache_type_summary=engine._build_cache_type_summary(all_usages),
        usages=all_usages,
    )

    print(f"\n[SUMMARY]")
    print(f"Target Source:     {report.target_source}")
    print(f"Repository URL:    {report.repo_url}")
    print(f"Total Files:       {report.total_files_scanned}")
    print(f"Files with Usages: {report.files_with_usages}")
    print(f"Total Usages:      {report.total_usages_found}")
    print(f"Cache_Type Summary:{report.cache_type_summary}\n")

    print("[DETAILED DETECTIONS]")
    for idx, u in enumerate(report.usages, start=1):
        print(f"\nDetection #{idx}:")
        print(f"  File:          {u.file_path}:{u.line_number}")
        print(f"  Repo Link:     {u.repo_url}")
        print(f"  File Line URL: {u.file_url}")
        print(f"  Target:        {u.target_name}")
        print(f"  Cache_Type:    {u.cache_type}")
        print(f"  Cache_Options: {u.cache_options or 'None'}")
        print(f"  Context:       Class={u.enclosing_class}, Function={u.enclosing_function}")
        print(f"  Code Snippet:\n    {u.code_snippet}")

    # Generate JSON output representation
    print("\n[JSON OUTPUT REPORT (SAMPLE)]")
    print(json.dumps(report.to_dict(), indent=2))


# ================================================================================
# CLI ENTRY POINT
# ================================================================================

def main():
    parser = argparse.ArgumentParser(description="Extract fsspec open usages, cache_type options, and repo URLs from Python BigQuery codebases.")
    parser.add_argument("--dir", "-d", help="Path to local directory to scan")
    parser.add_argument("--file", "-f", help="Path to single Python file to scan")
    parser.add_argument("--repo", "-r", help="GitHub repository (e.g. googleapis/python-bigquery)")
    parser.add_argument("--branch", "-b", default="main", help="GitHub branch (default: main)")
    parser.add_argument("--output-json", "-o", help="Path to write output JSON report")
    parser.add_argument("--output-md", "-m", help="Path to write output Markdown report")
    parser.add_argument("--demo", action="store_true", help="Run built-in demo scan")

    args = parser.parse_args()

    if args.demo or not any([args.dir, args.file, args.repo]):
        run_demo()
        return

    engine = FsspecCrawlerEngine()
    report: Optional[CrawlReport] = None

    if args.file:
        repo_url, branch = detect_git_repo_info(str(Path(args.file).parent.resolve()))
        usages = engine.scan_file(args.file, repo_url=repo_url, branch=branch)
        report = CrawlReport(
            target_source=args.file,
            total_files_scanned=1,
            files_with_usages=1 if usages else 0,
            total_usages_found=len(usages),
            repo_url=repo_url,
            cache_type_summary=engine._build_cache_type_summary(usages),
            usages=usages,
        )
    elif args.dir:
        report = engine.scan_directory(args.dir)
    elif args.repo:
        report = engine.scan_github_repo(args.repo, branch=args.branch)

    if report:
        print(f"Crawled '{report.target_source}': Found {report.total_usages_found} usages in {report.files_with_usages}/{report.total_files_scanned} files.")
        print(f"Repository Link: {report.repo_url or 'Local directory'}")
        print(f"Cache_Type Breakdown: {report.cache_type_summary}")
        if args.output_json:
            Path(args.output_json).write_text(json.dumps(report.to_dict(), indent=2), encoding="utf-8")
            print(f"JSON report saved to: {args.output_json}")
        if args.output_md:
            export_markdown_report(report, args.output_md)


if __name__ == "__main__":
    main()
