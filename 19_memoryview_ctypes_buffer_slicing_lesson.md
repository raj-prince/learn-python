# Lesson 19: `memoryview`, `ctypes.memmove`, and Zero-Copy Buffer Slicing in CPython

When processing binary streams, large datasets (gigabytes of image/video frames, network packets, machine learning tensors), or designing high-performance concurrent pipelines, **how memory is sliced and copied determines whether Python runs at C speed or grinds to a halt under Garbage Collection (GC) and Memory Bandwidth pressure**.

This lesson breaks down the CPython memory model, the C Buffer Protocol, `memoryview`, `ctypes.memmove`, and concurrent memory patterns.

---

## 1. The Core Problem: Why Standard Slicing Hurts Performance

In standard Python, slicing a sequence like `bytes`, `bytearray`, or `list` creates a **new object** and copies all elements over:

```python
data = bytes(50_000_000)   # 50 MB in memory
chunk = data[1000:10_001_000] # 10 MB slice
```

```mermaid
flowchart TD
    subgraph Standard Slicing (O(N) Copy)
        A["Source \`bytes\` (50 MB)<br>Heap Block 0x1000"] -->|Allocates NEW 10 MB Heap Block 0x5000| B["New \`bytes\` Object (10 MB)"]
        A -->|Copies 10,000,000 bytes byte-by-byte| B
    end
```

### Why this is expensive:
1. **$O(N)$ Time & Space**: Slicing 10 MB takes time proportional to 10 MB.
2. **Heap Allocation & GC Pressure**: Every slice triggers `pymalloc` / OS `malloc`, increasing GC tracking and memory fragmentation.
3. **CPU Cache Thrashing**: Allocating and copying megabytes forces CPU caches (L1/L2/L3) to evict hot working data.
4. **GIL Contention**: CPython holds the Global Interpreter Lock while allocating and copying objects.

---

## 2. The Solution: CPython Buffer Protocol & `memoryview`

### What is the Buffer Protocol?
The **Buffer Protocol** (PEP 3118) is a C-level interface in CPython (`Py_buffer`). It allows objects that hold contiguous blocks of memory (such as `bytes`, `bytearray`, `array.array`, and NumPy `ndarray`) to expose their raw memory address, shape, and strides directly to other objects **without copying data**.

```c
/* CPython Py_buffer struct definition */
typedef struct bufferinfo {
    void *buf;              /* Raw pointer to the start of memory */
    PyObject *obj;          /* Source object being viewed (ref-counted) */
    Py_ssize_t len;         /* Total length in bytes */
    Py_ssize_t itemsize;    /* Size of each element in bytes */
    int readonly;           /* 1 for bytes, 0 for bytearray */
    int ndim;               /* Number of dimensions (1 for flat buffers) */
    char *format;           /* Struct-style type string (e.g. 'B', 'i', 'd') */
    Py_ssize_t *shape;      /* Shape array */
    Py_ssize_t *strides;    /* Stride array */
} Py_buffer;
```

### `memoryview`: The $O(1)$ Zero-Copy Window
`memoryview` is Python's built-in wrapper around `Py_buffer`. When you slice a `memoryview`, CPython does **not** allocate memory for the underlying data:

```mermaid
flowchart TD
    subgraph Zero-Copy Memoryview Slicing (O(1))
        Buf["Single Continuous 50 MB Buffer in Memory<br>(0x1000 ... 0x3FFF)"]
        V1["\`memoryview(buf)\`<br>Points to 0x1000, len=50MB"] -.-> Buf
        V2["\`mv[1000:1001000]\`<br>Points to (0x1000 + 1000), len=10MB"] -.->|Zero-Copy Window| Buf
    end
```

```python
raw_data = bytearray(50_000_000)
mv = memoryview(raw_data)

# Slicing creates a ~200-byte Py_buffer header pointing at (base_addr + offset)
chunk_view = mv[1000:10_001_000] # O(1) Time, O(1) Memory!
```

---

