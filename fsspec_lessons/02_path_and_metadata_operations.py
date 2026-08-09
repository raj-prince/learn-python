#!/usr/bin/env python3
"""
================================================================================
FSSPEC LESSON 02: PATH DISCOVERY, METADATA & STATISTICAL OPERATIONS
================================================================================

In cloud object stores like Google Cloud Storage (GCS), there are no real "directories";
paths are flat key-value object names containing forward slashes. `fsspec` presents a unified
POSIX-like virtual directory view over both in-memory and cloud storage backends.

In this lesson, we explore every path listing, matching, recursive discovery, and
metadata extraction method in both `memory://` and `gcs://` (`princer-working-dirs`).

--------------------------------------------------------------------------------
EXPOSED METHODS COVERED IN THIS LESSON:
--------------------------------------------------------------------------------
- Directory Listing & Discovery : `ls()`, `listdir()`, `find()`, `glob()`, `walk()`, `tree()`
- Metadata & Attributes        : `info()`, `stat()`, `exists()`, `lexists()`, `isfile()`, `isdir()`
- File Statistics & Hashes     : `size()`, `sizes()`, `created()`, `modified()`, `checksum()`, `ukey()`
- Disk & Footprint Utilization : `du()`, `disk_usage()`, `fsid`
"""

import time
import fsspec
import gcsfs

BUCKET_NAME = "princer-working-dirs"
GCS_PREFIX = f"{BUCKET_NAME}/fsspec_demo_lesson2"


# ================================================================================
# PART 1: DIRECTORY LISTING & RECURSIVE DISCOVERY (IN-MEMORY vs GCS)
# ================================================================================

def demonstrate_path_discovery():
    print("\n" + "=" * 80)
    print("PART 1: DIRECTORY LISTING & RECURSIVE DISCOVERY")
    print("=" * 80)

    # --------------------------------------------------------------------------
    # A. In-Memory Filesystem (memory://)
    # --------------------------------------------------------------------------
    print("--- [A] IN-MEMORY FILESYSTEM (memory://) ---")
    mem_fs = fsspec.filesystem("memory")
    mem_fs.pipe("mem_bucket/logs/2026/app.log", b"Log line 1\nLog line 2")
    mem_fs.pipe("mem_bucket/data/records.csv", b"id,name\n1,Alice\n2,Bob")

    print("1. mem_fs.ls('mem_bucket'):", mem_fs.ls("mem_bucket"))
    print("2. mem_fs.glob('mem_bucket/**/*.log'):", mem_fs.glob("mem_bucket/**/*.log"))
    print("3. mem_fs.find('mem_bucket'):", mem_fs.find("mem_bucket"))

    # --------------------------------------------------------------------------
    # B. GCS Cloud Filesystem (gs://princer-working-dirs)
    # --------------------------------------------------------------------------
    print("\n--- [B] GCS CLOUD FILESYSTEM (gs://princer-working-dirs) ---")
    gcs_fs = fsspec.filesystem("gcs")
    gcs_fs.pipe(f"{GCS_PREFIX}/logs/2026/app.log", b"Log line 1\nLog line 2")
    gcs_fs.pipe(f"{GCS_PREFIX}/data/records.csv", b"id,name\n1,Alice\n2,Bob")

    print(f"1. gcs_fs.ls('{GCS_PREFIX}'):", gcs_fs.ls(GCS_PREFIX))
    print(f"2. gcs_fs.glob('{GCS_PREFIX}/**/*.log'):", gcs_fs.glob(f"{GCS_PREFIX}/**/*.log"))
    print(f"3. gcs_fs.find('{GCS_PREFIX}'):", gcs_fs.find(GCS_PREFIX))

    print(f"\n4. gcs_fs.walk('{GCS_PREFIX}'):")
    for root, dirs, files in gcs_fs.walk(GCS_PREFIX):
        print(f"   Root: {root} | Dirs: {dirs} | Files: {files}")


# ================================================================================
# PART 2: FILE METADATA, TIME STAMPS & HASHING (IN-MEMORY vs GCS)
# ================================================================================

