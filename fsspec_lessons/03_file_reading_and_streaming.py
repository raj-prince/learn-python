#!/usr/bin/env python3
"""
================================================================================
FSSPEC LESSON 03: FILE READING, BLOCK CACHING & RANGE STREAMING
================================================================================

Reading large files over high-latency cloud storage (GCS / S3) requires specialized
methods. `fsspec` provides multiple read strategies: streaming file handles (`open`),
bulk byte reading (`read_bytes`), range slicing (`cat_ranges`), head/tail inspections,
and block-offset reads (`read_block`).

In this lesson, we explore every read method on both `memory://` and `gcs://` (`princer-working-dirs`).

--------------------------------------------------------------------------------
EXPOSED METHODS COVERED IN THIS LESSON:
--------------------------------------------------------------------------------
- Streaming File Opening  : `open()` (Returns `GCSFile` / `AbstractBufferedFile`)
- Bulk Content Reading   : `read_bytes()`, `read_text()`, `cat()`, `cat_file()`
- Partial & Range Reads  : `read_block()`, `cat_ranges()`, `head()`, `tail()`
- File Downloading       : `get()`, `get_file()`, `download()`
"""

import fsspec
import gcsfs

BUCKET_NAME = "princer-working-dirs"
GCS_PREFIX = f"{BUCKET_NAME}/fsspec_demo_lesson3"


# ================================================================================
# PART 1: STREAMING READS WITH open() & BLOCK READS (read_block)
# ================================================================================

def demonstrate_streaming_and_block_reads():
    print("\n" + "=" * 80)
    print("PART 1: STREAMING READS (open & read_block)")
    print("=" * 80)

    content = b"0123456789abcdefghijklmnopqrstuvwxyz" * 100

    # --------------------------------------------------------------------------
    # A. In-Memory Filesystem
    # --------------------------------------------------------------------------
    print("--- [A] IN-MEMORY STREAMING READS ---")
    mem_fs = fsspec.filesystem("memory")
    mem_fs.pipe("mem_bucket/dataset.txt", content)
    with mem_fs.open("mem_bucket/dataset.txt", "rb") as f:
        print(f"  mem_fs.open() read 32 bytes: {f.read(32)}")

    # --------------------------------------------------------------------------
    # B. GCS Cloud Filesystem
    # --------------------------------------------------------------------------
    print("\n--- [B] GCS CLOUD STREAMING READS ---")
    gcs_fs = fsspec.filesystem("gcs")
    gcs_path = f"{GCS_PREFIX}/dataset.txt"
    gcs_fs.pipe(gcs_path, content)

    print(f"1. Reading via gcs_fs.open('{gcs_path}'):")
    with gcs_fs.open(gcs_path, "rb") as f:
        chunk = f.read(64)
        print(f"   Read 64 bytes: {chunk[:20]}...")
        print(f"   Current position (tell()): {f.tell()}")

    print("\n2. Reading fixed offset block via gcs_fs.read_block():")
    block_data = gcs_fs.read_block(gcs_path, offset=10, length=20)
    print(f"   Block (offset=10, len=20): {block_data}")


# ================================================================================
# PART 2: BULK & PARTIAL RANGE READS (cat, cat_ranges, head, tail)
# ================================================================================

def demonstrate_bulk_and_range_reads():
    print("\n" + "=" * 80)
    print("PART 2: BULK & PARTIAL RANGE READS (cat, cat_ranges, head, tail)")
    print("=" * 80)

    gcs_fs = fsspec.filesystem("gcs")
    p1 = f"{GCS_PREFIX}/part1.txt"
    p2 = f"{GCS_PREFIX}/part2.txt"
    gcs_fs.pipe(p1, b"HEADER_1: Hello World!\nLINE2\nLINE3")
    gcs_fs.pipe(p2, b"HEADER_2: Cloud Storage!\nLINEB\nLINEC")

    # 1. cat() / cat_file()
    print("1. Single & Multi-file cat():")
    print("   cat(p1)                :", gcs_fs.cat(p1))
    print("   cat([p1, p2])          :", gcs_fs.cat([p1, p2]))

    # 2. head() and tail()
    print("\n2. Inspection via head() and tail():")
    print("   head(p1, 10 bytes)     :", gcs_fs.head(p1, 10))
    print("   tail(p1, 10 bytes)     :", gcs_fs.tail(p1, 10))

    # 3. cat_ranges() - Efficient HTTP Byte Range Requests
    print("\n3. Byte Range Requests via cat_ranges():")
    ranges = gcs_fs.cat_ranges(paths=[p1, p2], starts=[0, 10], ends=[5, 15])
    print("   cat_ranges() results   :", ranges)


# ================================================================================
# PART 3: DOWNLOADING TO LOCAL DISK (get, get_file, download)
# ================================================================================

