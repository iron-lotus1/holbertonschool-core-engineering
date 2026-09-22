## 1. [The Last digit](./last_digit.py) (`if`, `elif`, `else`)


Conditional statements allow your program to make decisions based on specific conditions.

- **`if`**: Evaluates the first condition. If `True`, its code block runs.
    
- **`elif`**: Short for "else if". Evaluates additional conditions sequentially if all preceding `if` or `elif` checks were `False`.
    
- **`else`**: The default block that executes only if **all** preceding conditions evaluate to `False`.
    

### f-strings (Modern & Readable)

Allows you to embed Python expressions directly inside string literals using curly braces `{}`.

Python

```py
name = "Alice"

# Harder to read (string concatenation): 
print("Hello " + name + "!") 

# Cleaner and faster (f-string): 
print(f"Hello {name}!")
```

## 2. [Alphabet Game](./print_alphabt.py)

Prints lowercase letters `a` through `z` while skipping the letters `e` (ASCII 101) and `q` (ASCII 113).

Python

```py
for i in range(97, 123):
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end="")
```

### Breakdown:

- **`range(97, 123)`**: Generates ASCII decimal numbers from `97` (`'a'`) up to `122` (`'z'`).
    
- **`i != 101 and i != 113`**: Excludes `'e'` (101) and `'q'` (113).
    
- **`chr(i)`**: Converts an ASCII integer back to its character equivalent (e.g., `chr(97)` $\rightarrow$ `'a'`).
    
- **`end=""`**: Overrides the default newline behavior (`\n`), printing characters continuously on a single line.
    

## 3. [Hexadecimal Printing](./print_hexa.py)

Loops through numbers `0` to `98` and prints their decimal and lowercase hexadecimal values.

Python

```py
for i in range(99):
    print("{} = 0x{:x}".format(i, i))
```

### Breakdown:

- **`range(99)`**: Generates numbers from `0` to `98`.
    
- **`"{}"`**: First placeholder receives the standard decimal value `i`.
    
- **`"0x"`**: Literal string prefix for hexadecimal notation.
    
- **`"{:x}"`**: Format specifier converting the second value `i` into lowercase hexadecimal (e.g., `10` $\rightarrow$ `a`).
    

## 4. [Number Formatting with Leading Zeros (`00`–`99`)](./print_comb2.py)

Prints numbers from `00` to `99` separated by commas, with no trailing comma after `99`.

Python

```py
for i in range(100):
    if i < 99:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(i))
```

### Breakdown:

- **`range(100)`**: Loops 100 times, from `0` to `99`.
    
- **`{:02d}`**: Format specifier breakdown:
    
    - `d`: Decimal integer.
        
    - `2`: Minimum field width of 2 characters.
        
    - `0`: Pads single-digit numbers with a leading zero (e.g., `7` $\rightarrow$ `07`).
        
- **`end=", "`**: Replaces the standard newline with a comma and space to keep output on one line.
    
- **`else:`**: Executes only on the final iteration (`i = 99`) to print without a trailing comma.

## 5. [Combination of Two Digits](./print_comb3.py)

Python

```py
for i in range(10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
```

### 1. Outer Loop (`for i in range(10)`)

- Controls the **first digit** ($i$), which goes from `0` to `9`.
    

### 2. Inner Loop (`for j in range(i + 1, 10)`)

- Controls the **second digit** ($j$).
    
- Starting `j` at `i + 1` satisfies two rules automatically:
    
    1. **Digits are different:** $j$ is strictly greater than $i$ ($i < j$), so pairs like `00` or `11` are never generated.
        
    2. **No repeated combinations:** Since $i$ is always smaller than $j$, combinations like `10` are skipped because `01` was already printed when $i=0$ and $j=1$.
        

### 3. Output Formatting (`if/else`)

- **`else` branch:** For all combinations except the last one, `print("{}{}".format(i, j), end=", ")` prints the two digits glued together followed by a comma and space `,` .
    
- **`if i == 8 and j == 9:` branch:** When the loop reaches the final combination (`89`), `print("{}{}".format(i, j))` prints without `end=", "`, ensuring there is no trailing comma at the end of the output.
    

### Output

```
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
```


