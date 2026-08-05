#!/usr/bin/env python3
"""
================================================================================
BATCH FSSPEC CRAWLER FOR MAJOR PYTHON DATA SCIENCE & ML LIBRARIES
================================================================================

Crawls and performs AST static analysis on 8 major open-source data repositories:
1. Dask (dask/dask)
2. Intake (intake/intake)
3. pandas (pandas-dev/pandas)
4. xarray (pydata/xarray)
5. zarr (zarr-developers/zarr-python)
6. DVC (iterative/dvc)
7. Kedro (kedro-org/kedro)
8. Hugging Face Datasets (huggingface/datasets)

Generates combined outputs:
- fsspec_crawl_results.csv (CSV format for data analysis)
- combined_fsspec_report.json (JSON format)
- combined_fsspec_report.md (Markdown format)
"""

import csv
import json
import os
import sys
import time
from pathlib import Path
from typing import Dict, List

# Import crawler engine from 26_fsspec_bigquery_crawler
from importlib import import_module
sys.path.insert(0, str(Path(__file__).resolve().parent))
crawler_module = import_module("26_fsspec_bigquery_crawler")

FsspecCrawlerEngine = crawler_module.FsspecCrawlerEngine
CrawlReport = crawler_module.CrawlReport
FsspecUsage = crawler_module.FsspecUsage
export_markdown_report = crawler_module.export_markdown_report

TARGET_REPOS = [
    ("Dask", "dask/dask"),
    ("Intake", "intake/intake"),
    ("pandas", "pandas-dev/pandas"),
    ("xarray", "pydata/xarray"),
    ("zarr", "zarr-developers/zarr-python"),
    ("DVC", "iterative/dvc"),
    ("Kedro", "kedro-org/kedro"),
    ("Hugging Face Datasets", "huggingface/datasets"),
]

