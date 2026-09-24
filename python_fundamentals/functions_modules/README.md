# Functions Modules

## 0.[islower](./islower.py)
Checks whether a single character is a lowercase letter without using Python's built-in .islower() method.
```py
Python

def islower(c):
    return 97 <= ord(c) <= 122
```

- ord(c): Converts a character into its numerical ASCII code (e.g., 'a' is 97, 'z' is 122).
- 97 <= ord(c) <= 122: Checks if the character's ASCII code falls in the lowercase range ($a$ to $z$)
- return: Returns True if it's lowercase, or False if it isn't.

## 1.[To Uppercase](./uppercase)

Converts lowercase letters in a string to uppercase manually using ASCII values and prints the result.

```py
Python

def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")

```
- for c in str:: Loops through each character in the string.
- 97 <= ord(c) <= 122: Checks if character c is lowercase.
- ord(c) - 32: In ASCII, subtracting 32 from a lowercase letter turns it into its uppercase equivalent (e.g., 'a' ($97$) becomes 'A' ($65$)).
- chr(...): Converts an ASCII code back into a text character.
- end="": Prints characters side-by-side on the same line.
- print(""): Prints a newline at the very end after the full string is processed.

## 2.[Print Last Digit](./print_last_digit.py)

Extracts, prints, and returns the last digit of any integer.

```py

Python

def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
```

- abs(number): Ensures negative numbers become positive (e.g., -1024 becomes 1024).

- % 10 (Modulo operator): Returns the remainder after dividing by 10, which is always the last digit (e.g., 1024 % 10 is 4).

- end="": Prevents print() from adding a newline character at the end.

```py

Python

if __name__ == "__main__":
    print_last_digit(98)     # Prints 8
    print()                  # Moves to a new line
    print_last_digit(0)      # Prints 0
    print()
    print_last_digit(-1024)  # Prints 4
    print()
```

## 3.[a ^ b](./pow.py)

Calculates $a$ raised to the power of $b$ ($a^b$) manually without using a ** b or pow().

```py

Python

def pow(a, b):
    result = 1
    for _ in range(abs(b)):
        result *= a
```

- abs(b): Takes the absolute (positive) value of b so the loop runs the correct number of times.
- for _ in range(...): Runs a loop b times. The underscore _ is used when you don't need the loop variable.
- result *= a: Multiplies result by a on every iteration.

```py

Python

    if b < 0:
        return 1 / result

    return result

```

- Negative Exponents: Mathematically, $a^{-b} = \frac{1}{a^b}$. If $b$ was negative, it returns $\frac{1}{\text{result}}$. Otherwise, it returns result directly.

## 4.[quiz]

## 5.[Import a Simple Function from a Simple File](./add.py)

This script imports a math function from another file, uses it, and prints the result.

```py

Python

#!/usr/bin/env python3
```
Shebang line: Tells Unix/Linux systems to run this file using Python 3.

```py
Python

from add_0 import add
```
Import statement: Opens another Python file named add_0.py and grabs the function named add so you can use it here.

```py
Python

if __name__ == "__main__":

```
Execution guard: Ensures the code inside it only runs when you execute add.py directly (e.g., python3 add.py), but not if another file tries to import add.py.

```py
Python

    a = 1
    b = 2
    c = add(a, b)

Variables & Function Call: Creates two variables, passes them into add(), and saves the returned sum inside c.

```py
Python

    print("{} + {} = {}".format(a, b, c))
```

Formatted Printing: Sets up placeholders ({}) and fills them sequentially with a, b, and c. Output: 1 + 2 = 3.

## 6.[My First Toolbox](./calculation.py)

Similar to add.py, but performs multiple math operations at once.

```py
Python

from calculator_1 import add, sub, mul, div

```

Imports four math functions—addition, subtraction, multiplication, and division—from calculator_1.py.

```py
Python
if __name__ == "__main__":
    a = 10
    b = 5

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
```

Formatted integers: {:d} explicitly tells Python to format the values as decimal integers. Instead of storing the result in a new variable first, it calls the function directly inside format().

## 7.[Everything Can Be Imported](./variable_load.py)

