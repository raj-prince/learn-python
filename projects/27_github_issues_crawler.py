#!/usr/bin/env python3
"""
================================================================================
LESSON 27 / GITHUB ISSUES PERFORMANCE CRAWLER
================================================================================

This module crawls open (or closed) GitHub issues across target repositories,
identifying and categorizing performance issues related to fsspec, gcsfs,
filesystem caching, I/O bottlenecks, and cloud storage integrations.

--------------------------------------------------------------------------------
USAGE EXAMPLES:
--------------------------------------------------------------------------------
1. Scan open issues for a specific repository:
   python projects/27_github_issues_crawler.py --repo dask/dask --output-md dask_issues.md

2. Scan open issues for fsspec & gcsfs repositories:
   python projects/27_github_issues_crawler.py --repo fsspec/filesystem_spec fsspec/gcsfs --output-csv fsspec_issues.csv --output-md fsspec_issues.md

3. Scan all default open-source AI & data repositories:
   python projects/27_github_issues_crawler.py --all --output-csv all_issues.csv --output-json all_issues.json --output-md all_issues.md
"""

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

# ================================================================================
# KEYWORDS & DEFAULT TARGET REPOSITORIES
# ================================================================================

FILESYSTEM_KEYWORDS: Set[str] = {
    "fsspec",
    "gcsfs",
    "s3fs",
    "abfs",
    "pyarrow.fs",
    "filesystem",
    "abstractfilesystem",
    "gcsfilesystem",
    "s3filesystem",
    "open_files",
    "url_to_fs",
    "cache_type",
    "simple_cache",
    "readahead",
    "blockcache",
    "mmap",
    "parts",
}

PERFORMANCE_KEYWORDS: Set[str] = {
    "performance",
    "slow",
    "slowness",
    "latency",
    "throughput",
    "bottleneck",
    "benchmark",
    "speed",
    "speedup",
    "hang",
    "hanging",
    "stall",
    "stalled",
    "timeout",
    "memory leak",
    "high memory",
    "oom",
    "cpu utilization",
    "prefetch",
    "prefetching",
    "caching",
    "cache",
    "chunk_size",
    "block_size",
    "range request",
    "io",
    "i/o",
    "concurrent",
    "multithreading",
}

PERFORMANCE_LABELS: Set[str] = {
    "performance",
    "perf",
    "speed",
    "latency",
    "memory",
    "io",
    "storage",
    "gcs",
    "fsspec",
}

DEFAULT_TARGET_REPOS: List[Tuple[str, str]] = [
    ("fsspec Core", "fsspec/filesystem_spec"),
    ("gcsfs", "fsspec/gcsfs"),
    ("s3fs", "fsspec/s3fs"),
    ("Dask", "dask/dask"),
    ("pandas", "pandas-dev/pandas"),
    ("xarray", "pydata/xarray"),
    ("zarr", "zarr-developers/zarr-python"),
    ("Apache Arrow", "apache/arrow"),
    ("Hugging Face Datasets", "huggingface/datasets"),
    ("PyTorch", "pytorch/pytorch"),
    ("Ray", "ray-project/ray"),
]


# ================================================================================
# DATA STRUCTURES FOR ISSUES
# ================================================================================

@dataclass
class GitHubIssue:
    """Represents a single parsed GitHub issue matched by the crawler."""
    repo_name: str
    issue_number: int
    title: str
    html_url: str
    state: str
    created_at: str
    updated_at: str
    author: str
    labels: List[str] = field(default_factory=list)
    matched_fs_keywords: List[str] = field(default_factory=list)
    matched_perf_keywords: List[str] = field(default_factory=list)
    relevance_score: int = 0
    body_snippet: str = ""

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)


@dataclass
class IssueCrawlReport:
    """Summary report of the issue crawling session."""
    target_repo: str
    total_issues_scanned: int
    matched_issues_count: int
    repo_url: str
    issues: List[GitHubIssue] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        data = asdict(self)
        data["issues"] = [i.to_dict() for i in self.issues]
        return data


# ================================================================================
# ISSUE ANALYZER & FILTER ENGINE
# ================================================================================

