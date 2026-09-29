# Exception Handling

Welcome to the **Exception Handling** section of the `python_fundamentals` module! 

When writing software, things don't always go as planned. A user might enter text when you asked for a number, or code might try to access an item in a list that doesn't exist. Instead of allowing the program to crash, Python allows us to handle these errors gracefully using **Exceptions**.

---

## 🎯 What is Exception Handling?

In Python, an **exception** is an error that occurs while a program is running. **Exception handling** is a mechanism that catches these errors, prevents the program from abruptly stopping, and allows you to decide what to do next.

### Key Keywords

* **`try`**: Wraps the block of code you want to test for errors.
* **`except`**: Executes if an error occurs inside the `try` block.
* **`else`**: Executes if **no** errors occurred inside the `try` block.
* **`finally`**: Executes no matter what (whether an error occurred or not).
* **`raise`**: Manually triggers an exception when a specific condition is met.

---

## 🛠️ Code Breakdown & Concept Explanations

Here is how common exception-handling patterns work in this directory:

### 1. Safe Printing & Catching Specific Errors (`IndexError`)

**Concept:** Catching out-of-bounds access safely.

```python
def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list safely."""
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            # Reached the end of the list before printing x elements
            break
    print("")  # New line
    return count
💡 Why this matters: If x is larger than the length of my_list, accessing my_list[i] normally crashes with an IndexError. The try-except IndexError block intercepts the error and lets the loop stop cleanly.

2. Type Verification (TypeError & ValueError)
Concept: Checking if an input is valid before operating on it.

```py
Python
def safe_print_integer(value):
    """Prints an integer with "{:d}".format()."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
```
💡 Why this matters: Passing a string like "hello" into "{:d}".format() triggers a ValueError or TypeError. The except (ValueError, TypeError): block catches either error and returns False instead of terminating the script.

3. Division & Cleanup (ZeroDivisionError + finally)
Concept: Handling math errors and ensuring cleanup actions always run.

```py
Python
def safe_print_division(a, b):
    """Divides 2 integers and prints the result."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
```
💡 Why this matters: Dividing by zero is mathematically undefined and throws a ZeroDivisionError. Using finally guarantees that Inside result: ... is printed whether division succeeded or failed.

4. Raising Custom Exceptions (raise)
Concept: Forcing an error when constraints are violated.

```py
Python
def raise_exception():
    """Raises a TypeError exception deliberately."""
    raise TypeError("Custom error message")
```
💡 Why this matters: raise allows you to stop execution when an invalid condition occurs in your own logic and send a message up to whichever part of the program called the function.
