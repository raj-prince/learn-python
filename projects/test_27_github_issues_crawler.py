#!/usr/bin/env python3
"""
Unit tests for 27_github_issues_crawler.py
"""

import json
import pytest
import sys
from pathlib import Path
from importlib import import_module

sys.path.insert(0, str(Path(__file__).parent.resolve()))
crawler_module = import_module("27_github_issues_crawler")

IssuePerformanceAnalyzer = crawler_module.IssuePerformanceAnalyzer
GitHubIssue = crawler_module.GitHubIssue
IssueCrawlReport = crawler_module.IssueCrawlReport
export_issues_csv = crawler_module.export_issues_csv
export_issues_markdown = crawler_module.export_issues_markdown


def test_issue_analyzer_performance_and_fs_match():
    analyzer = IssuePerformanceAnalyzer()
    raw_issue = {
        "number": 101,
        "title": "fsspec read is very slow with gcsfs readahead",
        "body": "When reading large parquet files using fsspec.open, the latency is high due to chunk_size buffering.",
        "html_url": "https://github.com/dask/dask/issues/101",
        "state": "open",
        "created_at": "2026-01-01T00:00:00Z",
        "updated_at": "2026-01-02T00:00:00Z",
        "labels": [{"name": "performance"}, {"name": "io"}],
        "user": {"login": "testuser"}
    }

    issue = analyzer.analyze_issue("dask/dask", raw_issue)
    assert issue is not None
    assert issue.issue_number == 101
    assert "fsspec" in issue.matched_fs_keywords
    assert "gcsfs" in issue.matched_fs_keywords
    assert "slow" in issue.matched_perf_keywords
    assert "latency" in issue.matched_perf_keywords
    assert issue.relevance_score > 10


def test_issue_analyzer_irrelevant_issue():
    analyzer = IssuePerformanceAnalyzer()
    raw_issue = {
        "number": 202,
        "title": "Fix typo in documentation README",
        "body": "There is a spelling mistake in the main title.",
        "html_url": "https://github.com/dask/dask/issues/202",
        "state": "open",
        "labels": [],
        "user": {"login": "docuser"}
    }

    issue = analyzer.analyze_issue("dask/dask", raw_issue)
    assert issue is None


def test_issue_analyzer_skip_pull_request():
    analyzer = IssuePerformanceAnalyzer()
    raw_issue = {
        "number": 303,
        "title": "fsspec performance optimization PR",
        "body": "Improves fsspec latency by 2x",
        "html_url": "https://github.com/dask/dask/pull/303",
        "state": "open",
        "pull_request": {"url": "https://api.github.com/repos/dask/dask/pulls/303"},
        "user": {"login": "contributor"}
    }

    issue = analyzer.analyze_issue("dask/dask", raw_issue)
    assert issue is None


def test_issue_analyzer_fsspec_repo_implicit_fs():
    analyzer = IssuePerformanceAnalyzer()
    raw_issue = {
        "number": 404,
        "title": "High memory leak during multi-threaded chunk download",
        "body": "Download stalls and causes throughput drop after 100MB.",
        "html_url": "https://github.com/fsspec/gcsfs/issues/404",
        "state": "open",
        "labels": [{"name": "perf"}],
        "user": {"login": "gcsuser"}
    }

    issue = analyzer.analyze_issue("fsspec/gcsfs", raw_issue)
    assert issue is not None
    assert "repo:fsspec" in issue.matched_fs_keywords
    assert "memory leak" in issue.matched_perf_keywords or "throughput" in issue.matched_perf_keywords


def test_issues_csv_and_markdown_exports(tmp_path):
    issue = GitHubIssue(
        repo_name="fsspec/gcsfs",
        issue_number=505,
        title="gcsfs read_block latency issue",
        html_url="https://github.com/fsspec/gcsfs/issues/505",
        state="open",
        created_at="2026-02-01T00:00:00Z",
        updated_at="2026-02-02T00:00:00Z",
        author="benchuser",
        labels=["perf", "gcs"],
        matched_fs_keywords=["gcsfs"],
        matched_perf_keywords=["latency", "slow"],
        relevance_score=18,
        body_snippet="read_block takes too long on GCS",
    )

    report = IssueCrawlReport(
        target_repo="fsspec/gcsfs",
        total_issues_scanned=10,
        matched_issues_count=1,
        repo_url="https://github.com/fsspec/gcsfs",
        issues=[issue],
    )

    csv_path = tmp_path / "report.csv"
    export_issues_csv([report], str(csv_path))
    assert csv_path.exists()
    content_csv = csv_path.read_text(encoding="utf-8")
    assert "fsspec/gcsfs" in content_csv
    assert "gcsfs read_block latency issue" in content_csv

    md_path = tmp_path / "report.md"
    export_issues_markdown([report], str(md_path))
    assert md_path.exists()
    content_md = md_path.read_text(encoding="utf-8")
    assert "GitHub Issues Performance & FSSPEC Crawl Report" in content_md
    assert "gcsfs read_block latency issue" in content_md
