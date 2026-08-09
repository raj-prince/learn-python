#!/usr/bin/env python3
"""
================================================================================
SOLUTION: LESSON 31 — MONKEY PATCHING & RUNTIME DYNAMIC BEHAVIOR MODIFICATION
================================================================================
"""

class TemporaryPatch:
    """
    A custom context manager that temporarily monkey patches an attribute
    on a target object/module and automatically restores it upon exit.
    """

    def __init__(self, target_obj, attr_name: str, new_value):
        self.target_obj = target_obj
        self.attr_name = attr_name
        self.new_value = new_value
        self.original_value = getattr(target_obj, attr_name)

    def __enter__(self):
        setattr(self.target_obj, self.attr_name, self.new_value)
        return self.new_value

    def __exit__(self, exc_type, exc_val, exc_tb):
        setattr(self.target_obj, self.attr_name, self.original_value)


def run_exercise_tests():
    print("\n==================================================")
    print("RUNNING EXERCISE 31 TESTS")
    print("==================================================")
    
    class DatabaseConfig:
        host = "production-db.internal"
        
    config = DatabaseConfig()
    assert config.host == "production-db.internal", "FAILED: Original host incorrect"
    
    with TemporaryPatch(config, "host", "localhost-test-db"):
        assert config.host == "localhost-test-db", "FAILED: Patch was not applied inside context!"
        print("Inside patch context: host =", config.host)
        
    assert config.host == "production-db.internal", "FAILED: Patch was not reverted after exit!"
    print("Outside patch context: host =", config.host)
    print("🎉 Exercise 31 Passed Successfully!")


if __name__ == "__main__":
    run_exercise_tests()
