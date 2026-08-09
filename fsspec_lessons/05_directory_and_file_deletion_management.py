#!/usr/bin/env python3
"""
================================================================================
FSSPEC LESSON 05: DIRECTORIES, DELETIONS & CACHE INVALIDATION
================================================================================

In cloud object storage, directory creation (`mkdir`) and deletion (`rm`) operate
differently than traditional POSIX filesystems because directories are implicit prefix paths.

In this lesson, we explore directory creation, recursive file deletion, and cache
invalidation methods on both `memory://` and `gcs://` (`princer-working-dirs`).

--------------------------------------------------------------------------------
EXPOSED METHODS COVERED IN THIS LESSON:
--------------------------------------------------------------------------------
- Directory Creation : `mkdir()`, `makedir()`, `mkdirs()`, `makedirs()`
- File & Dir Removal : `rm()`, `delete()`, `rm_file()`, `rmdir()`
- Invalidation & Separators : `invalidate_cache()`, `root_marker`, `sep`
"""

import fsspec
import gcsfs

BUCKET_NAME = "princer-working-dirs"
GCS_PREFIX = f"{BUCKET_NAME}/fsspec_demo_lesson5"


# ================================================================================
# PART 1: DIRECTORY CREATION & PATH SEPARATORS
# ================================================================================

def demonstrate_directory_creation():
    print("\n" + "=" * 80)
    print("PART 1: DIRECTORY CREATION & PATH SEPARATORS")
    print("=" * 80)

    # --------------------------------------------------------------------------
    # A. In-Memory Filesystem
    # --------------------------------------------------------------------------
    print("--- [A] IN-MEMORY DIRECTORIES ---")
    mem_fs = fsspec.filesystem("memory")
    mem_fs.mkdir("mem_bucket/new_folder")
    mem_fs.makedirs("mem_bucket/deep/nested/structure", exist_ok=True)
    print("  In-Memory separator:", mem_fs.sep, "| Root marker:", mem_fs.root_marker)

    # --------------------------------------------------------------------------
    # B. GCS Cloud Filesystem
    # --------------------------------------------------------------------------
    print("\n--- [B] GCS CLOUD DIRECTORIES ---")
    gcs_fs = fsspec.filesystem("gcs")
    gcs_fs.mkdir(f"{GCS_PREFIX}/new_folder")
    gcs_fs.makedirs(f"{GCS_PREFIX}/deep/nested/structure", exist_ok=True)
    print("  GCS separator      :", gcs_fs.sep, "| Root marker:", gcs_fs.root_marker)


# ================================================================================
# PART 2: REMOVAL & DELETIONS (rm, rmdir, delete)
# ================================================================================

def demonstrate_deletions():
    print("\n" + "=" * 80)
    print("PART 2: REMOVAL & DELETIONS (rm, rmdir, delete)")
    print("=" * 80)

    gcs_fs = fsspec.filesystem("gcs")
    gcs_fs.pipe(f"{GCS_PREFIX}/temp/file1.log", b"Log 1")
    gcs_fs.pipe(f"{GCS_PREFIX}/temp/file2.log", b"Log 2")
    gcs_fs.pipe(f"{GCS_PREFIX}/keep.txt", b"Keep me")

    print("1. Before deletion on GCS:")
    print("  ", gcs_fs.find(GCS_PREFIX))

    # 1. Single file deletion (rm / rm_file / delete)
    target_file = f"{GCS_PREFIX}/temp/file1.log"
    gcs_fs.rm(target_file)
    print(f"\n2. After rm('{target_file}'):")
    print("  ", gcs_fs.find(GCS_PREFIX))

    # 2. Recursive directory deletion
    target_dir = f"{GCS_PREFIX}/temp"
    gcs_fs.rm(target_dir, recursive=True)
    print(f"\n3. After rm('{target_dir}', recursive=True):")
    print("  ", gcs_fs.find(GCS_PREFIX))


# ================================================================================
# PART 3: CACHE INVALIDATION (invalidate_cache)
# ================================================================================

def demonstrate_cache_invalidation():
    print("\n" + "=" * 80)
    print("PART 3: CACHE INVALIDATION (invalidate_cache)")
    print("=" * 80)

    gcs_fs = fsspec.filesystem("gcs")
    gcs_fs.pipe(f"{GCS_PREFIX}/data.json", b'{"key": "v1"}')

    # Warm up directory listing cache
    _ls_cache = gcs_fs.ls(GCS_PREFIX)

    # When external processes modify the cloud bucket out-of-band, invalidate_cache()
    # forces fsspec to re-query cloud APIs on subsequent calls
    gcs_fs.invalidate_cache(f"{GCS_PREFIX}/data.json")
    gcs_fs.invalidate_cache(GCS_PREFIX)
    print(f"✅ Successfully invalidated cache for '{GCS_PREFIX}'")

    # Clean up GCS test prefix
    gcs_fs.rm(GCS_PREFIX, recursive=True)
    print(f"✅ Cleaned up GCS prefix '{GCS_PREFIX}'")


# ================================================================================
# YOUR TURN: EXERCISE 05
# ================================================================================
# Scenario:
# You are writing a cleanup daemon that wipes temporary scratch folders and invalidates
# filesystem cache afterwards.
#
# INSTRUCTIONS:
# 1. Create a function `purge_scratch_directory(fs, scratch_dir: str)`.
# 2. If `fs.exists(scratch_dir)` is True, call `fs.rm(scratch_dir, recursive=True)` to delete it.
# 3. Call `fs.invalidate_cache(scratch_dir)` to purge cached directory listings.
# ================================================================================

# WRITE YOUR FUNCTION HERE:




# --- EXERCISE 05 TEST CODE (Un-comment below to test your implementation) ---
# def run_exercise_tests():
#     print("\n==================================================")
#     print("RUNNING EXERCISE 05 TESTS")
#     print("==================================================")
#     
#     # Memory FS Test
#     mem_fs = fsspec.filesystem("memory")
#     mem_fs.pipe("scratch/tmp1.txt", b"temp 1")
#     purge_scratch_directory(mem_fs, "scratch")
#     assert not mem_fs.exists("scratch/tmp1.txt")
#     print("In-Memory Purge passed!")
#     
#     # GCS FS Test
#     gcs_fs = fsspec.filesystem("gcs")
#     ex_prefix = f"{BUCKET_NAME}/fsspec_demo_ex5"
#     gcs_fs.pipe(f"{ex_prefix}/tmp1.txt", b"temp 1")
#     purge_scratch_directory(gcs_fs, ex_prefix)
#     assert not gcs_fs.exists(f"{ex_prefix}/tmp1.txt")
#     print("GCS Purge passed!")
#     print("🎉 Exercise 05 Passed Successfully!")


if __name__ == "__main__":
    demonstrate_directory_creation()
    demonstrate_deletions()
    demonstrate_cache_invalidation()
    # run_exercise_tests()
