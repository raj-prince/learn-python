#!/usr/bin/env python3
"""
================================================================================
LESSON 20: MMAP — MEMORY-MAPPED FILES & ANONYMOUS SHARED MEMORY
================================================================================

The `mmap` standard library module allows you to map file contents directly into 
your process's virtual memory address space (`mmap(2)` system call on Linux/Unix, 
`CreateFileMapping` on Windows).

Instead of copying file data from OS kernel disk buffers into Python heap memory 
(as `file.read()` does), `mmap` lets Python access disk files directly through 
CPU virtual memory page tables.

--------------------------------------------------------------------------------
KEY ADVANTAGES & MECHANICS OF MMAP
--------------------------------------------------------------------------------
1. Zero-Copy Performance:
   - Reads occur directly from OS disk cache page tables (Demand Paging).
   - Eliminates redundant memory allocations and heap copying.

2. Access Files Larger Than RAM:
   - You can map a 100 GB file on a machine with 8 GB RAM.
   - The OS kernel automatically pages memory blocks in/out as needed (LRU).

3. In-Place File Mutation:
   - Updating bytes in an `mmap` slice updates the actual underlying file on disk 
     WITHOUT rewriting the entire file (`ACCESS_WRITE`).

4. Inter-Process Communication (IPC):
   - Anonymous memory (`fileno = -1`) allows multiple child processes to share 
     a raw memory buffer without socket/pipe serialization overhead.

5. Access Modes:
   - `mmap.ACCESS_READ` : Read-only access.
   - `mmap.ACCESS_WRITE`: Read-write (modifications are flushed to disk).
   - `mmap.ACCESS_COPY` : Copy-On-Write (modifications remain in-memory only).
"""

import os
import time
import mmap
import re
from pathlib import Path
from multiprocessing import Process, Array


# ================================================================================
# PART 1: BASIC FILE MEMORY MAPPING & ZERO-COPY SEARCHING
# ================================================================================

def demonstrate_basic_file_mmap(sample_file: Path):
    print("\n" + "=" * 80)
    print("PART 1: BASIC FILE MEMORY MAPPING & FAST SEARCHING")
    print("=" * 80)

    # 1. Open standard file descriptor
    with open(sample_file, "rb") as f:
        # fileno() gives the raw OS file descriptor
        # length=0 maps the ENTIRE file
        with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_READ) as mm:
            print(f"📁 Mapped File Size : {len(mm):,} bytes")
            print(f"📖 Slice [0:40]     : {mm[:40]}")

            # Finding byte offsets (Fast C-level search inside memory pages)
            target = b"KEY_INDEX_500"
            offset = mm.find(target)
            print(f"🔍 Found '{target.decode()}' at byte offset: {offset}")

            if offset != -1:
                print(f"   Context Slice    : {mm[offset:offset + 30]}")


# ================================================================================
# PART 2: IN-PLACE DISK FILE MUTATION (ACCESS_WRITE)
# ================================================================================

def demonstrate_inplace_file_mutation(sample_file: Path):
    print("\n" + "=" * 80)
    print("PART 2: IN-PLACE FILE MUTATION (WITHOUT REWRITING FILE)")
    print("=" * 80)

    # Open file in read-write binary mode ('r+b')
    with open(sample_file, "r+b") as f:
        with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_WRITE) as mm:
            target = b"HEADER_TOKEN"
            offset = mm.find(target)
            
            if offset != -1:
                print(f"Original Data at offset {offset}: {mm[offset:offset + 12]}")
                
                # Direct in-place memory update!
                new_token = b"UPDATED_TOKN"
                mm[offset:offset + len(new_token)] = new_token
                
                # Flush changes from OS virtual memory back to physical disk storage
                mm.flush()
                print(f"Updated  Data at offset {offset}: {mm[offset:offset + 12]}")


# ================================================================================
# PART 3: BENCHMARK: mmap vs Standard file.read()
# ================================================================================

