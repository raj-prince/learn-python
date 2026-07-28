#!/usr/bin/env python3
"""
================================================================================
LESSON 21: CALLING RUST FROM PYTHON & RELEASING THE GIL
================================================================================

Python is loved for its developer velocity, while Rust is built for raw performance,
memory safety, and concurrency. Combining Python and Rust gives you the best of both worlds.

This lesson explores:
1. How to call Rust code from Python (Modern PyO3 + maturin vs C-FFI / ctypes).
2. How calling Rust removes the Global Interpreter Lock (GIL) bottleneck.
3. How Rust achieves true multi-threaded CPU speedups across all cores.

--------------------------------------------------------------------------------
HOW RUST ELIMINATES THE GIL BOTTLENECK
--------------------------------------------------------------------------------
- THE GIL PROBLEM:
  CPython's Global Interpreter Lock enforces that only ONE thread executes Python 
  bytecode at any given moment. Adding Python threads (`threading.Thread`) for 
  CPU-bound tasks yields NO speedup because threads block waiting for the GIL.

- THE RUST SOLUTION:
  When Python enters compiled Rust code, execution leaves Python bytecode and enters 
  raw native machine instructions. 

  1. In PyO3: You wrap CPU-heavy logic in `py.allow_threads(|| { ... })`.
     This temporarily unlocks CPython's GIL (`PyEval_SaveThread()`), allowing 
     other Python threads to run freely on other CPU cores!
  2. Inside Rust: You can spawn native OS threads or use Rayon data parallelism 
     to utilize 100% of all available CPU cores at raw hardware speed.
  3. Re-acquiring the GIL: Once Rust finishes the calculation, it re-locks the GIL 
     (`PyEval_RestoreThread()`) only to return the result object back to Python.

--------------------------------------------------------------------------------
TWO MAIN METHODS TO BIND RUST & PYTHON
--------------------------------------------------------------------------------
Method A: PyO3 + maturin (RECOMMENDED FOR PRODUCTION)
  - PyO3 generates native CPython extension modules (`.so` / `.pyd`).
  - Seamless type conversion (`Vec<T>` <-> `list`, `String` <-> `str`, `PyResult<T>`).
  - Native GIL control via `py.allow_threads(...)`.

Method B: Rust `cdylib` + Python `ctypes` (ZERO THIRD-PARTY DEPENDENCIES)
  - Rust exposes C ABI functions with `#[no_mangle] pub extern "C"`.
  - Compiled directly into a `.so` shared library.
  - Loaded into Python via standard library `ctypes.CDLL()`.
  - `ctypes` foreign C calls AUTOMATICALLY release the GIL!
"""

import sys
import os
import time
import ctypes
import subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor


# ================================================================================
# PART 1: RUST SOURCE CODE & FFI DYNAMIC COMPILATION
# ================================================================================

RUST_C_ABI_CODE = """
// Rust C-ABI Shared Library Source (rust_math.rs)
// Compiled as a C-compatible dynamic library (cdylib)

#[no_mangle]
pub extern "C" fn rust_cpu_heavy_work(iterations: u64) -> f64 {
    // This runs in pure native machine code without touching Python runtime/GIL!
    let mut sum = 0.0f64;
    for i in 1..=iterations {
        sum += (i as f64).sqrt().sin().cos();
    }
    sum
}
"""


def compile_rust_library(scratch_dir: Path) -> Path:
    """Compiles the Rust C-ABI source into a shared library (.so)."""
    scratch_dir.mkdir(parents=True, exist_ok=True)
    rs_path = scratch_dir / "rust_math.rs"
    so_path = scratch_dir / "librust_math.so"

    rs_path.write_text(RUST_C_ABI_CODE)

    # Locate cargo / rustc
    cargo_home = Path.home() / ".cargo" / "bin"
    rustc_bin = cargo_home / "rustc"
    if not rustc_bin.exists():
        rustc_bin = "rustc"

    # Compile rust source into .so shared object
    cmd = [str(rustc_bin), "--crate-type", "cdylib", "-O", str(rs_path), "-o", str(so_path)]
    subprocess.run(cmd, check=True)
    return so_path


# ================================================================================
# PART 2: DEMONSTRATING RUST INVOCATION VIA CTYPES & GIL RELEASE
# ================================================================================