class IssuePerformanceAnalyzer:
    """Analyzes issue title, body, and labels to score performance and fsspec relevance."""

    def __init__(
        self,
        fs_keywords: Optional[Set[str]] = None,
        perf_keywords: Optional[Set[str]] = None,
    ):
        self.fs_keywords = fs_keywords or FILESYSTEM_KEYWORDS
        self.perf_keywords = perf_keywords or PERFORMANCE_KEYWORDS

    def analyze_issue(self, repo_name: str, issue_raw: Dict[str, Any]) -> Optional[GitHubIssue]:
        """
        Inspect raw GitHub REST API issue payload.
        Returns GitHubIssue object if relevant, or None if irrelevant.
        """
        # Skip pull requests (GitHub API returns PRs in /issues endpoint)
        if "pull_request" in issue_raw:
            return None

        title = issue_raw.get("title", "")
        body = issue_raw.get("body", "") or ""
        labels_raw = issue_raw.get("labels", [])
        labels = [lbl.get("name", "") if isinstance(lbl, dict) else str(lbl) for lbl in labels_raw]

        combined_text = f"{title}\n{body}".lower()
        labels_text = " ".join(labels).lower()

        # Match keywords
        matched_fs = [kw for kw in self.fs_keywords if kw in combined_text]
        matched_perf = [kw for kw in self.perf_keywords if kw in combined_text]

        # Label matching
        has_perf_label = any(pl in labels_text for pl in PERFORMANCE_LABELS)

        # Repos dedicated to filesystem (e.g. fsspec/gcsfs, fsspec/filesystem_spec) implicitly match FS
        is_filesystem_repo = "fsspec" in repo_name.lower() or "gcsfs" in repo_name.lower() or "s3fs" in repo_name.lower()
        if is_filesystem_repo and not matched_fs:
            matched_fs.append("repo:fsspec")

        # Determine relevance criteria:
        # 1. Must have at least 1 performance keyword or performance label.
        # 2. Must have at least 1 filesystem keyword (or belong to fsspec/gcsfs repo).
        if not (matched_perf or has_perf_label):
            return None
        if not matched_fs:
            return None

        # Calculate relevance score
        score = (len(matched_fs) * 2) + (len(matched_perf) * 3) + (10 if has_perf_label else 0)

        # Create body snippet (first 300 characters cleaned)
        clean_body = re.sub(r"\s+", " ", body).strip()
        snippet = clean_body[:300] + ("..." if len(clean_body) > 300 else "")

        user_info = issue_raw.get("user", {})
        author = user_info.get("login", "unknown") if isinstance(user_info, dict) else "unknown"

        return GitHubIssue(
            repo_name=repo_name,
            issue_number=issue_raw.get("number", 0),
            title=title,
            html_url=issue_raw.get("html_url", ""),
            state=issue_raw.get("state", "open"),
            created_at=issue_raw.get("created_at", ""),
            updated_at=issue_raw.get("updated_at", ""),
            author=author,
            labels=labels,
            matched_fs_keywords=sorted(list(set(matched_fs))),
            matched_perf_keywords=sorted(list(set(matched_perf))),
            relevance_score=score,
            body_snippet=snippet,
        )


# ================================================================================
# GITHUB ISSUES CRAWLER ENGINE
# ================================================================================