def demonstrate_download():
    print("\n" + "=" * 80)
    print("PART 3: DOWNLOADING TO LOCAL DISK (get / get_file)")
    print("=" * 80)

    gcs_fs = fsspec.filesystem("gcs")
    remote_path = f"{GCS_PREFIX}/exports/data.csv"
    gcs_fs.pipe(remote_path, b"id,val\n1,100\n2,200\n")

    local_path = "/tmp/fsspec_demo_download.csv"
    gcs_fs.get(remote_path, local_path)
    print(f"Downloaded GCS path '{remote_path}' to local '{local_path}'")

    with open(local_path, "r", encoding="utf-8") as f:
        print("Local file content preview:")
        print("  ", f.read().strip())


# ================================================================================
# PART 4: LINE-BY-LINE READING & UNDERLYING CALL CHAIN MECHANICS
# ================================================================================

def demonstrate_line_by_line_call_chain():
    print("\n" + "=" * 80)
    print("PART 4: LINE-BY-LINE READING & UNDERLYING CALL CHAIN MECHANICS")
    print("=" * 80)

    gcs_fs = fsspec.filesystem("gcs")
    gcs_path = f"{GCS_PREFIX}/lines_demo.txt"
    gcs_fs.pipe(gcs_path, b"Line 1: Fsspec Streams\nLine 2: Line-by-line reading\nLine 3: Cat file ranges\n")

    print(f"1. Reading '{gcs_path}' line-by-line with `for line in f`:")
    with gcs_fs.open(gcs_path, "r") as f:
        print("   File handle object class:", type(f))         # _io.TextIOWrapper
        print("   Underlying binary stream :", type(f.buffer))  # GCSFile / AbstractBufferedFile
        for line in f:
            print(f"   > {line.strip()}")

    print("\n💡 UNDERLYING CALL CHAIN EXPLANATION:")
    print("   1. `for line in f` calls `TextIOWrapper.readline()`")
    print("   2. `TextIOWrapper` calls `GCSFile.readline()` (inherited from AbstractBufferedFile)")
    print("   3. `AbstractBufferedFile.readline()` calls `self.readuntil(b'\\n')`")
    print("   4. `readuntil()` calls `self.read(blocksize)` which checks `self.cache` (RAM)")
    print("   5. On cache miss, `self._fetch_range(start, end)` is invoked")
    print("   6. `_fetch_range()` calls `self.fs.cat_file(path, start, end)` to fetch byte ranges over HTTP!")

    # Clean up GCS test prefix
    gcs_fs.rm(GCS_PREFIX, recursive=True)
    print(f"✅ Cleaned up GCS prefix '{GCS_PREFIX}'")


# ================================================================================
# YOUR TURN: EXERCISE 03
# ================================================================================
# Scenario:
# You are implementing a log sampler that reads the first 100 bytes (header) and 
# last 100 bytes (footer) from a large cloud file.
#
# INSTRUCTIONS:
# 1. Create a function `sample_header_and_footer(fs, path: str, size: int = 100) -> tuple[bytes, bytes]`.
# 2. Use `fs.head(path, size)` to fetch the header bytes.
# 3. Use `fs.tail(path, size)` to fetch the footer bytes.
# 4. Return the tuple `(header, footer)`.
# ================================================================================

# WRITE YOUR FUNCTION HERE:




# --- EXERCISE 03 TEST CODE (Un-comment below to test your implementation) ---
# def run_exercise_tests():
#     print("\n==================================================")
#     print("RUNNING EXERCISE 03 TESTS")
#     print("==================================================")
#     
#     # Memory FS Test
#     mem_fs = fsspec.filesystem("memory")
#     big_content = b"START_HEADER_" + (b"X" * 500) + b"_END_FOOTER"
#     mem_fs.pipe("mem_bucket/logs/big.log", big_content)
#     head, tail = sample_header_and_footer(mem_fs, "mem_bucket/logs/big.log", size=12)
#     assert head == b"START_HEADER", f"FAILED: Expected b'START_HEADER', got {head}"
#     assert tail.endswith(b"_END_FOOTER"), f"FAILED: Expected end-with b'_END_FOOTER', got {tail}"
#     print("In-Memory Header & Footer sampled successfully!")
#     
#     # GCS FS Test
#     gcs_fs = fsspec.filesystem("gcs")
#     ex_prefix = f"{BUCKET_NAME}/fsspec_demo_ex3"
#     gcs_fs.pipe(f"{ex_prefix}/logs/big.log", big_content)
#     ghead, gtail = sample_header_and_footer(gcs_fs, f"{ex_prefix}/logs/big.log", size=12)
#     assert ghead == b"START_HEADER", f"FAILED: Expected b'START_HEADER', got {ghead}"
#     assert gtail.endswith(b"_END_FOOTER"), f"FAILED: Expected end-with b'_END_FOOTER', got {gtail}"
#     print("GCS Header & Footer sampled successfully!")
#     gcs_fs.rm(ex_prefix, recursive=True)
#     print("🎉 Exercise 03 Passed Successfully!")


if __name__ == "__main__":
    demonstrate_streaming_and_block_reads()
    demonstrate_bulk_and_range_reads()
    demonstrate_download()
    demonstrate_line_by_line_call_chain()
    # run_exercise_tests()

