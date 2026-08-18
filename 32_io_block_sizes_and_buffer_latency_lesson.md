# Lesson 32: Isolated Latency Profiling & 50% Partial Read Comparison (128 KB to 64 MB)

This lesson isolates and compares the runtime latency of memory operations across **128 KB, 256 KB, 1 MB, 2 MB, 4 MB, 8 MB, 16 MB, 32 MB, and 64 MB**:

1. **Isolated Operation Latency**: Creating `bytes`, creating `bytearray`, overriding `bytearray`, creating `memoryview`, overriding `memoryview`.
2. **Partial Read Pipeline Comparison (50% Data Read)**: Reading 50% of a large buffer into a destination buffer across $x$ iterations comparing Naive Slicing vs. Pooled `memoryview`.

---

## 1. Isolated Latency Benchmark Results

| Buffer Size | 1. Create `bytes` (`b"X"*N`) | 2. Create `bytearray` (`bytearray(sz)`) | 3. Override `bytearray` (`ba[:] = data`) | 4. Create `memoryview` (`O(1)`) | 5. Override `memoryview` (`mv[:] = src`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **128 KB** | **0.002 ms** (2 µs) | **0.002 ms** (2 µs) | 0.006 ms (6 µs) | **0.08 µs** (80 ns) | **0.003 ms** (3 µs) |
| **256 KB** | **0.005 ms** (5 µs) | **0.004 ms** (4 µs) | 0.015 ms (15 µs) | **0.08 µs** (80 ns) | **0.011 ms** (11 µs) |
| **1 MB** | **0.044 ms** | **0.027 ms** | 0.076 ms | **0.08 µs** (80 ns) | **0.041 ms** |
| **2 MB** | **0.067 ms** | **0.034 ms** | 0.130 ms | **0.08 µs** (80 ns) | **0.059 ms** |
| **4 MB** | **0.120 ms** | **0.067 ms** | 0.251 ms | **0.08 µs** (80 ns) | **0.116 ms** |
| **8 MB** | **0.254 ms** | **0.155 ms** | 0.564 ms | **0.08 µs** (80 ns) | **0.222 ms** |
| **16 MB** | **0.912 ms** | **0.671 ms** | 2.086 ms | **0.08 µs** (80 ns) | **1.086 ms** |
| **32 MB** | **3.712 ms** | **2.871 ms** | 6.659 ms | **0.08 µs** (80 ns) | **1.625 ms** |
| **64 MB** | **6.183 ms** | **6.823 ms** | 11.285 ms | **0.08 µs** (80 ns) | **3.204 ms** |

---

## 2. Partial 50% Read Pipeline: Naive `bytes` vs. Pooled `memoryview`

When an application only needs to read a **partial subset (e.g. 50%)** of a large buffer:

* **Approach 1 (Naive Pipeline)**: Creates full `bytes` object $\rightarrow$ Slices 50% (`src_bytes[:half_sz]`, which creates a temporary slice object) $\rightarrow$ Copies into a new destination buffer `bytearray(...)`.
* **Approach 2 (Pooled `memoryview` Pipeline)**: Overwrites full pool buffer $\rightarrow$ Creates an $O(1)$ zero-copy window slice (`pool_mv[:half_sz]`) $\rightarrow$ Overwrites pre-allocated destination buffer in-place (`dst_mv[:] = pool_mv[:half_sz]`).

```mermaid
flowchart TD
    subgraph ❌ Approach 1: Naive (Double Copy & Allocations)
        A1["1. src_bytes = b'X'*sz (Allocates 64 MB)"] --> B1["2. src_bytes[:32MB] (Allocates 32 MB Temp Slice)"]
        B1 --> C1["3. bytearray(slice) (Allocates 32 MB Destination Buffer)"]
        C1 --> D1["Total per iteration: 128 MB allocated + 2 copies + GC pressure"]
    end

    subgraph ✅ Approach 2: Pooled memoryview (Zero-Copy 50% Slice)
        A2["1. pool_mv[:] = dummy_mv (Overwrites 64 MB pool buffer)"] --> B2["2. pool_mv[:32MB] (O(1) Zero-Copy View Header in 80 ns)"]
        B2 --> C2["3. dst_mv[:] = pool_mv[:32MB] (Direct in-place C copy)"]
        C2 --> D2["Total per iteration: 0 allocations + 0 temp objects"]
    end
```

---

### Partial 50% Read Benchmark Results

| Total Buffer Size | 50% Read Size | Iterations | Approach 1: Naive (50% Slice Copy) | Approach 2: Pooled `memoryview` | Speedup Factor |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **128 KB** | **0.06 MB** (64 KB) | 2,000 iters | 0.004 ms / iter | **0.004 ms / iter** | 1.0x |
| **256 KB** | **0.12 MB** (128 KB) | 1,000 iters | 0.010 ms / iter | **0.011 ms / iter** | 0.9x |
| **1 MB** | **0.50 MB** (512 KB) | 300 iters | 0.060 ms / iter | **0.055 ms / iter** | 1.1x |
| **2 MB** | **1.00 MB** | 150 iters | 0.126 ms / iter | **0.109 ms / iter** | 1.2x |
| **4 MB** | **2.00 MB** | 80 iters | 0.251 ms / iter | **0.219 ms / iter** | 1.1x |
| **8 MB** | **4.00 MB** | 40 iters | 0.516 ms / iter | **0.444 ms / iter** | 1.2x |
| **16 MB** | **8.00 MB** | 20 iters | 1.428 ms / iter | **1.259 ms / iter** | 1.1x |
| **32 MB** | **16.00 MB** | 10 iters | 6.621 ms / iter | **2.882 ms / iter** | 🚀 **2.3x Faster** |
| **64 MB** | **32.00 MB** | 5 iters | 18.065 ms / iter | **4.920 ms / iter** | 🚀 **3.7x Faster** |

---

### Key Architectural Takeaways for Partial Reads

1. **Elimination of the "Double-Copy Penalty"**:
   * In standard Python, slicing `src_bytes[:half_sz]` creates a **temporary `bytes` object** containing 32 MB of copied data.
   * Passing that temporary slice to `bytearray(...)` copies the 32 MB a **second time**.
   * With `memoryview`, `pool_mv[:half_sz]` is a zero-copy pointer window that creates **no intermediate objects**, writing directly to destination memory in a single pass.

2. **3.7x Faster at 64 MB (18.06 ms $\rightarrow$ 4.92 ms)**:
   * By avoiding 128 MB of memory allocations and temporary object creation per iteration, the pooled `memoryview` pipeline cuts per-iteration latency from **18.06 ms** down to **4.92 ms**.
