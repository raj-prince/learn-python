#!/usr/bin/env python3
"""
================================================================================
LESSON 24: IO.IOBASE AND PYTHON STREAM ARCHITECTURE — SOLUTION
================================================================================
"""

import io

class SanitizingTextStream(io.TextIOBase):
    """Custom stream processor that redacts sensitive keywords on write."""
    
    def __init__(self, redactions: list[str]):
        super().__init__()
        self.redactions = redactions
        self._buffer = io.StringIO()

    def write(self, s: str) -> int:
        sanitized = s
        for word in self.redactions:
            sanitized = sanitized.replace(word, "[REDACTED]")
        self._buffer.write(sanitized)
        return len(s)

    def writable(self) -> bool:
        return True

    def getvalue(self) -> str:
        return self._buffer.getvalue()


if __name__ == "__main__":
    print("\n==================================================")
    print("RUNNING EXERCISE 24 SOLUTION")
    print("==================================================")
    
    secrets = ["PASSWORD", "SECRET", "API_KEY"]
    sanitizer = SanitizingTextStream(redactions=secrets)
    
    sanitizer.write("User login attempt with PASSWORD=12345!\n")
    sanitizer.write("Exporting API_KEY=abc_999 to config.\n")
    sanitizer.write("This line has no SECRET info.\n")
    
    output = sanitizer.getvalue()
    print("Sanitizer Stream Output:")
    print(output)
    
    assert "PASSWORD" not in output, "FAILED: 'PASSWORD' was not redacted!"
    assert "API_KEY" not in output, "FAILED: 'API_KEY' was not redacted!"
    assert "SECRET" not in output, "FAILED: 'SECRET' was not redacted!"
    assert "[REDACTED]" in output, "FAILED: '[REDACTED]' missing from output!"
    print("🎉 Solution Verified Successfully!")