def demonstrate_metadata_and_hashes():
    print("\n" + "=" * 80)
    print("PART 2: FILE METADATA, STATS & HASHES")
    print("=" * 80)

    content = b'{"status": "OK", "total": 100}'

    # --------------------------------------------------------------------------
    # A. In-Memory Filesystem
    # --------------------------------------------------------------------------
    print("--- [A] IN-MEMORY METADATA ---")
    mem_fs = fsspec.filesystem("memory")
    mem_path = "mem_bucket/reports/q1.json"
    mem_fs.pipe(mem_path, content)
    print(f"info('{mem_path}'): {mem_fs.info(mem_path)}")
    print(f"checksum('{mem_path}'): {mem_fs.checksum(mem_path)}")

    # --------------------------------------------------------------------------
    # B. GCS Cloud Filesystem
    # --------------------------------------------------------------------------
    print("\n--- [B] GCS CLOUD METADATA ---")
    gcs_fs = fsspec.filesystem("gcs")
    gcs_path = f"{GCS_PREFIX}/reports/q1.json"
    gcs_fs.pipe(gcs_path, content)

    info = gcs_fs.info(gcs_path)
    print(f"1. gcs_fs.info('{gcs_path}'):")
    print(f"   Type: {info.get('type')} | Size: {info.get('size')} | Generation: {info.get('generation')}")

    print(f"\n2. GCS Existence & Attributes:")
    print(f"   exists('{gcs_path}') : {gcs_fs.exists(gcs_path)}")
    print(f"   isfile('{gcs_path}') : {gcs_fs.isfile(gcs_path)}")
    print(f"   size('{gcs_path}')   : {gcs_fs.size(gcs_path)} bytes")
    print(f"   created('{gcs_path}'): {gcs_fs.created(gcs_path)}")
    print(f"   ukey('{gcs_path}')   : {gcs_fs.ukey(gcs_path)} (GCS generation hash)")
    print(f"   checksum('{gcs_path}'): {gcs_fs.checksum(gcs_path)}")


# ================================================================================
# PART 3: DISK FOOTPRINT & USAGE (du & disk_usage)
# ================================================================================

def demonstrate_disk_usage():
    print("\n" + "=" * 80)
    print("PART 3: DISK FOOTPRINT & USAGE (du & disk_usage)")
    print("=" * 80)

    gcs_fs = fsspec.filesystem("gcs")
    total_bytes = gcs_fs.du(GCS_PREFIX)
    print(f"Total GCS directory size via du('{GCS_PREFIX}') : {total_bytes:,} bytes")

    # Clean up GCS test prefix
    gcs_fs.rm(GCS_PREFIX, recursive=True)
    print(f"✅ Cleaned up GCS prefix '{GCS_PREFIX}'")


# ================================================================================
# YOUR TURN: EXERCISE 02
# ================================================================================
# Scenario:
# You are writing a data lake auditor. You need to inspect a directory tree 
# and return total bytes used by all `.csv` files matching a wildcard.
#
# INSTRUCTIONS:
# 1. Create a function `calculate_csv_footprint(fs, root_dir: str) -> int`.
# 2. Use `fs.glob()` to find all `.csv` files recursively under `root_dir` (pattern: `f"{root_dir}/**/*.csv"`).
# 3. Calculate and return the sum of sizes for all matched `.csv` files using `fs.size(path)`.
# ================================================================================

# WRITE YOUR FUNCTION HERE:




# --- EXERCISE 02 TEST CODE (Un-comment below to test your implementation) ---
# def run_exercise_tests():
#     print("\n==================================================")
#     print("RUNNING EXERCISE 02 TESTS")
#     print("==================================================")
#     
#     # Test on In-Memory FS
#     mem_fs = fsspec.filesystem("memory")
#     mem_fs.pipe("data/sales/2025.csv", b"a,b,c\n1,2,3\n")
#     mem_fs.pipe("data/sales/2026.csv", b"a,b,c\n4,5,6\n7,8,9\n")
#     mem_fs.pipe("data/notes.txt", b"ignore this file")
#     
#     total_csv_size = calculate_csv_footprint(mem_fs, "data")
#     expected = mem_fs.size("data/sales/2025.csv") + mem_fs.size("data/sales/2026.csv")
#     assert total_csv_size == expected, f"FAILED: Expected {expected}, got {total_csv_size}"
#     print(f"Total CSV Footprint (In-Memory): {total_csv_size} bytes")
#     
#     # Test on GCS FS
#     gcs_fs = fsspec.filesystem("gcs")
#     ex_prefix = f"{BUCKET_NAME}/fsspec_demo_ex2"
#     gcs_fs.pipe(f"{ex_prefix}/sales/2025.csv", b"a,b,c\n1,2,3\n")
#     gcs_fs.pipe(f"{ex_prefix}/sales/2026.csv", b"a,b,c\n4,5,6\n7,8,9\n")
#     
#     gcs_csv_size = calculate_csv_footprint(gcs_fs, ex_prefix)
#     assert gcs_csv_size == expected, f"FAILED: Expected {expected}, got {gcs_csv_size}"
#     print(f"Total CSV Footprint (GCS): {gcs_csv_size} bytes")
#     gcs_fs.rm(ex_prefix, recursive=True)
#     print("🎉 Exercise 02 Passed Successfully!")


if __name__ == "__main__":
    demonstrate_path_discovery()
    demonstrate_metadata_and_hashes()
    demonstrate_disk_usage()
    # run_exercise_tests()
