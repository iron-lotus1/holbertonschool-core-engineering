# Python File I/O: Reading, Writing, and Appending

This directory demonstrates how to work with external text files in Python using the built-in `open()` function, context managers (`with` statement), and standard file modes (`r`, `w`, `a`).

---

## 🎯 Key Concepts to Learn

### 1. The Context Manager (`with` Statement)
When opening files in Python, it is standard practice to use the `with` statement:

```python
with open("filename.txt", "r") as file:
    # Operations on file
Why use it? It automatically closes the file when the block finishes—even if an error or exception occurs. This prevents memory leaks and file corruption.2. File ModesThe second argument of open() specifies what action you want to perform:ModeNameDescription"r"ReadDefault. Opens a file for reading. Raises an error if the file doesn't exist."w"WriteOpens a file for writing. Overwrites existing contents or creates a new file."a"AppendOpens a file for writing. Appends data to the end without deleting existing contents.3. Encoding (utf-8)Specifying encoding="utf-8" ensures that characters across all human languages, special symbols, and emojis are consistently interpreted across different operating systems (Linux, macOS, Windows).📂 File Explanations1. Reading a File (read_file.py)Reads the entire contents of a UTF-8 text file and prints it directly to standard output (stdout).Python#!/usr/bin/env python3
"""Module that reads a UTF-8 text file and prints its contents."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its contents to stdout."""
    with open(filename, encoding="utf-8") as read_data:
        print(read_data.read(), end="")
read_data.read(): Reads the entire file content into memory as a single string.end="": Prevents Python's print() function from adding an unnecessary extra newline at the end of the file output.2. Writing to a File (write_file.py)Writes a string into a file using "w" mode and returns the total number of characters written.Python#!/usr/bin/env python3
"""Function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 file and return the number of characters written."""
    with open(filename, mode="w", encoding="utf-8") as my_first_file:
        nb_characters = my_first_file.write(text)
        return nb_characters
mode="w": If filename already exists, its contents are completely replaced. If it doesn't exist, Python creates a new file automatically.file.write(text): Writes the string and returns an integer representing the exact count of written characters.3. Appending to a File (append_write.py)Appends text to the end of an existing file using "a" mode without overwriting existing data.Python#!/usr/bin/env python3
"""Function that appends a string at the end of text file."""


def append_write(filename="", text=""):
    """Returns the number of characters added."""
    with open(filename, mode="a", encoding="utf-8") as file_append:
        nb_characters_added = file_append.write(text)
        return nb_characters_added
mode="a": Places the file cursor at the end of the file. Any text passed to .write() will be added after existing content.🧪 Quick Usage ExampleYou can test these functions in Python like this:Pythonfrom read_file import read_file
from write_file import write_file
from append_write import append_write

# 1. Write initial text to a new file
chars_written = write_file("example.txt", "Hello World!\n")
print(f"Wrote {chars_written} characters.")

# 2. Append additional text to the same file
chars_appended = append_write("example.txt", "Appending a second line.\n")
print(f"Appended {chars_appended} characters.")

# 3. Read and output the final contents
read_file("example.txt")
Output:PlaintextWrote 13 characters.
Appended 25 characters.
Hello World!
Appending a second line.