class GitHubIssuesCrawler:
    """Engine that fetches open issues from GitHub REST API and filters them."""

    def __init__(
        self,
        github_token: Optional[str] = None,
        max_issues_per_repo: int = 200,
        fs_keywords: Optional[Set[str]] = None,
        perf_keywords: Optional[Set[str]] = None,
    ):
        self.github_token = github_token or os.getenv("GITHUB_TOKEN")
        self.max_issues_per_repo = max_issues_per_repo
        self.analyzer = IssuePerformanceAnalyzer(fs_keywords, perf_keywords)

    def _make_request(self, url: str) -> Optional[Any]:
        """Execute HTTP GET request to GitHub API with headers."""
        headers = {"User-Agent": "Fsspec-Issues-Crawler-Python", "Accept": "application/vnd.github.v3+json"}
        if self.github_token:
            headers["Authorization"] = f"token {self.github_token}"

        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 403:
                print(f"GitHub API Rate Limit Exceeded or Forbidden for {url}", file=sys.stderr)
            elif e.code != 404:
                print(f"HTTP Error {e.code} for {url}: {e.reason}", file=sys.stderr)
            return None
        except Exception as e:
            print(f"Failed to fetch {url}: {e}", file=sys.stderr)
            return None

    def crawl_repository_issues(self, repo_name: str, state: str = "open") -> IssueCrawlReport:
        """
        Fetch and filter issues for a GitHub repository.
        e.g. repo_name = 'dask/dask' or 'fsspec/gcsfs'
        """
        repo_url = f"https://github.com/{repo_name}"
        scanned_issues = 0
        matched_issues: List[GitHubIssue] = []

        page = 1
        per_page = 100

        while scanned_issues < self.max_issues_per_repo:
            api_url = f"https://api.github.com/repos/{repo_name}/issues?state={state}&per_page={per_page}&page={page}"
            raw_data = self._make_request(api_url)

            if not raw_data or not isinstance(raw_data, list) or len(raw_data) == 0:
                break

            for issue_raw in raw_data:
                scanned_issues += 1
                parsed_issue = self.analyzer.analyze_issue(repo_name, issue_raw)
                if parsed_issue:
                    matched_issues.append(parsed_issue)

            if len(raw_data) < per_page:
                break

            page += 1

        # Sort matched issues by relevance score descending
        matched_issues.sort(key=lambda x: x.relevance_score, reverse=True)

        return IssueCrawlReport(
            target_repo=repo_name,
            total_issues_scanned=scanned_issues,
            matched_issues_count=len(matched_issues),
            repo_url=repo_url,
            issues=matched_issues,
        )


# ================================================================================
# EXPORT FORMATTERS (CSV, JSON, MARKDOWN)
# ================================================================================

def export_issues_csv(reports: List[IssueCrawlReport], output_path: str):
    """Export matched issues across reports to CSV format."""
    rows = []
    for r in reports:
        for issue in r.issues:
            rows.append([
                issue.repo_name,
                issue.issue_number,
                issue.title,
                issue.html_url,
                issue.state,
                issue.relevance_score,
                ", ".join(issue.labels),
                ", ".join(issue.matched_fs_keywords),
                ", ".join(issue.matched_perf_keywords),
                issue.author,
                issue.created_at,
                issue.body_snippet,
            ])

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "repository", "issue_number", "title", "html_url", "state",
            "relevance_score", "labels", "matched_fs_keywords",
            "matched_perf_keywords", "author", "created_at", "body_snippet"
        ])
        writer.writerows(rows)
    print(f"CSV report exported to: {output_path} ({len(rows)} issues)")


def export_issues_markdown(reports: List[IssueCrawlReport], output_path: str):
    """Generate a clean Markdown summary report of fsspec/performance issues."""
    total_scanned = sum(r.total_issues_scanned for r in reports)
    total_matched = sum(r.matched_issues_count for r in reports)

    md_lines = [
        f"# GitHub Issues Performance & FSSPEC Crawl Report",
        f"",
        f"- **Repositories Crawled:** `{len(reports)}`",
        f"- **Total Issues Scanned:** `{total_scanned}`",
        f"- **Matched Performance / FSSPEC Issues:** `{total_matched}`",
        f"",
        f"---",
        f"",
        f"## 📊 Repository Issue Breakdown",
        f"",
        f"| Repository | Issues Scanned | Matched Perf/FSSPEC Issues | Top Issue Link |",
        f"| :--- | :--- | :--- | :--- |"
    ]

    for r in reports:
        top_link = f"[#{r.issues[0].issue_number}]({r.issues[0].html_url})" if r.issues else "N/A"
        md_lines.append(f"| [{r.target_repo}]({r.repo_url}) | `{r.total_issues_scanned}` | `{r.matched_issues_count}` | {top_link} |")

    md_lines.extend([
        f"",
        f"---",
        f"",
        f"## 🔍 Detailed Matched Issues",
        f""
    ])

    idx = 1
    for r in reports:
        if not r.issues:
            continue
        md_lines.append(f"### [{r.target_repo}]({r.repo_url}) ({r.matched_issues_count} issues)")
        md_lines.append("")
        for issue in r.issues:
            labels_str = ", ".join([f"`{lbl}`" for lbl in issue.labels]) if issue.labels else "None"
            fs_str = ", ".join([f"`{k}`" for k in issue.matched_fs_keywords])
            perf_str = ", ".join([f"`{k}`" for k in issue.matched_perf_keywords])

            md_lines.extend([
                f"#### {idx}. [{issue.title}]({issue.html_url}) (#{issue.issue_number})",
                f"- **URL:** {issue.html_url}",
                f"- **Relevance Score:** `{issue.relevance_score}` | **State:** `{issue.state}` | **Author:** `{issue.author}`",
                f"- **Labels:** {labels_str}",
                f"- **FS Keywords:** {fs_str}",
                f"- **Perf Keywords:** {perf_str}",
                f"- **Excerpt:** *\"{issue.body_snippet}\"*",
                f"",
            ])
            idx += 1

    Path(output_path).write_text("\n".join(md_lines), encoding="utf-8")
    print(f"Markdown report exported to: {output_path}")


