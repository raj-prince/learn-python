#!/usr/bin/env python3
"""
================================================================================
LESSON 24: IO.IOBASE AND PYTHON STREAM ARCHITECTURE
================================================================================

In Python, all input/output operations (file objects, network sockets, 
in-memory string/bytes buffers, and standard input/output) are built on top 
of the `io` module's abstract base class hierarchy, rooted at `io.IOBase`.

Understanding `io.IOBase` allows you to write polymorphic functions that can 
read from or write to disk files, network payloads, or memory buffers 
interchangeably, and build custom stream processors.

--------------------------------------------------------------------------------
1. THE IO MODULE HIERARCHY
--------------------------------------------------------------------------------
                     io.IOBase (Abstract Base Class)
                        │
      ┌─────────────────┼─────────────────┐
      ▼                 ▼                 ▼
 io.RawIOBase      io.BufferedIOBase   io.TextIOBase
 (Low-level raw)    (Buffered binary)  (Unicode text)
  e.g., FileIO       e.g., BytesIO,     e.g., StringIO,
                     BufferedReader     TextIOWrapper, open()

--------------------------------------------------------------------------------
2. CORE CAPABILITIES AND METHODS OF IOBASE
--------------------------------------------------------------------------------
- Stream Capabilities:
    `readable()` -> Returns True if stream supports read operations.
    `writable()` -> Returns True if stream supports write operations.
    `seekable()` -> Returns True if stream supports random positioning (seek/tell).
    `isatty()`   -> Returns True if stream is connected to a TTY/terminal.

- Lifecycle & Context Management:
    `close()`    -> Flushes write buffers and closes stream (sets `closed` = True).
    `closed`     -> Read-only boolean property.
    `__enter__`/`__exit__` -> Context manager support (automatic closing).

- Reading & Writing:
    `read()`, `write()`, `flush()`, `seek(offset, whence)`, `tell()`
    `readline()`, `readlines()`, `writelines()`
    Iterability: `for line in stream:`
"""

import io
import json
import shutil


# ================================================================================
# PART 1: IN-MEMORY STREAMS (io.StringIO & io.BytesIO)
# ================================================================================

