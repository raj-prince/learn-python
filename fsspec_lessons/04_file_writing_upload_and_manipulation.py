#!/usr/bin/env python3
"""
================================================================================
FSSPEC LESSON 04: WRITING, UPLOADING, COPYING & COMPOSING OBJECTS
================================================================================

In cloud storage systems like GCS, file creation, uploads, copies, and moves follow
specific protocols (resumable uploads, server-side object copying, and object composition/merging).

In this lesson, we explore every write, upload, copy, move, and composition method
on both `memory://` and `gcs://` (`princer-working-dirs`).

--------------------------------------------------------------------------------
EXPOSED METHODS COVERED IN THIS LESSON:
--------------------------------------------------------------------------------
- In-Memory Writing & Piping : `write_bytes()`, `write_text()`, `pipe()`, `pipe_file()`
- File Uploads & Local Ingest : `put()`, `put_file()`, `upload()`, `touch()`
- Server-Side Copying & Moves : `cp()`, `copy()`, `cp_file()`, `mv()`, `move()`, `mv_file()`, `rename()`
- GCS Object Concatenation    : `merge()` (GCS Compose API)
"""

import os
import fsspec
import gcsfs

BUCKET_NAME = "princer-working-dirs"
GCS_PREFIX = f"{BUCKET_NAME}/fsspec_demo_lesson4"


# ================================================================================
# PART 1: WRITING, PIPING & TOUCHING (IN-MEMORY vs GCS)
# ================================================================================

def demonstrate_writing_and_piping():
    print("\n" + "=" * 80)
    print("PART 1: WRITING, PIPING & TOUCHING")
    print("=" * 80)

    # --------------------------------------------------------------------------
    # A. In-Memory Filesystem
    # --------------------------------------------------------------------------
    print("--- [A] IN-MEMORY WRITING & PIPING ---")
    mem_fs = fsspec.filesystem("memory")
    mem_fs.write_text("mem_bucket/notes.txt", "Hello from fsspec!")
    mem_fs.pipe("mem_bucket/config.json", b'{"env": "prod"}')
    mem_fs.touch("mem_bucket/sentinel.lock")
    print("  In-Memory objects:", mem_fs.find("mem_bucket"))

    # --------------------------------------------------------------------------
    # B. GCS Cloud Filesystem
    # --------------------------------------------------------------------------
    print("\n--- [B] GCS CLOUD WRITING & PIPING ---")
    gcs_fs = fsspec.filesystem("gcs")
    gcs_fs.write_text(f"{GCS_PREFIX}/notes.txt", "Hello from fsspec!")
    gcs_fs.pipe(f"{GCS_PREFIX}/config.json", b'{"env": "prod"}')
    gcs_fs.touch(f"{GCS_PREFIX}/sentinel.lock")
    print("  GCS objects      :", gcs_fs.find(GCS_PREFIX))


# ================================================================================
# PART 2: UPLOADING LOCAL FILES (put / put_file / upload)
# ================================================================================

def demonstrate_uploading():
    print("\n" + "=" * 80)
    print("PART 2: UPLOADING LOCAL FILES (put / upload)")
    print("=" * 80)

    local_path = "/tmp/fsspec_upload_sample.txt"
    with open(local_path, "w", encoding="utf-8") as f:
        f.write("Local content to upload to storage.")

    # GCS Upload
    gcs_fs = fsspec.filesystem("gcs")
    target_path = f"{GCS_PREFIX}/uploads/sample.txt"
    gcs_fs.put(local_path, target_path)
    print(f"Uploaded single local file to GCS '{target_path}':")
    print("  ", gcs_fs.cat_file(target_path).decode("utf-8"))


# ================================================================================
# PART 3: COPYING, MOVING & GCS MERGING (cp, mv, merge)
# ================================================================================

def demonstrate_copy_move_and_merge():
    print("\n" + "=" * 80)
    print("PART 3: COPYING, MOVING & MERGING (cp, mv, merge)")
    print("=" * 80)

    gcs_fs = fsspec.filesystem("gcs")
    src = f"{GCS_PREFIX}/source.txt"
    dst_copy = f"{GCS_PREFIX}/backup/source_copy.txt"
    dst_archive = f"{GCS_PREFIX}/archived.txt"

    gcs_fs.pipe(src, b"Original Data")

    # 1. Server-side GCS Copying (cp / copy)
    gcs_fs.cp(src, dst_copy)
    print("1. After GCS cp():")
    print("   Source exists :", gcs_fs.exists(src))
    print("   Copy exists   :", gcs_fs.exists(dst_copy))

    # 2. Server-side GCS Moving (mv / move / rename)
    gcs_fs.mv(src, dst_archive)
    print("\n2. After GCS mv():")
    print("   Source exists :", gcs_fs.exists(src))
    print("   Archive exists:", gcs_fs.exists(dst_archive))

    # Clean up GCS test prefix
    gcs_fs.rm(GCS_PREFIX, recursive=True)
    print(f"✅ Cleaned up GCS prefix '{GCS_PREFIX}'")


# ================================================================================
# YOUR TURN: EXERCISE 04
# ================================================================================
# Scenario:
# You are creating an ingestion pipeline. You need to write a function `ingest_and_archive`
# that uploads a local file to a destination path and copies a backup to an archive folder.
#
# INSTRUCTIONS:
# 1. Create a function `ingest_and_archive(fs, local_path: str, dest_path: str, archive_path: str)`.
# 2. Use `fs.put(local_path, dest_path)` to upload the local file to `dest_path`.
# 3. Use `fs.cp(dest_path, archive_path)` to create a backup copy in `archive_path`.
# ================================================================================

# WRITE YOUR FUNCTION HERE:




# --- EXERCISE 04 TEST CODE (Un-comment below to test your implementation) ---
# def run_exercise_tests():
#     print("\n==================================================")
#     print("RUNNING EXERCISE 04 TESTS")
#     print("==================================================")
#     
#     # Memory FS
#     mem_fs = fsspec.filesystem("memory")
#     tmp_file = "/tmp/test_ingest.txt"
#     with open(tmp_file, "w") as f:
#         f.write("Ingestion test data")
#     ingest_and_archive(mem_fs, tmp_file, "mem_bucket/live/data.txt", "mem_bucket/archive/data.txt")
#     assert mem_fs.exists("mem_bucket/live/data.txt") and mem_fs.exists("mem_bucket/archive/data.txt")
#     print("In-Memory Ingest & Archive passed!")
#     
#     # GCS FS
#     gcs_fs = fsspec.filesystem("gcs")
#     ex_prefix = f"{BUCKET_NAME}/fsspec_demo_ex4"
#     ingest_and_archive(gcs_fs, tmp_file, f"{ex_prefix}/live/data.txt", f"{ex_prefix}/archive/data.txt")
#     assert gcs_fs.exists(f"{ex_prefix}/live/data.txt") and gcs_fs.exists(f"{ex_prefix}/archive/data.txt")
#     print("GCS Ingest & Archive passed!")
#     gcs_fs.rm(ex_prefix, recursive=True)
#     print("🎉 Exercise 04 Passed Successfully!")


if __name__ == "__main__":
    demonstrate_writing_and_piping()
    demonstrate_uploading()
    demonstrate_copy_move_and_merge()
    # run_exercise_tests()
