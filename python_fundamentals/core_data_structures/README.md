# Core Data Structures 🧱

Welcome to the **Core Data Structures** directory of the `python_fundamentals` module! 

In programming, a **data structure** is simply a way to organize, store, and manage data so that we can use it efficiently. Python gives us four main built-in collection types: **Lists**, **Tuples**, **Sets**, and **Dictionaries**.

---

## 💡 Quick Overview of Data Structures

| Structure | Syntax | Ordered? | Mutable? (Can change?) | Allows Duplicates? | Analogy |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **List** | `[1, 2, 3]` | Yes | ✅ Yes | ✅ Yes | A grocery shopping list |
| **Tuple** | `(1, 2, 3)` | Yes | ❌ No | ✅ Yes | GPS coordinates `(lat, long)` |
| **Set** | `{1, 2, 3}` | No | ✅ Yes | ❌ No | A collection of unique unique tags/badges |
| **Dictionary** | `{"a": 1}` | Yes* | ✅ Yes | Keys: ❌ / Values: ✅ | A phonebook (`Name -> Phone #`) |

*\*Dictionaries maintain insertion order in Python 3.7+.*

---

## 🛠️ Concepts & Code Explanations

---

### 1. Lists (`[]`) — Flexible & Ordered Collections

Lists store an ordered collection of items where position (indexing) matters. You can add, remove, or modify items at any time.

```py
python
def print_list_integer(my_list=[]):
    """Prints all integers of a list, one per line."""
    for item in my_list:
        print("{:d}".format(item))
```
```py
Python
def element_at(my_list, idx):
    """Retrieves an element from a list at a specific index."""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
```
💡 Key Takeaways for Beginners:

Python lists use 0-based indexing: the first element is at my_list[0].

Always check if idx is within valid bounds (0 <= idx < len(my_list)) to prevent IndexError crashes.

2. Tuples (()) — Immutable Sequences
Tuples are similar to lists, but with one crucial rule: they cannot be changed after creation (this property is called immutability).

```py
Python
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys using tuples."""
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
```
```py
Python
def tuple_addition(tuple_a=(), tuple_b=()):
    """Adds first 2 elements of two tuples together."""
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a1 + b1, a2 + b2)
```
💡 Key Takeaways for Beginners:

Tuples are great for data that should never accidentally be modified (e.g., coordinates, RGB color values, fixed database rows).

Attempting my_tuple[0] = 5 will raise a TypeError.

3. Sets ({}) — Unique Elements Only
A Set is an unordered collection of items where every element must be unique. Duplicate items are automatically removed.

```py
Python
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix."""
    return [[x ** 2 for x in row] for row in matrix]
```
```py
Python
def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets (Intersection)."""
    return set_1 & set_2
```
💡 Key Takeaways for Beginners:

Use sets when you want to eliminate duplicates or quickly check if an item exists (x in my_set is lightning fast).

Set mathematical operations:

& (Intersection): Items present in both sets.

| (Union): All items from both sets combined.

- (Difference): Items in the first set but not in the second.

4. Dictionaries ({key: value}) — Key-Value Pair Mapping
A Dictionary stores data in pairs: a unique key mapped to a value. Think of looking up a word in a real dictionary: the word is the key, and the definition is the value.

```py
Python
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary with keys sorted alphabetically."""
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
```
```py
Python
def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary."""
    a_dictionary[key] = value
    return a_dictionary
```
💡 Key Takeaways for Beginners:

Keys must be unique and immutable (strings, numbers, tuples).

Values can be anything (integers, lists, even other dictionaries).

Accessing a key with a_dictionary[key] is very fast, but using a_dictionary.get(key) is safer because it doesn't crash if the key is missing.