def demonstrate_in_memory_streams():
    print("\n" + "=" * 80)
    print("PART 1: IN-MEMORY STREAMS (StringIO & BytesIO)")
    print("=" * 80)

    # 1. Text Stream in Memory (io.StringIO)
    text_stream = io.StringIO()
    text_stream.write("Line 1: Python I/O Streams\n")
    text_stream.write("Line 2: Fast in-memory processing without disk I/O!\n")

    # Retrieve full buffer content without seeking
    print("StringIO `getvalue()` output:")
    print(text_stream.getvalue())

    # Seek back to beginning to read line-by-line
    text_stream.seek(0)
    print("Reading line-by-line after seek(0):")
    for line in text_stream:
        print(f"  > {line.strip()}")

    # 2. Binary Stream in Memory (io.BytesIO)
    binary_stream = io.BytesIO()
    binary_stream.write(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR")
    print(f"\nBytesIO buffer size: {len(binary_stream.getvalue())} bytes")
    print(f"BytesIO raw bytes: {binary_stream.getvalue()}")


# ================================================================================
# PART 2: POLYMORPHIC FUNCTIONS ACCEPTING ANY IOBASE STREAM
# ================================================================================

def export_report(data: dict, stream: io.IOBase):
    """
    Polymorphic export function: Accepts ANY writable stream!
    Can write to a file object, stdout, or a StringIO memory buffer.
    """
    if not stream.writable():
        raise ValueError("Provided stream is not writable!")

    # Format data into stream
    stream.write(f"=== REPORT: {data.get('title', 'UNTITLED')} ===\n")
    for key, val in data.get("metrics", {}).items():
        stream.write(f"  - {key}: {val}\n")
    stream.write("=== END OF REPORT ===\n")


def demonstrate_polymorphic_streams():
    print("\n" + "=" * 80)
    print("PART 2: POLYMORPHISM WITH IOBASE")
    print("=" * 80)

    report_data = {
        "title": "System Performance",
        "metrics": {"CPU": "12%", "Memory": "4.2GB / 16GB", "Uptime": "99.9%"}
    }

    # Case A: Export directly to an in-memory string buffer
    mem_stream = io.StringIO()
    export_report(report_data, mem_stream)
    print("1. Exported to io.StringIO:")
    print(mem_stream.getvalue())

    # Case B: Export to a disk file using standard open()
    with open("report.txt", "w", encoding="utf-8") as file_stream:
        export_report(report_data, file_stream)
    print("2. Exported to disk file 'report.txt' (Check file on disk!)")


# ================================================================================
# PART 3: CUSTOM STREAM CLASS (SUBCLASSING io.TextIOBase)
# ================================================================================

class PrefixTextStream(io.TextIOBase):
    """
    Custom Stream Processor that inherits from io.TextIOBase.
    Automatically prepends a timestamp or prefix to every line written!
    """

    def __init__(self, prefix: str = "[LOG]"):
        super().__init__()
        self.prefix = prefix
        self._buffer = io.StringIO()

    def write(self, s: str) -> int:
        """Override write() to intercept and transform input text."""
        lines = s.splitlines(keepends=True)
        transformed = ""
        for line in lines:
            if line.strip():
                transformed += f"{self.prefix} {line}"
            else:
                transformed += line
        self._buffer.write(transformed)
        return len(s)

    def getvalue(self) -> str:
        """Retrieve accumulated transformed text."""
        return self._buffer.getvalue()

    def writable(self) -> bool:
        """Declare capability."""
        return True


def demonstrate_custom_stream():
    print("\n" + "=" * 80)
    print("PART 3: CUSTOM STREAM (SUBCLASSING io.TextIOBase)")
    print("=" * 80)

    log_stream = PrefixTextStream(prefix="[INFO]")
    log_stream.write("Application started.\n")
    log_stream.write("Connecting to database...\n")
    log_stream.write("Connection established!\n")

    print("Custom Stream Output:")
    print(log_stream.getvalue())


# ================================================================================
# PART 4: METACLASS CACHING FOR STREAMS (STOPPING GARBAGE COLLECTION)
# ================================================================================

class StreamCacheMeta(type):
    """
    Metaclass that caches stream objects by URI/filename.
    Maintains strong references to created streams so Python's Garbage Collector
    does not close or destroy them even when caller references are dropped.
    """

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._stream_cache = {}

    def __call__(cls, uri: str, *args, **kwargs):
        if uri not in cls._stream_cache:
            print(f"  [Metaclass] Opening new stream for URI: '{uri}'")
            cls._stream_cache[uri] = super().__call__(uri, *args, **kwargs)
        else:
            print(f"  [Metaclass] Returning cached stream for URI: '{uri}'")

        return cls._stream_cache[uri]


class ManagedFileStream(metaclass=StreamCacheMeta):
    """A stream wrapper managed by StreamCacheMeta."""

    def __init__(self, uri: str):
        self.uri = uri
        self.stream = io.StringIO()

    def write(self, text: str):
        self.stream.write(text)

    def read_all(self) -> str:
        return self.stream.getvalue()


def demonstrate_metaclass_stream_caching():
    print("\n" + "=" * 80)
    print("PART 4: METACLASS STREAM CACHING & GARBAGE COLLECTION")
    print("=" * 80)

    s1 = ManagedFileStream("session_log.txt")
    s1.write("Session 1 active.\n")

    # Local variable s1 deleted
    del s1

    # Re-instantiating returns the exact same cached object!
    s2 = ManagedFileStream("session_log.txt")
    s2.write("Session 2 appended.\n")

    print("\nContent of persistent cached stream:")
    print(s2.read_all())
    print(f"Cache registry: {ManagedFileStream._stream_cache}")


# ================================================================================
# YOUR TURN: EXERCISE 24
# ================================================================================
# Scenario:
# You are building a secure logging pipeline. Sensitive words like "PASSWORD",
# "SECRET", and "API_KEY" must never be written in plain text to logs.
#
# INSTRUCTIONS:
# 1. Create a custom stream class `SanitizingTextStream` that inherits from `io.TextIOBase`.
# 2. In `__init__(self, redactions: list[str])`:
#    - Store a list of redacted words.
#    - Initialize an internal `io.StringIO()` buffer named `self._buffer`.
# 3. Override `write(self, s: str) -> int`:
#    - Replace every occurrence of any target redaction word in `s` with `"[REDACTED]"`.
#    - Write the sanitized string into `self._buffer`.
#    - Return the length of the original string `s`.
# 4. Override `writable(self) -> bool`:
#    - Return `True`.
# 5. Add a `getvalue(self) -> str` method:
#    - Return `self._buffer.getvalue()`.
#
# Un-comment the test code at the bottom of the file once you've written your solution!
# ================================================================================

# WRITE YOUR SanitizingTextStream CLASS HERE:




if __name__ == "__main__":
    demonstrate_in_memory_streams()
    demonstrate_polymorphic_streams()
    demonstrate_custom_stream()
    demonstrate_metaclass_stream_caching()

    # --- EXERCISE 24 TEST CODE (Un-comment below to test your implementation) ---
    # print("\n==================================================")
    # print("RUNNING EXERCISE 24 TESTS")
    # print("==================================================")
    # 
    # secrets = ["PASSWORD", "SECRET", "API_KEY"]
    # sanitizer = SanitizingTextStream(redactions=secrets)
    # 
    # sanitizer.write("User login attempt with PASSWORD=12345!\n")
    # sanitizer.write("Exporting API_KEY=abc_999 to config.\n")
    # sanitizer.write("This line has no SECRET info.\n")
    # 
    # output = sanitizer.getvalue()
    # print("Sanitizer Stream Output:")
    # print(output)
    # 
    # assert "PASSWORD" not in output, "FAILED: 'PASSWORD' was not redacted!"
    # assert "API_KEY" not in output, "FAILED: 'API_KEY' was not redacted!"
    # assert "SECRET" not in output, "FAILED: 'SECRET' was not redacted!"
    # assert "[REDACTED]" in output, "FAILED: '[REDACTED]' missing from output!"
    # print("🎉 Exercise 24 Passed Successfully!")