## 3. In-Place Memory Transfers: Slicing vs `memoryview` vs `ctypes.memmove`

When updating an existing pre-allocated destination buffer from a source buffer, there are three main approaches:

| Approach | Code | Mechanics | Speed | Allocation |
| :--- | :--- | :--- | :--- | :--- |
| **1. Bytes Slice Assign** | `dst[a:b] = src[a:b]` | Slices `src` into a temporary `bytes` object, then copies bytes into `dst`. | Slowest | Allocates temporary slice object |
| **2. Memoryview Assign** | `dst_mv[a:b] = src_mv[a:b]` | Slices views ($O(1)$ headers) and executes direct C buffer copy. | Fast | Zero payload allocations |
| **3. \`ctypes.memmove\`** | `ctypes.memmove(dst_addr, src_addr, count)` | Bypasses Python object layer completely, invokes C libc `memmove(3)`. | Fastest (SIMD) | Zero Python objects created |

### Using `ctypes.memmove`
```python
import ctypes

src_ba = bytearray(b"Hello World" * 1000)
dst_ba = bytearray(len(src_ba))

# Obtain underlying C pointers directly from bytearray buffers
src_ptr = (ctypes.c_char * len(src_ba)).from_buffer(src_ba)
dst_ptr = (ctypes.c_char * len(dst_ba)).from_buffer(dst_ba)

src_addr = ctypes.addressof(src_ptr) + 1000
dst_addr = ctypes.addressof(dst_ptr) + 1000
copy_size = 5000

# Direct C memcpy / memmove at hardware speed
ctypes.memmove(dst_addr, src_addr, copy_size)
```

---

## 4. Multi-Threading & Parallel Memory Writes (Releasing the GIL)

### The GIL Dilemma in Python
In pure Python, CPU-bound tasks in multiple threads are serialized by the Global Interpreter Lock (GIL). However:
* **`memoryview` for Concurrent Reads**: Multiple threads can read from an immutable `bytes` memoryview concurrently without locking.
* **`ctypes.memmove` for Parallel Writes**: `ctypes` functions release the GIL during native C execution. This allows multiple threads to write into non-overlapping regions of a pre-allocated memory buffer in **true parallel execution** on multiple CPU cores!

```mermaid
flowchart TD
    subgraph Pre-Allocated Target Buffer (40 MB)
        B0["Chunk 0 (0-10 MB)"]
        B1["Chunk 1 (10-20 MB)"]
        B2["Chunk 2 (20-30 MB)"]
        B3["Chunk 3 (30-40 MB)"]
    end

    T0["Thread 0 (ctypes.memmove)<br>[Releases GIL]"] -->|Writes to| B0
    T1["Thread 1 (ctypes.memmove)<br>[Releases GIL]"] -->|Writes to| B1
    T2["Thread 2 (ctypes.memmove)<br>[Releases GIL]"] -->|Writes to| B2
    T3["Thread 3 (ctypes.memmove)<br>[Releases GIL]"] -->|Writes to| B3
```

```python
from concurrent.futures import ThreadPoolExecutor
import ctypes

