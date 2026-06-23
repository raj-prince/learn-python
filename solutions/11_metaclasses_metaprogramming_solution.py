#!/usr/bin/env python3
"""
================================================================================
LESSON 11: METAPROGRAMMING AND METACLASSES — SOLUTION
================================================================================
"""

# 1. Global registry dictionary
PLUGINS = {}

# 2. Custom Metaclass
class PluginRegistryMeta(type):
    def __new__(cls, name, bases, dct):
        # Create the class object first
        new_class = super().__new__(cls, name, bases, dct)
        
        # 3. Prevent registering the base class itself
        if name != "BasePlugin":
            # If the class defines a custom plugin_name attribute, use it as the key.
            # Otherwise, default to the class name.
            plugin_key = dct.get("plugin_name", name)
            PLUGINS[plugin_key] = new_class
            
        return new_class

# 4. Base class that hooks up the metaclass
class BasePlugin(metaclass=PluginRegistryMeta):
    pass


# --- TEST CODE ---
class ImageCompressor(BasePlugin):
    # Custom plugin name
    plugin_name = "image_compressor"
    
    def run(self):
        print("🖼️ Compressing image...")

class TextTranslator(BasePlugin):
    # Will default to using the class name "TextTranslator" as registry key
    def run(self):
        print("📝 Translating text...")

if __name__ == "__main__":
    print("\n==================================================")
    print("RUNNING EXERCISE 11 TESTS")
    print("==================================================")
    
    # Check if the plugins were registered automatically by the metaclass
    print(f"Registered Plugins: {list(PLUGINS.keys())}")
    
    # Instantiate and run all registered plugins dynamically!
    print("\nExecuting all registered plugins:")
    for plugin_name, plugin_class in PLUGINS.items():
        instance = plugin_class()
        print(f"Running: {plugin_name}")
        instance.run()
