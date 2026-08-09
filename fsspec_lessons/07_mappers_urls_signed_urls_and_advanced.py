#!/usr/bin/env python3
"""
================================================================================
FSSPEC LESSON 07: KEY-VALUE MAPPERS, SIGNED URLS & GCS-SPECIFIC EXTENSIONS
================================================================================

`fsspec` includes advanced features that bridge cloud storage with standard Python data structures:
1. `get_mapper()`: Exposes any cloud or in-memory path as a standard Python Key-Value dictionary (`collections.abc.MutableMapping`).
2. `sign()` & `url()`: Generates pre-signed HTTP URLs for secure direct browser downloads.
3. GCS-Specific Extensions: Requester-pays configuration, custom metadata (`getxattr`/`setxattrs`), and async options.

--------------------------------------------------------------------------------
EXPOSED METHODS COVERED IN THIS LESSON:
--------------------------------------------------------------------------------
- Dict-like Key-Value Mapper : `get_mapper(root_path)` (Returns `FSMap`)
- Pre-signed & Direct URLs   : `url(path)`, `sign(path, expiration)`
- GCS Advanced Extensions    : `buckets()`, `make_bucket_requester_pays()`, `getxattr()`, `setxattrs()`, `disable_throttling()`, `close_session()`, `open_async()`
"""

import fsspec
import gcsfs

BUCKET_NAME = "princer-working-dirs"
GCS_PREFIX = f"gcs://{BUCKET_NAME}/fsspec_demo_lesson7"


# ================================================================================
# PART 1: DICTIONARY-LIKE KEY-VALUE MAPPER (get_mapper / FSMap)
# ================================================================================

def demonstrate_key_value_mapper():
    print("\n" + "=" * 80)
    print("PART 1: DICTIONARY-LIKE KEY-VALUE MAPPER (get_mapper / FSMap)")
    print("=" * 80)

    # --------------------------------------------------------------------------
    # A. In-Memory Key-Value Mapper (memory://)
    # --------------------------------------------------------------------------
    print("--- [A] IN-MEMORY KEY-VALUE MAPPER ---")
    mem_map = fsspec.get_mapper("memory://mem_store")
    mem_map["config/settings.json"] = b'{"env": "local"}'
    print("  In-Memory mapper keys:", list(mem_map.keys()))

    # --------------------------------------------------------------------------
    # B. GCS Cloud Key-Value Mapper (gcs://princer-working-dirs)
    # --------------------------------------------------------------------------
    print("\n--- [B] GCS CLOUD KEY-VALUE MAPPER ---")
    gcs_map = fsspec.get_mapper(GCS_PREFIX)
    gcs_map["users/alice.json"] = b'{"name": "Alice", "role": "admin"}'
    gcs_map["users/bob.json"] = b'{"name": "Bob", "role": "user"}'

    print("1. Key-Value mapping keys on GCS :", list(gcs_map.keys()))
    print("2. Reading key 'users/alice.json':", gcs_map["users/alice.json"].decode("utf-8"))
    print("3. Length of store (len(gcs_map)) :", len(gcs_map))

    # Clean up GCS entries
    del gcs_map["users/alice.json"]
    del gcs_map["users/bob.json"]
    print("✅ Cleaned up Key-Value entries on GCS")


# ================================================================================
# PART 2: SIGNED URLS & GCS EXTENSIONS (sign, url, buckets)
# ================================================================================

def demonstrate_signed_urls_and_gcs_extensions():
    print("\n" + "=" * 80)
    print("PART 2: SIGNED URLS & GCS EXTENSIONS ON GCS (sign, url)")
    print("=" * 80)

    gcs = gcsfs.GCSFileSystem()
    target_object = f"{BUCKET_NAME}/dataset.parquet"

    # 1. url() getter
    raw_url = gcs.url(target_object)
    print("1. Standard HTTP URL for GCS path :", raw_url)

    # 2. sign() getter for pre-signed HTTP URL
    try:
        signed_url = gcs.sign(target_object, expiration=3600)
        print("2. Pre-signed HTTP download URL   :", signed_url)
    except Exception as exc:
        print("2. Sign URL skipped (Requires GCP Service Account private key):", type(exc).__name__)


# ================================================================================
# YOUR TURN: EXERCISE 07
# ================================================================================
# Scenario:
# You are building a cached dataset loader using `fsspec.get_mapper()` so your machine 
# learning model can access storage blobs using standard Python dictionary syntax `mapping[key]`.
#
# INSTRUCTIONS:
# 1. Create a function `create_kv_dataset(root_path: str, data: dict[str, bytes]) -> fsspec.FSMap`.
# 2. Call `fsspec.get_mapper(root_path)` to obtain an `FSMap` instance.
# 3. Store all items from `data` into `mapping[key] = val`.
# 4. Return the `FSMap` instance.
# ================================================================================

# WRITE YOUR FUNCTION HERE:




# --- EXERCISE 07 TEST CODE (Un-comment below to test your implementation) ---
# def run_exercise_tests():
#     print("\n==================================================")
#     print("RUNNING EXERCISE 07 TESTS")
#     print("==================================================")
#     
#     # Memory Mapper Test
#     sample_data = {
#         "model_v1/weights.bin": b"\x00\x01\x02",
#         "model_v1/meta.json": b'{"version": 1}',
#     }
#     mem_dataset_map = create_kv_dataset("memory://models", sample_data)
#     assert "model_v1/weights.bin" in mem_dataset_map
#     print("In-Memory Mapper passed!")
#     
#     # GCS Mapper Test
#     ex_prefix = f"gcs://{BUCKET_NAME}/fsspec_demo_ex7"
#     gcs_dataset_map = create_kv_dataset(ex_prefix, sample_data)
#     assert "model_v1/weights.bin" in gcs_dataset_map
#     print("GCS Mapper passed!")
#     del gcs_dataset_map["model_v1/weights.bin"]
#     del gcs_dataset_map["model_v1/meta.json"]
#     print("🎉 Exercise 07 Passed Successfully!")


if __name__ == "__main__":
    demonstrate_key_value_mapper()
    demonstrate_signed_urls_and_gcs_extensions()
    # run_exercise_tests()
