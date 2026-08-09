#!/usr/bin/env python3
"""
================================================================================
FSSPEC LESSON 06: TRANSACTIONS & BATCH OPERATIONS
================================================================================

When writing multiple files or performing bulk file manipulations on cloud storage,
issuing individual network calls per file is slow and exposes incomplete writes if an error occurs.

`fsspec` provides **Transactions** (`transaction`, `start_transaction()`, `end_transaction()`)
that buffer file writes locally or defer network API calls until the transaction block exits successfully
on both `memory://` and `gcs://` (`princer-working-dirs`).

--------------------------------------------------------------------------------
EXPOSED METHODS COVERED IN THIS LESSON:
--------------------------------------------------------------------------------
- Transaction Context  : `transaction` (Context manager `with fs.transaction:`)
- Transaction Controls : `start_transaction()`, `end_transaction()`, `transaction_type`
- Batch Manipulation  : Deferred write buffering and atomic commit semantics
"""

import fsspec
import gcsfs

BUCKET_NAME = "princer-working-dirs"
GCS_PREFIX = f"{BUCKET_NAME}/fsspec_demo_lesson6"


# ================================================================================
# PART 1: FSSPEC TRANSACTIONS (with fs.transaction)
# ================================================================================

def demonstrate_transactions():
    print("\n" + "=" * 80)
    print("PART 1: FSSPEC TRANSACTIONS (with fs.transaction)")
    print("=" * 80)

    # --------------------------------------------------------------------------
    # A. In-Memory Filesystem
    # --------------------------------------------------------------------------
    print("--- [A] IN-MEMORY TRANSACTIONS ---")
    mem_fs = fsspec.filesystem("memory")
    with mem_fs.transaction:
        mem_fs.pipe("mem_bucket/tx_data/file1.csv", b"id,val\n1,A\n")
        mem_fs.pipe("mem_bucket/tx_data/file2.csv", b"id,val\n2,B\n")
    print("  In-Memory files committed:", mem_fs.find("mem_bucket/tx_data"))

    # --------------------------------------------------------------------------
    # B. GCS Cloud Filesystem
    # --------------------------------------------------------------------------
    print("\n--- [B] GCS CLOUD TRANSACTIONS ---")
    gcs_fs = fsspec.filesystem("gcs")
    with gcs_fs.transaction:
        gcs_fs.pipe(f"{GCS_PREFIX}/tx_data/file1.csv", b"id,val\n1,A\n")
        gcs_fs.pipe(f"{GCS_PREFIX}/tx_data/file2.csv", b"id,val\n2,B\n")
    print("  GCS files committed      :", gcs_fs.find(f"{GCS_PREFIX}/tx_data"))


# ================================================================================
# PART 2: MANUAL TRANSACTION CONTROLS (start_transaction / end_transaction)
# ================================================================================

def demonstrate_manual_transactions():
    print("\n" + "=" * 80)
    print("PART 2: MANUAL TRANSACTION CONTROLS (start_transaction / end_transaction)")
    print("=" * 80)

    gcs_fs = fsspec.filesystem("gcs")

    # Start transaction manually
    gcs_fs.start_transaction()
    print("   Started manual transaction (transaction_type):", type(gcs_fs.transaction))

    gcs_fs.pipe(f"{GCS_PREFIX}/manual_tx/a.txt", b"Alpha")
    gcs_fs.pipe(f"{GCS_PREFIX}/manual_tx/b.txt", b"Beta")

    # Commit/End transaction
    gcs_fs.end_transaction()
    print("   Ended manual transaction. Created files:", gcs_fs.find(f"{GCS_PREFIX}/manual_tx"))

    # Clean up GCS test prefix
    gcs_fs.rm(GCS_PREFIX, recursive=True)
    print(f"✅ Cleaned up GCS prefix '{GCS_PREFIX}'")


# ================================================================================
# YOUR TURN: EXERCISE 06
# ================================================================================
# Scenario:
# You are implementing an atomic multi-file ETL exporter. All exported partition files
# must be written together inside a transaction block.
#
# INSTRUCTIONS:
# 1. Create a function `batch_export_partitions(fs, partition_data: dict[str, bytes])`.
# 2. Open a transaction using `with fs.transaction:`.
# 3. Inside the transaction block, iterate through `partition_data.items()` and write each file using `fs.pipe(path, content)`.
# ================================================================================

# WRITE YOUR FUNCTION HERE:




# --- EXERCISE 06 TEST CODE (Un-comment below to test your implementation) ---
# def run_exercise_tests():
#     print("\n==================================================")
#     print("RUNNING EXERCISE 06 TESTS")
#     print("==================================================")
#     
#     # Memory FS Test
#     mem_fs = fsspec.filesystem("memory")
#     payloads = {"mem_bucket/part1.json": b'{"p": 1}'}
#     batch_export_partitions(mem_fs, payloads)
#     assert mem_fs.exists("mem_bucket/part1.json")
#     print("In-Memory Transaction passed!")
#     
#     # GCS FS Test
#     gcs_fs = fsspec.filesystem("gcs")
#     ex_prefix = f"{BUCKET_NAME}/fsspec_demo_ex6"
#     gcs_payloads = {f"{ex_prefix}/part1.json": b'{"p": 1}'}
#     batch_export_partitions(gcs_fs, gcs_payloads)
#     assert gcs_fs.exists(f"{ex_prefix}/part1.json")
#     print("GCS Transaction passed!")
#     gcs_fs.rm(ex_prefix, recursive=True)
#     print("🎉 Exercise 06 Passed Successfully!")


if __name__ == "__main__":
    demonstrate_transactions()
    demonstrate_manual_transactions()
    # run_exercise_tests()
