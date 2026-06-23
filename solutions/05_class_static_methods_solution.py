#!/usr/bin/env python3
"""
================================================================================
LESSON 5: CLASS AND STATIC METHODS — SOLUTION
================================================================================
"""

class Book:
    # Class variable to track total books created
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Increment the class variable on instantiation
        Book.total_books += 1

    def get_info(self):
        return f"{self.title} by {self.author}"

    @classmethod
    def from_string(cls, book_str):
        # Split the string by the separator " - "
        # E.g., "The Hobbit - J.R.R. Tolkien" -> ["The Hobbit", "J.R.R. Tolkien"]
        parts = book_str.split(" - ")
        title = parts[0].strip()
        author = parts[1].strip()
        
        # Instantiate the class (cls is equivalent to Book) and return the new object
        return cls(title, author)

    @staticmethod
    def is_bestseller(copies_sold):
        return copies_sold >= 100000


# --- TEST CODE ---
print("--- Running Book Class Tests ---")
# Test static method
print(f"Is 150k sold a bestseller? {Book.is_bestseller(150000)}") # Should be True
print(f"Is 50k sold a bestseller? {Book.is_bestseller(50000)}")   # Should be False

# Test standard constructor
b1 = Book("1984", "George Orwell")
print(b1.get_info()) # Should print: 1984 by George Orwell

# Test factory class method
b2 = Book.from_string("The Hobbit - J.R.R. Tolkien")
print(b2.get_info()) # Should print: The Hobbit by J.R.R. Tolkien

# Test class variable tracking
print(f"Total books cataloged: {Book.total_books}") # Should be 2