def parallel_buffer_copy(dst_ba: bytearray, src_ba: bytearray, num_workers=4):
    total_size = len(src_ba)
    chunk_size = total_size // num_workers

    src_ptr = (ctypes.c_char * total_size).from_buffer(src_ba)
    dst_ptr = (ctypes.c_char * total_size).from_buffer(dst_ba)

    def _worker(worker_id):
        offset = worker_id * chunk_size
        s_addr = ctypes.addressof(src_ptr) + offset
        d_addr = ctypes.addressof(dst_ptr) + offset
        # Releases GIL during memmove
        ctypes.memmove(d_addr, s_addr, chunk_size)

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        list(executor.map(_worker, range(num_workers)))
```

---

## 5. Multi-Processing & Zero-Copy POSIX Shared Memory

When scaling across processes (`multiprocessing`), standard IPC (`Queue`, `Pipe`) incurs heavy overhead:
1. Object Serialization (`pickle.dumps`).
2. OS Socket/Pipe transport copy.
3. Object Deserialization (`pickle.loads`).

### Solution: `multiprocessing.shared_memory` + `memoryview`
By combining POSIX Shared Memory with `memoryview` and `ctypes.memmove`, separate OS processes share the exact same physical RAM pages zero-copy:

```mermaid
flowchart LR
    subgraph POSIX Shared Memory (/dev/shm)
        RAM["Physical RAM Segment<br>(e.g. 500 MB)"]
    end

    subgraph Process 1 (Parent)
        P1_MV["memoryview(shm.buf)"] -.->|Points to| RAM
    end

    subgraph Process 2 (Worker A)
        P2_Ptr["ctypes.memmove()"] -->|Direct Write Slice A| RAM
    end

    subgraph Process 3 (Worker B)
        P3_Ptr["ctypes.memmove()"] -->|Direct Write Slice B| RAM
    end
```

### Code Implementation:
```python
from multiprocessing import shared_memory, Process
import ctypes

def child_worker(shm_name: str, offset: int, data: bytes):
    existing_shm = shared_memory.SharedMemory(name=shm_name)
    try:
        ba_data = bytearray(data)
        src_ptr = (ctypes.c_char * len(ba_data)).from_buffer(ba_data)
        dst_ptr = (ctypes.c_char * len(existing_shm.buf)).from_buffer(existing_shm.buf)
        
        dst_addr = ctypes.addressof(dst_ptr) + offset
        src_addr = ctypes.addressof(src_ptr)
        
        # Zero-copy write directly into Shared Memory segment
        ctypes.memmove(dst_addr, src_addr, len(data))
        
        del src_ptr
        del dst_ptr
    finally:
        existing_shm.close()

# Parent Process
shm = shared_memory.SharedMemory(create=True, size=50_000_000)
try:
    p = Process(target=child_worker, args=(shm.name, 0, b"ZERO_COPY_PAYLOAD"))
    p.start()
    p.join()

    # Zero-copy read in parent
    mv = memoryview(shm.buf)
    print("Read from worker:", bytes(mv[0:17]))
    mv.release()
finally:
    shm.close()
    shm.unlink()
```

---

## 6. Summary Comparison Matrix

| Metric / Feature | Standard Slicing (`bytes[a:b]`) | `memoryview(buf)[a:b]` | `ctypes.memmove` |
| :--- | :--- | :--- | :--- |
| **Slicing Complexity** | $O(N)$ (Allocates & Copies) | $O(1)$ (Pointer Window) | N/A (Copy primitive) |
| **Memory Allocated** | Full copy size | Tiny (~200 B header) | $0$ Bytes |
| **Garbage Collector Impact** | Heavy (Triggers Gen 0 GC) | Minimal | None |
| **GIL Releasing** | No (holds GIL) | Yes (when passed to I/O C-APIs) | Yes (Native C execution) |
| **Best Used For** | Small strings/bytes (< 1 KB) | Sub-slicing, parsing streams, socket/file I/O | High-throughput parallel bulk transfers |
| **Multi-Threading** | Creates memory pressure | Thread-safe concurrent reads | Parallel thread writes to non-overlapping offsets |
| **Multi-Processing** | Avoid (Pickling overhead) | Wrap `shared_memory.buf` | Write directly to shared memory offsets |

---

## 7. Practical Rules of Thumb
1. **Never slice `bytes` in a tight loop**: When consuming binary protocols or chunking large payloads, wrap the buffer in `memoryview(buf)` first.
2. **Release views before resizing/closing**: Calling `mv.release()` or `del mv` is required before mutating the size of the underlying `bytearray` or unlinking `SharedMemory`.
3. **Use `ctypes.memmove` for multi-threaded chunking**: If you need to populate a large array using multiple CPU threads, pre-allocate the buffer and use `ctypes.memmove` with offsets to bypass GIL constraints.
