#!/usr/bin/env python3
"""
================================================================================
FSSPEC LESSON 01: CORE ARCHITECTURE & INSTANTIATION (GCS & ABSTRACTFILESYSTEM)
================================================================================

`fsspec` (Filesystem Spec) provides a unified Pythonic interface to local, remote,
and cloud storage systems (GCS, S3, Azure Blob, SFTP, Zip, Memory, HDFS).

In this lesson, we cover instantiation, protocol normalization, instance caching,
serialization (`to_dict` / `to_json`), and GCS-specific connection options.

--------------------------------------------------------------------------------
EXPOSED METHODS COVERED IN THIS LESSON:
--------------------------------------------------------------------------------
- `fsspec.filesystem('gcs', **kwargs)` / `gcsfs.GCSFileSystem(**kwargs)`
- `protocol` / `unstrip_protocol(path)`
- `cachable` / `clear_instance_cache()`
- `from_dict(d)` / `to_dict()`
- `from_json(json_str)` / `to_json()`
- `split_path(path)`
"""

import json
import fsspec
import gcsfs
from fsspec.spec import AbstractFileSystem


# ================================================================================
# PART 1: INSTANTIATION & PROTOCOL RESOLUTION
# ================================================================================

def demonstrate_instantiation_and_protocols():
    print("\n" + "=" * 80)
    print("PART 1: INSTANTIATION & PROTOCOL RESOLUTION")
    print("=" * 80)

    # Method 1: Using generic fsspec factory function (Recommended for multi-backend code)
    fs_gcs_factory = fsspec.filesystem("gcs", token="anon")
    print("Factory GCS instance     :", type(fs_gcs_factory), f"| Protocol: {fs_gcs_factory.protocol}")

    # Method 2: Direct GCSFileSystem instantiation
    fs_gcs_direct = gcsfs.GCSFileSystem(token="anon")
    print("Direct GCS instance      :", type(fs_gcs_direct), f"| Protocol: {fs_gcs_direct.protocol}")

    # Protocol handling
    print(f"Protocol name            : {fs_gcs_factory.protocol}")
    full_url = fs_gcs_factory.unstrip_protocol("my-bucket/data/file.csv")
    print(f"Unstripped protocol URL  : {full_url}")

    # Path splitting helper (called on an instance or via static _split_path)
    bucket, key, generation = fs_gcs_direct.split_path("gcs://princer-working-dirs/subfolder/file.txt")
    print(f"split_path() result      : Bucket='{bucket}', Key='{key}'")



# ================================================================================
# PART 2: INSTANCE CACHING & CLEARING CACHE
# ================================================================================

def demonstrate_instance_caching():
    print("\n" + "=" * 80)
    print("PART 2: INSTANCE CACHING (clear_instance_cache)")
    print("=" * 80)

    fs1 = fsspec.filesystem("gcs", token="anon")
    fs2 = fsspec.filesystem("gcs", token="anon")
    print(f"Instances cached & reused : {fs1 is fs2} (Same memory address!)")

    # Clear instance cache
    AbstractFileSystem.clear_instance_cache()
    fs3 = fsspec.filesystem("gcs", token="anon")
    print(f"New instance after clear  : {fs1 is not fs3} (New instance created!)")


# ================================================================================
# PART 3: SERIALIZATION & DESERIALIZATION (to_dict / to_json / from_dict)
# ================================================================================

def demonstrate_serialization():
    print("\n" + "=" * 80)
    print("PART 3: SERIALIZATION (to_dict / to_json / from_dict / from_json)")
    print("=" * 80)

    fs = gcsfs.GCSFileSystem(token="anon", project="my-gcp-project")

    # Serialize to dict and JSON
    fs_dict = fs.to_dict()
    fs_json = fs.to_json()

    print("Serialized Dict Keys     :", list(fs_dict.keys()))
    print("Serialized JSON snippet  :", fs_json[:120] + "...")

    # Reconstruct instance from dict / json
    reconstructed_fs = AbstractFileSystem.from_dict(fs_dict)
    print("Reconstructed instance   :", type(reconstructed_fs), f"| Project: {reconstructed_fs.project}")



# ================================================================================
# YOUR TURN: EXERCISE 01
# ================================================================================
# Scenario:
# You are building a configurable Cloud Storage loader that serializes GCS 
# filesystem configurations to JSON and reconstructs them in worker tasks.
#
# INSTRUCTIONS:
# 1. Create a function `serialize_and_reconstruct_gcs(project: str, token: str) -> GCSFileSystem`.
# 2. Instantiate `gcsfs.GCSFileSystem(project=project, token=token)`.
# 3. Serialize it to a JSON string using `.to_json()`.
# 4. Reconstruct and return the filesystem object from the JSON string using `AbstractFileSystem.from_json()`.
# ================================================================================

# WRITE YOUR FUNCTION HERE:




# --- EXERCISE 01 TEST CODE (Un-comment below to test your implementation) ---
# def run_exercise_tests():
#     print("\n==================================================")
#     print("RUNNING EXERCISE 01 TESTS")
#     print("==================================================")
#     
#     reconstructed = serialize_and_reconstruct_gcs(project="demo-proj", token="anon")
#     assert isinstance(reconstructed, gcsfs.GCSFileSystem), "FAILED: Did not return a GCSFileSystem"
#     assert reconstructed.token == "anon", "FAILED: Token was not preserved"
#     print("Reconstructed GCS Project:", reconstructed.project)
#     print("🎉 Exercise 01 Passed Successfully!")


if __name__ == "__main__":
    demonstrate_instantiation_and_protocols()
    demonstrate_instance_caching()
    demonstrate_serialization()
    # run_exercise_tests()
