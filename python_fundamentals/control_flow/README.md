## Control Flow

0. Positive anything is better than negative nothing


1. The last digit
```py
if - The first line of argument statment that checks for a TRUE value
elif - The continous line after the if statment with other arguments.
else - if all statements are FALSE else will be executed

f-strings
allows you to embed Python variables or expressions directly inside a string using curly braces {}
Python automatically replaces {variable_name} with its actual value when printing

name = "Alice"

# Using concatenation (harder to read): 
print("Hello " + name + "!") 

# Using an f-string (cleaner and easier to write): 
print(f"Hello {name}!")

```


2. Alphabet Game (Lowercase)
```py
for i in range(97, 123): # generates a sequence of numbers from 97 to 122 (123 is exculded)

ASCII table: 
			97 = a
			122 = z
for loop executes the block once for each value

if i != 101 and i != 113:
ASCII table: 
			101 = e
			122 = q
!= this will exclude i and q

print("{}".format(chr(i)), end="")

chr(i) Converts the ASCII integer back into its character representation (e.g. chr(97) becomes a)

"{}".format(...) Formats the character into a string using standard Python string formatting

end="": Overrides the default `print()` behavior (which adds a newline `\n` after every call) so that each character prints continuously on the same line.

```

3. Hexadecimal Printing
```py
for i in range(99):
# range(99) generates a sequence of numbers starting at 0 and ending at 98
# for i in ... loops through each number one by one, assigning the current number to the variable i

print("{} = 0x{:x}".format(i, i))
# "{} = 0x{:x}" Template string containing 2 placeholders defined by {}
# first {} inserts value passed to the .format() as a standard number
# 0x prints as is
# Second {:x} the :x is a format specifier. This coverts the value into lower hex number
# .format(i, i) Takes the variable i twice and place it into two placeholders, first i goes in the {} and the 2nd i goes into {:x} 
```

