#!/usr/bin/env python3
"""
================================================================================
LESSON 16: STANDARD JSON VS. ORJSON — HIGH-PERFORMANCE JSON PROCESSING
================================================================================

JSON serialization and deserialization is a core operation in web services, 
microservices, and data pipelines.

Python comes with a built-in `json` module. However, `orjson` is a modern, 
ultra-fast Rust-backed JSON library for Python.

--------------------------------------------------------------------------------
KEY DIFFERENCES SUMMARY
--------------------------------------------------------------------------------
1. Speed: `orjson` is 2x to 10x faster than standard `json` (written in Rust).
2. Return Type:
   - `json.dumps()` returns a `str`.
   - `orjson.dumps()` returns `bytes` (eliminates UTF-8 encoding step for web sockets/HTTP!).
3. Native Datatype Support:
   - `json`: Cannot serialize `datetime`, `UUID`, `dataclass`, `numpy` arrays natively.
   - `orjson`: Natively serializes `datetime`, `UUID`, `dataclass`, `Enum`, `tuple` natively.
4. Memory Efficiency: `orjson` allocates less RAM during large JSON processing.
"""

import json
import orjson
import time
import timeit
from datetime import datetime, timezone
from dataclasses import dataclass
import uuid

# ================================================================================
# 1. SAMPLE DATA GENERATOR FOR BENCHMARKING
# ================================================================================

def generate_large_dataset(count=50_000):
    """Generates a dataset with strings, numbers, booleans, and lists."""
    return [
        {
            "id": i,
            "uuid": "550e8400-e29b-41d4-a716-446655440000",
            "username": f"user_{i}",
            "email": f"user_{i}@example.com",
            "is_active": i % 2 == 0,
            "scores": [i * 1.5, i * 2.5, i * 3.5],
            "metadata": {
                "role": "admin" if i % 10 == 0 else "user",
                "login_count": i * 3,
                "tags": ["python", "asyncio", "json"]
            }
        }
        for i in range(count)
    ]


# ================================================================================
# 2. SPEED BENCHMARK: SERIALIZATION & DESERIALIZATION
# ================================================================================

def benchmark_json_vs_orjson():
    print("==================================================")
    print("1. SPEED BENCHMARK (50,000 NESTED RECORDS)")
    print("==================================================")
    
    data = generate_large_dataset(50_000)

    # --- A) SERIALIZATION (dumps) ---
    # Standard json.dumps
    start = time.perf_counter()
    json_bytes = json.dumps(data).encode('utf-8')
    time_json_dumps = time.perf_counter() - start

    # Orjson dumps
    start = time.perf_counter()
    orjson_bytes = orjson.dumps(data)
    time_orjson_dumps = time.perf_counter() - start

    print(f"📦 Serialization (dumps):")
    print(f"   - Standard json.dumps(): {time_json_dumps:.4f} seconds")
    print(f"   - Fast orjson.dumps()  : {time_orjson_dumps:.4f} seconds")
    print(f"   ⚡ orjson is {time_json_dumps / time_orjson_dumps:.2f}x FASTER at serialization!")

    # --- B) DESERIALIZATION (loads) ---
    json_str = json.dumps(data)
    
    # Standard json.loads
    start = time.perf_counter()
    data_json = json.loads(json_str)
    time_json_loads = time.perf_counter() - start

    # Orjson loads
    start = time.perf_counter()
    data_orjson = orjson.loads(orjson_bytes)
    time_orjson_loads = time.perf_counter() - start

    print(f"\n📂 Deserialization (loads):")
    print(f"   - Standard json.loads(): {time_json_loads:.4f} seconds")
    print(f"   - Fast orjson.loads()  : {time_orjson_loads:.4f} seconds")
    print(f"   ⚡ orjson is {time_json_loads / time_orjson_loads:.2f}x FASTER at deserialization!")


# ================================================================================
# 3. ADVANCED FEATURES & TYPE SUPPORT
# ================================================================================

@dataclass
class UserProfile:
    user_id: int
    name: str
    created_at: datetime
    session_id: uuid.UUID


def demonstrate_type_support():
    print("\n==================================================")
    print("2. NATIVE DATATYPE SUPPORT (DATETIME, UUID, DATACLASS)")
    print("==================================================")
    
    profile = UserProfile(
        user_id=101,
        name="Alice Developer",
        created_at=datetime.now(timezone.utc),
        session_id=uuid.uuid4()
    )

    # --- Standard json fails on custom objects ---
    print("Testing standard `json.dumps` on Dataclass & Datetime:")
    try:
        json.dumps(profile.__dict__)
    except TypeError as e:
        print(f"❌ Standard json error: {e}")

    # --- Orjson handles Datetime, UUID, Dataclass out-of-the-box ---
    print("\nTesting `orjson.dumps` on Dataclass & Datetime:")
    encoded_bytes = orjson.dumps(profile)
    print(f"✅ orjson output (bytes): {encoded_bytes.decode('utf-8')}")


# ================================================================================
# 4. OPTION FLAGS IN ORJSON
# ================================================================================

def demonstrate_option_flags():
    print("\n==================================================")
    print("3. ORJSON OPTION FLAGS")
    print("==================================================")
    
    payload = {
        "timestamp": datetime.now(timezone.utc),
        "b_key": 2,
        "a_key": 1
    }

    # Format output with 2-space indentation, sorted keys, and UTC 'Z' suffix
    formatted = orjson.dumps(
        payload,
        option=orjson.OPT_INDENT_2 | orjson.OPT_SORT_KEYS | orjson.OPT_UTC_Z
    )
    print(formatted.decode('utf-8'))


# ================================================================================
# MAIN ENTRY POINT
# ================================================================================

if __name__ == "__main__":
    benchmark_json_vs_orjson()
    demonstrate_type_support()
    demonstrate_option_flags()