# ================================================================================
# CLI ENTRY POINT
# ================================================================================

def main():
    parser = argparse.ArgumentParser(description="Crawl GitHub repository open issues for fsspec, gcsfs, and I/O performance bottlenecks.")
    parser.add_argument("--repo", "-r", nargs="+", help="One or more GitHub repositories (e.g. --repo dask/dask fsspec/gcsfs)")
    parser.add_argument("--all", "-a", action="store_true", help="Crawl open issues across all 11 default repositories")
    parser.add_argument("--state", default="open", choices=["open", "closed", "all"], help="Issue state to scan (default: open)")
    parser.add_argument("--max-issues", type=int, default=200, help="Maximum issues to scan per repository (default: 200)")
    parser.add_argument("--github-token", help="GitHub API token to avoid rate limits (or set GITHUB_TOKEN env var)")
    parser.add_argument("--output-csv", "-c", help="Path to write output CSV report")
    parser.add_argument("--output-json", "-o", help="Path to write output JSON report")
    parser.add_argument("--output-md", "-m", help="Path to write output Markdown report")

    args = parser.parse_args()

    if args.all:
        target_repos = [repo for _, repo in DEFAULT_TARGET_REPOS]
    elif args.repo:
        target_repos = args.repo
    else:
        parser.error("Please specify --repo <owner/repo...> or --all")

    crawler = GitHubIssuesCrawler(
        github_token=args.github_token,
        max_issues_per_repo=args.max_issues,
    )

    reports: List[IssueCrawlReport] = []
    start_time = time.time()

    def _fetch_repo_issues(repo: str) -> IssueCrawlReport:
        print(f"[+] Crawling open issues for: {repo}...")
        report = crawler.crawl_repository_issues(repo, state=args.state)
        print(f"    - Scanned {report.total_issues_scanned} issues | Found {report.matched_issues_count} performance/fsspec matches.")
        return report

    with ThreadPoolExecutor(max_workers=5) as executor:
        reports = list(executor.map(_fetch_repo_issues, target_repos))

    elapsed = time.time() - start_time
    print(f"\nCompleted issue crawling across {len(reports)} repository target(s) in {elapsed:.2f} seconds.")

    # Export CSV
    if args.output_csv:
        export_issues_csv(reports, args.output_csv)

    # Export JSON
    if args.output_json:
        json_payload = {
            "summary": {
                "total_repositories": len(reports),
                "total_issues_scanned": sum(r.total_issues_scanned for r in reports),
                "matched_issues_count": sum(r.matched_issues_count for r in reports),
                "elapsed_seconds": round(elapsed, 2),
            },
            "per_repository": [r.to_dict() for r in reports],
        }
        Path(args.output_json).write_text(json.dumps(json_payload, indent=2), encoding="utf-8")
        print(f"JSON report saved to: {args.output_json}")

    # Export Markdown
    if args.output_md:
        export_issues_markdown(reports, args.output_md)


if __name__ == "__main__":
    main()
