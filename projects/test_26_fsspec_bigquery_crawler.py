#!/usr/bin/env python3
"""
Unit tests for 26_fsspec_bigquery_crawler.py
"""

import json
import os
import tempfile
import pytest
import sys
from pathlib import Path
from importlib import import_module

sys.path.insert(0, str(Path(__file__).parent.resolve()))
crawler_module = import_module("26_fsspec_bigquery_crawler")
FsspecASTVisitor = crawler_module.FsspecASTVisitor
FsspecCrawlerEngine = crawler_module.FsspecCrawlerEngine
FsspecUsage = crawler_module.FsspecUsage
CrawlReport = crawler_module.CrawlReport
export_markdown_report = crawler_module.export_markdown_report


def test_fsspec_direct_open():
    code = """
import fsspec

def read_gcs(url):
    with fsspec.open(url, "rb") as f:
        return f.read()
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("test.py", code)
    assert len(usages) == 1
    u = usages[0]
    assert u.target_name == "fsspec.open"
    assert u.enclosing_function == "read_gcs"
    assert u.args == ["url", "'rb'"]
    assert u.cache_type == "NOT_EXPLICIT"
    assert u.line_number == 5


def test_repo_url_and_file_url():
    code = """
import fsspec

def read_parquet_mmap(url):
    with fsspec.open(url, "rb", cache_type="mmap") as f:
        return f.read()
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("google/cloud/bigquery/client.py", code, repo_url="https://github.com/googleapis/python-bigquery", branch="main")
    assert len(usages) == 1
    u = usages[0]
    assert u.repo_url == "https://github.com/googleapis/python-bigquery"
    assert u.file_url == "https://github.com/googleapis/python-bigquery/blob/main/google/cloud/bigquery/client.py#L5"


def test_cache_type_extraction():
    code = """
import fsspec

def read_parquet_mmap(url):
    with fsspec.open(url, "rb", cache_type="mmap") as f:
        return f.read()

def read_csv_block(url):
    with fsspec.open(url, "r", cache_type="block", cache_options={"block_size": 1048576}) as f:
        return f.read()
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("cache_test.py", code)
    assert len(usages) == 2
    
    assert usages[0].cache_type == "mmap"
    assert usages[0].cache_options is None

    assert usages[1].cache_type == "block"
    assert usages[1].cache_options == "{'block_size': 1048576}"


def test_fsspec_aliased_import():
    code = """
from fsspec import open as my_open

class Loader:
    def load(self, path):
        f = my_open(path, mode="w", compression="gzip", cache_type="none")
        return f
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("loader.py", code)
    assert len(usages) == 1
    u = usages[0]
    assert u.target_name == "my_open"
    assert u.enclosing_class == "Loader"
    assert u.enclosing_function == "load"
    assert u.cache_type == "none"
    assert u.kwargs == {"mode": "'w'", "compression": "'gzip'", "cache_type": "'none'"}


def test_filesystem_object_open():
    code = """
import fsspec

class BQHandler:
    def __init__(self):
        self.fs = fsspec.filesystem("gcs")
    
    def read_data(self, path):
        with self.fs.open(path, "r") as stream:
            return stream.readlines()
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("bq_handler.py", code)
    assert len(usages) == 2
    assert usages[0].target_name == "fsspec.filesystem"
    u = usages[1]
    assert u.target_name == "self.fs.open"
    assert u.enclosing_class == "BQHandler"
    assert u.enclosing_function == "read_data"


def test_fsspec_url_to_fs():
    code = """
from fsspec.core import url_to_fs

def process_file(uri):
    fs, path = url_to_fs(uri)
    return fs
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("url_fs.py", code)
    assert len(usages) == 1
    u = usages[0]
    assert u.target_name == "url_to_fs"
    assert u.enclosing_function == "process_file"


def test_syntax_error_fallback():
    invalid_code = """
import fsspec
def broken_func(
    with fsspec.open("gs://bucket/file.csv", cache_type="readahead") as f:
        pass
"""
    engine = FsspecCrawlerEngine(use_regex_fallback=True)
    usages = engine.scan_code("broken.py", invalid_code)
    assert len(usages) >= 1
    assert usages[0].detection_method == "regex"
    assert usages[0].cache_type == "readahead"


def test_directory_scan_and_report_export(tmp_path):
    f1 = tmp_path / "sample1.py"
    f1.write_text("import fsspec\nwith fsspec.open('gs://b/f.csv', cache_type='mmap'): pass", encoding="utf-8")
    
    f2 = tmp_path / "sample2.py"
    f2.write_text("print('no fsspec here')", encoding="utf-8")

    engine = FsspecCrawlerEngine()
    report = engine.scan_directory(str(tmp_path))

    assert report.total_files_scanned == 2
    assert report.files_with_usages == 1
    assert report.total_usages_found == 1
    assert report.cache_type_summary == {"mmap": 1}

    # Test Markdown report generation
    md_file = tmp_path / "report.md"
    export_markdown_report(report, str(md_file))
    assert md_file.exists()
    assert "FSSPEC Open Usage & Cache_Type Crawl Report" in md_file.read_text(encoding="utf-8")
