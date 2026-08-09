# 🐍 FSSPEC & GCSFS MASTERCLASS

Welcome to the comprehensive **fsspec & GCSFileSystem** course directory. This dedicated suite covers **every single public method** exposed by `fsspec.spec.AbstractFileSystem` and `gcsfs.GCSFileSystem`.

---

## 📚 LESSON INDEX & COVERED METHODS

### 1. [`01_fsspec_core_and_instantiation.py`](file:///usr/local/google/home/princer/code/learn-python/fsspec_lessons/01_fsspec_core_and_instantiation.py)
- **Concepts:** Core architecture, factory patterns, protocol normalization, instance caching, and JSON serialization.
- **Methods Covered:**
  - `fsspec.filesystem("gcs", **kwargs)`
  - `gcsfs.GCSFileSystem(**kwargs)`
  - `protocol`, `unstrip_protocol(path)`
  - `cachable`, `clear_instance_cache()`
  - `from_dict(d)`, `to_dict()`
  - `from_json(json_str)`, `to_json()`
  - `split_path(path)`

### 2. [`02_path_and_metadata_operations.py`](file:///usr/local/google/home/princer/code/learn-python/fsspec_lessons/02_path_and_metadata_operations.py)
- **Concepts:** Listing, recursive tree traversal, glob wildcard matching, timestamps, hashes, and disk utilization.
- **Methods Covered:**
  - `ls()`, `listdir()`, `find()`, `glob()`, `walk()`, `tree()`
  - `info()`, `stat()`, `exists()`, `lexists()`, `isfile()`, `isdir()`
  - `size()`, `sizes()`, `created()`, `modified()`, `checksum()`, `ukey()`
  - `du()`, `disk_usage()`, `fsid`

### 3. [`03_file_reading_and_streaming.py`](file:///usr/local/google/home/princer/code/learn-python/fsspec_lessons/03_file_reading_and_streaming.py)
- **Concepts:** Streaming file handles, bulk byte reads, block offset reads, range requests, head/tail sampling, and disk downloading.
- **Methods Covered:**
  - `open()` (Returns `AbstractBufferedFile` / `GCSFile`)
  - `read_bytes()`, `read_text()`, `cat()`, `cat_file()`
  - `read_block()`, `cat_ranges()`, `head()`, `tail()`
  - `get()`, `get_file()`, `download()`

### 4. [`04_file_writing_upload_and_manipulation.py`](file:///usr/local/google/home/princer/code/learn-python/fsspec_lessons/04_file_writing_upload_and_manipulation.py)
- **Concepts:** Resumable uploads, piping memory data, server-side copying, atomic moves, and GCS object composition.
- **Methods Covered:**
  - `write_bytes()`, `write_text()`, `pipe()`, `pipe_file()`, `touch()`
  - `put()`, `put_file()`, `upload()`
  - `cp()`, `copy()`, `cp_file()`, `mv()`, `move()`, `mv_file()`, `rename()`
  - `merge()` (GCS Compose API)

### 5. [`05_directory_and_file_deletion_management.py`](file:///usr/local/google/home/princer/code/learn-python/fsspec_lessons/05_directory_and_file_deletion_management.py)
- **Concepts:** Prefix directories, recursive directory wiping, separators, root markers, and out-of-band cache invalidation.
- **Methods Covered:**
  - `mkdir()`, `makedir()`, `mkdirs()`, `makedirs()`
  - `rm()`, `delete()`, `rm_file()`, `rmdir()`
  - `invalidate_cache()`, `root_marker`, `sep`

### 6. [`06_transactions_and_batch_operations.py`](file:///usr/local/google/home/princer/code/learn-python/fsspec_lessons/06_transactions_and_batch_operations.py)
- **Concepts:** Transaction contexts, atomic multi-file updates, manual transaction lifecycle, and deferred batch commits.
- **Methods Covered:**
  - `transaction` (`with fs.transaction:`)
  - `start_transaction()`, `end_transaction()`
  - `transaction_type`

### 7. [`07_mappers_urls_signed_urls_and_advanced.py`](file:///usr/local/google/home/princer/code/learn-python/fsspec_lessons/07_mappers_urls_signed_urls_and_advanced.py)
- **Concepts:** Dict-like Key-Value `FSMap` integration, pre-signed HTTP URLs, GCS requester-pays, xattr metadata, and async options.
- **Methods Covered:**
  - `get_mapper(root_path)` (`FSMap` dictionary wrapper)
  - `url(path)`, `sign(path, expiration)`
  - `buckets()`, `make_bucket_requester_pays()`, `getxattr()`, `setxattrs()`
  - `disable_throttling()`, `close_session()`, `open_async()`, `async_impl`

---

## 🚀 HOW TO RUN THE LESSONS

You can run any lesson using Python:

```bash
# Run Lesson 1
python3 fsspec_lessons/01_fsspec_core_and_instantiation.py
```