def demonstrate_mmap_performance_benchmark(large_file: Path):
    print("\n" + "=" * 80)
    print("PART 3: BENCHMARK: mmap vs Standard file.read()")
    print("=" * 80)

    target_pattern = re.compile(b"TARGET_PATTERN_9999")

    # 1. Standard file.read() (Allocates Python bytes object, copies disk cache)
    start_t = time.perf_counter()
    with open(large_file, "rb") as f:
        content = f.read()  # Copies full file into Python heap memory
        match1 = target_pattern.search(content)
    t_read = time.perf_counter() - start_t

    # 2. mmap (Zero-copy demand-paged memory mapping)
    start_t = time.perf_counter()
    with open(large_file, "rb") as f:
        with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_READ) as mm:
            match2 = target_pattern.search(mm)  # Regex searches directly on mmap buffer!
    t_mmap = time.perf_counter() - start_t

    print(f"📦 File Size: {large_file.stat().st_size / 1e6:.1f} MB")
    print(f"⏱️  Standard file.read() : {t_read * 1000:.2f} ms  (Heap memory allocation + copy)")
    print(f"⏱️  mmap Zero-Copy       : {t_mmap * 1000:.2f} ms  (OS page table mapping)")
    
    speedup = t_read / max(t_mmap, 0.00001)
    print(f"🚀 Speedup Factor       : {speedup:.1f}x Faster!")


# ================================================================================
# PART 4: ANONYMOUS SHARED MEMORY FOR MULTI-PROCESSING (fileno = -1)
# ================================================================================

def worker_process(mm: mmap.mmap, worker_id: int):
    """Worker process writing directly into shared memory offset."""
    offset = worker_id * 30
    msg = f"Worker-{worker_id} output".encode("utf-8").ljust(30, b" ")
    mm[offset:offset + 30] = msg


def demonstrate_anonymous_shared_memory():
    print("\n" + "=" * 80)
    print("PART 4: ANONYMOUS SHARED MEMORY FOR MULTI-PROCESSING")
    print("=" * 80)

    buffer_size = 120  # 4 workers x 30 bytes
    
    # Create anonymous mmap (not backed by any file on disk, fileno=-1)
    # Serves as high-speed inter-process shared RAM memory!
    shm = mmap.mmap(-1, buffer_size, flags=mmap.MAP_SHARED if hasattr(mmap, 'MAP_SHARED') else 0)

    processes = []
    for i in range(4):
        p = Process(target=worker_process, args=(shm, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Shared Memory Output across 4 Independent Processes:")
    print(f"  {shm[:].decode('utf-8')}")
    shm.close()


# ================================================================================
# SETUP HELPER & MAIN EXECUTION
# ================================================================================

def create_demo_files(tmp_dir: Path):
    tmp_dir.mkdir(parents=True, exist_ok=True)
    sample_path = tmp_dir / "sample.bin"
    large_path = tmp_dir / "large_data.bin"

    # Create small sample file
    sample_content = b"HEADER_TOKEN --- Log Entry 1 --- KEY_INDEX_500: SUCCESS --- END"
    sample_path.write_bytes(sample_content)

    # Create 30MB benchmark file
    chunk = b"X" * 1000 + b"TARGET_PATTERN_9999" + b"Y" * 1000
    with open(large_path, "wb") as f:
        for _ in range(15_000):
            f.write(chunk)

    return sample_path, large_path


if __name__ == "__main__":
    tmp_directory = Path(__file__).parent / "tmp_mmap_demo"
    try:
        sample_f, large_f = create_demo_files(tmp_directory)
        demonstrate_basic_file_mmap(sample_f)
        demonstrate_inplace_file_mutation(sample_f)
        demonstrate_mmap_performance_benchmark(large_f)
        demonstrate_anonymous_shared_memory()
    finally:
        # Cleanup temp files
        if tmp_directory.exists():
            import shutil
            shutil.rmtree(tmp_directory)