def pure_python_cpu_work(iterations: int) -> float:
    import math
    sum_val = 0.0
    for i in range(1, iterations + 1):
        sum_val += math.cos(math.sin(math.sqrt(i)))
    return sum_val


def demonstrate_rust_ctypes_and_gil(so_path: Path):
    print("\n" + "=" * 80)
    print("PART 2: DEMONSTRATING RUST INVOCATION VIA CTYPES & GIL RELEASE")
    print("=" * 80)

    # Load Rust dynamic library into Python
    rust_lib = ctypes.CDLL(str(so_path))
    
    # Define Rust function argument and return types
    rust_lib.rust_cpu_heavy_work.argtypes = [ctypes.c_uint64]
    rust_lib.rust_cpu_heavy_work.restype = ctypes.c_double

    iterations = 5_000_000
    num_threads = 4

    print(f"⚡ Iterations per task: {iterations:,} | Threads: {num_threads}")

    # ----------------------------------------------------------------------------
    # 1. Pure Python Multi-Threading (GIL BOTTLENECK - NO SPEEDUP)
    # ----------------------------------------------------------------------------
    start_t = time.perf_counter()
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(pure_python_cpu_work, iterations) for _ in range(num_threads)]
        _py_results = [f.result() for f in futures]
    t_python_threads = time.perf_counter() - start_t
    print(f"⏱️  Pure Python ({num_threads} Threads with GIL): {t_python_threads:.4f} sec")

    # ----------------------------------------------------------------------------
    # 2. Rust Multi-Threading via ctypes (GIL RELEASED - PARALLEL HARDWARE SPEED)
    # ----------------------------------------------------------------------------
    start_t = time.perf_counter()
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # ctypes releases the GIL during foreign function calls!
        futures = [executor.submit(rust_lib.rust_cpu_heavy_work, iterations) for _ in range(num_threads)]
        _rust_results = [f.result() for f in futures]
    t_rust_threads = time.perf_counter() - start_t
    print(f"🚀 Rust via ctypes ({num_threads} Threads, GIL Released): {t_rust_threads:.4f} sec")

    speedup = t_python_threads / max(t_rust_threads, 0.00001)
    print(f"🔥 Speedup Factor: {speedup:.1f}x Faster with Rust + GIL Release!")


# ================================================================================
# PART 3: MODERN PYO3 & MATURIN OVERVIEW (PRODUCTION PATTERN)
# ================================================================================

def print_pyo3_production_guide():
    print("\n" + "=" * 80)
    print("PART 3: MODERN PYO3 & MATURIN PRODUCTION PATTERN")
    print("=" * 80)
    guide = """
In production Python/Rust projects (like Polars, Cryptography, Pydantic V2, Tiktoken):

1. Project Layout:
   my_project/
   ├── Cargo.toml          # Rust package config (depends on pyo3 = "0.20")
   ├── pyproject.toml      # Configured with maturin build-backend
   └── src/
       └── lib.rs          # Rust module logic

2. Rust Code with PyO3 & Rayon (lib.rs):
   --------------------------------------------------------------------
   use pyo3::prelude::*;
   use rayon::prelude::*;

   #[pyfunction]
   fn compute_heavy_parallel(py: Python, numbers: Vec<f64>) -> PyResult<f64> {
       // 1. Release Python GIL
       let result = py.allow_threads(|| {
           // 2. Parallel multi-threaded processing using Rayon across all CPU cores
           numbers.par_iter().map(|n| n.sqrt().sin().cos()).sum()
       });
       Ok(result)
   }

   #[pymodule]
   fn my_rust_ext(_py: Python, m: &PyModule) -> PyResult<()> {
       m.add_function(wrap_pyfunction!(compute_heavy_parallel, m)?)?;
       Ok(())
   }
   --------------------------------------------------------------------

3. Building & Installing:
   $ pip install maturin
   $ maturin develop              # Builds native .so and installs into active venv!

4. Importing in Python:
   import my_rust_ext
   res = my_rust_ext.compute_heavy_parallel([1.0, 2.0, 3.0])
"""
    print(guide)


# ================================================================================
# MAIN EXECUTION
# ================================================================================

if __name__ == "__main__":
    scratch_path = Path(__file__).parent / "scratch_rust"
    try:
        so_file = compile_rust_library(scratch_path)
        demonstrate_rust_ctypes_and_gil(so_file)
    except Exception as exc:
        print(f"Rust compilation/execution skipped or failed: {exc}")
    
    print_pyo3_production_guide()