def crawl_all():
    print("=" * 80)
    print("STARTING BATCH FSSPEC CRAWL ACROSS 8 MAJOR REPOSITORIES")
    print("=" * 80)
    
    engine = FsspecCrawlerEngine(use_regex_fallback=True)
    all_reports: List[CrawlReport] = []
    combined_usages: List[FsspecUsage] = []
    
    start_time = time.time()
    
    for title, repo in TARGET_REPOS:
        print(f"\n[+] Crawling {title} ({repo})...")
        # Try main branch first, fall back to master if empty
        report = engine.scan_github_repo(repo, branch="main")
        if report.total_files_scanned == 0:
            report = engine.scan_github_repo(repo, branch="master")
            
        print(f"    - Scanned {report.total_files_scanned} files | Found {report.total_usages_found} usages in {report.files_with_usages} files.")
        print(f"    - Cache_Type Summary: {report.cache_type_summary}")
        all_reports.append(report)
        combined_usages.extend(report.usages)
        
    elapsed = time.time() - start_time
    print("\n" + "=" * 80)
    print(f"BATCH CRAWL COMPLETED IN {elapsed:.2f} SECONDS")
    print("=" * 80)
    
    # Calculate global totals
    total_files = sum(r.total_files_scanned for r in all_reports)
    total_matches_files = sum(r.files_with_usages for r in all_reports)
    total_usages = len(combined_usages)
    
    global_cache_summary: Dict[str, int] = {}
    for u in combined_usages:
        global_cache_summary[u.cache_type] = global_cache_summary.get(u.cache_type, 0) + 1
        
    base_dir = Path(__file__).resolve().parent

    # 1. Export CSV
    csv_path = base_dir / "fsspec_crawl_results.csv"
    csv_rows = []
    for r in all_reports:
        repo_name = r.target_source.replace("GitHub:", "").split()[0]
        for u in r.usages:
            csv_rows.append([
                repo_name,
                u.file_path,
                u.line_number,
                u.target_name,
                u.cache_type,
                u.is_specified_cache_keyword,
                u.cache_options or "None",
                u.enclosing_class or "None",
                u.enclosing_function or "global",
                u.file_url,
                u.code_snippet.replace("\n", " ")
            ])

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "repository", "file_path", "line_number", "target_name",
            "cache_type", "is_specified_cache_keyword", "cache_options",
            "enclosing_class", "enclosing_function", "file_url", "code_snippet"
        ])
        writer.writerows(csv_rows)
    print(f"\nSaved CSV report ({len(csv_rows)} rows) to: {csv_path}")

    # 2. Save combined output JSON
    json_path = base_dir / "combined_fsspec_report.json"
    json_data = {
        "summary": {
            "total_repositories": len(TARGET_REPOS),
            "total_files_scanned": total_files,
            "files_with_usages": total_matches_files,
            "total_usages_found": total_usages,
            "cache_type_summary": global_cache_summary,
            "elapsed_seconds": round(elapsed, 2)
        },
        "per_repository": [r.to_dict() for r in all_reports]
    }
    json_path.write_text(json.dumps(json_data, indent=2), encoding="utf-8")
    print(f"Saved combined JSON report to: {json_path}")
    
    # 3. Generate combined Markdown Report
    md_path = base_dir / "combined_fsspec_report.md"
    md_lines = [
        f"# Master FSSPEC Usage Report Across 8 Major Python Ecosystem Repositories",
        f"",
        f"- **Repositories Crawled:** `{len(TARGET_REPOS)}`",
        f"- **Total Files Scanned:** `{total_files}`",
        f"- **Files with FSSPEC Usages:** `{total_matches_files}`",
        f"- **Total FSSPEC Usages Detected:** `{total_usages}`",
        f"- **Time Elapsed:** `{elapsed:.2f} seconds`",
        f"",
        f"---",
        f"",
        f"## 📊 Repository Summary Table",
        f"",
        f"| Project Name | Repository | Files Scanned | Files w/ Usages | Total Usages | Cache_Types |",
        f"| :--- | :--- | :--- | :--- | :--- | :--- |"
    ]
    
    for r in all_reports:
        repo_name = r.target_source.replace("GitHub:", "").split()[0]
        title = next((t for t, rep in TARGET_REPOS if rep == repo_name), repo_name)
        ct_str = ", ".join([f"{k}:{v}" for k, v in r.cache_type_summary.items()]) if r.cache_type_summary else "None"
        md_lines.append(f"| **{title}** | [{repo_name}](https://github.com/{repo_name}) | `{r.total_files_scanned}` | `{r.files_with_usages}` | `{r.total_usages_found}` | `{ct_str}` |")
        
    md_lines.extend([
        f"",
        f"---",
        f"",
        f"## 📈 Global Cache_Type Breakdown",
        f"",
        f"| Cache_Type Option | Total Occurrences | Description |",
        f"| :--- | :--- | :--- |"
    ])
    
    descriptions = {
        "readahead": "Default prefetching chunks for sequential reading",
        "mmap": "Memory-mapped temporary file for random binary/columnar seeking (Parquet/ORC)",
        "block": "Fixed-size block memory caching",
        "none": "No cache, direct HTTP Range GET requests",
        "bytes": "Dictionary of exact byte ranges in RAM",
        "background": "Async background block prefetching",
        "file": "Downloads complete file to local disk first",
        "NOT_EXPLICIT": "cache_type keyword omitted (uses default fsspec strategy)"
    }
    
    for ct, cnt in global_cache_summary.items():
        desc = descriptions.get(ct, "Custom cache strategy")
        md_lines.append(f"| `{ct}` | `{cnt}` | {desc} |")
        
    md_lines.extend([
        f"",
        f"---",
        f"",
        f"## 🔍 Detailed Usage Breakdown by Repository",
        f""
    ])
    
    for r in all_reports:
        repo_name = r.target_source.replace("GitHub:", "").split()[0]
        title = next((t for t, rep in TARGET_REPOS if rep == repo_name), repo_name)
        md_lines.extend([
            f"### {title} ([{repo_name}](https://github.com/{repo_name}))",
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
                    f"- **Target Call:** `{usage.target_name}` | **Cache_Type:** `{usage.cache_type}`",
                    f"- **Context:** {func_info}",
                    f"- **Arguments:** `{', '.join(usage.args)}`",
                    f"- **Keywords:** `{usage.kwargs}`",
                    f"",
                    f"```python",
                    f"{usage.code_snippet}",
                    f"```",
                    f""
                ])
                
    md_path.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"Generated Master Markdown report at: {md_path}")

if __name__ == "__main__":
    crawl_all()
