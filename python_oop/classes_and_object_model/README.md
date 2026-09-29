# Python - Classes and Object Model

This project introduces the basics of **Object-Oriented Programming (OOP)** in Python.

The exercises start with very simple classes and gradually add more features. The main example is a `Square` class, followed by a `Rectangle` class.

The goal is to understand how Python classes and objects work and how we can use them to organise data and behaviour.

---

## What is Object-Oriented Programming?

**Object-Oriented Programming**, usually called **OOP**, is a way of writing programs using **objects**.

An object can contain:

* **Attributes** — information stored inside the object
* **Methods** — functions that the object can perform

For example, if we create a `Square`, it could have:

```python
size
```

as an attribute.

It could also have:

```python
area()
my_print()
```

as methods.

We can think about it like this:

```text
Square object
│
├── Data
│   └── size
│
└── Actions
    ├── area()
    └── my_print()
```

---

# Classes and Objects

## What is a class?

A **class** is like a blueprint.

For example:

```python
class Square:
    pass
```

This creates a class called `Square`.

The class describes what a square object can be, but it doesn't create a particular square yet.

---

## What is an object?

An **object** is an instance of a class.

For example:

```python
my_square = Square()
```

Here:

```text
Square     → class
my_square  → object
```

We can create many objects from the same class:

```python
square_1 = Square()
square_2 = Square()
square_3 = Square()
```

All three objects are created from the `Square` class, but each object can contain different information.

---

# The Square Exercises

The `Square` exercises build on each other.

The progression is:

```text
0-square.py
     ↓
1-square.py
     ↓
2-square.py
     ↓
3-square.py
     ↓
4-square.py
     ↓
5-square.py
     ↓
6-square.py
```

Each exercise adds another OOP concept.

---

# 0-square.py

## Creating an empty class

The first exercise contains:

```python
class Square:
    pass
```

At this point, `Square` doesn't do anything.

The `pass` statement means:

> "There is nothing else to do here yet."

We can still create an object:

```python
my_square = Square()
```

But the object doesn't have any special attributes or methods.

### What this exercise teaches

The main idea is simply learning how to create a **class**.

```text
class
  ↓
Square
  ↓
object
```

---

# 1-square.py

## Adding an attribute

The next exercise introduces `__init__`:

```python
def __init__(self, size):
    self.__size = size
```

Now a square can have a size.

For example:

```python
my_square = Square(5)
```

The square now has a size of `5`.

---

## What is `__init__`?

`__init__` is a special method that Python automatically calls when an object is created.

When we write:

```python
my_square = Square(5)
```

Python calls:

```python
__init__
```

and gives it the value `5`.

---

## What is `self`?

`self` refers to the **current object**.

This line:

```python
self.__size = size
```

means:

> Store the value of `size` inside this particular square object.

For example:

```python
square_1 = Square(5)
square_2 = Square(10)
```

The objects can contain different values:

```text
square_1
└── size = 5

square_2
└── size = 10
```

---

## Why `__size` has two underscores

Your code uses:

```python
self.__size
```

The double underscore is used for **name mangling**.

It makes the attribute harder to access directly from outside the class.

Instead of directly working with the internal attribute, later exercises introduce a `size` property that gives us a controlled way to access it.

---

# 2-square.py

## Adding validation

The second Square exercise adds validation.

Your constructor is:

```python
def __init__(self, size=0):
```

This means the default size is `0`.

For example:

```python
square = Square()
```

creates a square with a size of `0`.

You can also provide a size:

```python
square = Square(5)
```

---

## Checking the type

Your code checks:

```python
if type(size) is not int:
    raise TypeError("size must be an integer")
```

This makes sure `size` is an integer.

For example:

```python
Square(5)
```

is valid.

But:

```python
Square("5")
```

causes a `TypeError`.

The program raises:

```text
TypeError: size must be an integer
```

---

## Checking the value

Your code also checks:

```python
if size < 0:
    raise ValueError("size must be >= 0")
```

A square cannot have a negative size in this exercise.

Therefore:

```python
Square(-5)
```

causes:

```text
ValueError: size must be >= 0
```

---

## `TypeError` vs `ValueError`

These are two important Python exceptions.

### TypeError

The value has the **wrong type**.

Example:

```python
Square("hello")
```

The program expected an integer but received a string.

### ValueError

The type is correct, but the **value is not acceptable**.

Example:

```python
Square(-5)
```

`-5` is an integer, but it is not an acceptable size.

---

# 3-square.py

## Adding a method

The next exercise introduces:

```python
def area(self):
    return self.__size ** 2
```

This calculates the area of the square.

The formula for a square is:

```text
area = size × size
```

For example, if:

```python
square = Square(4)
```

then:

```python
square.area()
```

returns:

```text
16
```

because:

```text
4 × 4 = 16
```

---

## What is a method?

A method is a function that belongs to a class.

For example:

```python
def area(self):
```

is a method of the `Square` class.

We call it using the object:

```python
square.area()
```

Think of it like this:

```text
Square
│
├── size
│
└── area()
       ↓
    calculates
       ↓
      area
```

---

# 4-square.py

## Adding properties

This exercise introduces:

```python
@property
```

and:

```python
@size.setter
```

These allow us to control how the `size` attribute is accessed and changed.

---

## The getter

Your code contains:

```python
@property
def size(self):
    return self.__size
```

This allows us to read the size using:

```python
square.size
```

instead of accessing:

```python
square.__size
```

directly.

---

## The setter

Your code contains:

```python
@size.setter
def size(self, value):
```

The setter controls what happens when we try to change the size.

For example:

```python
square.size = 5
```

Python calls the setter.

The setter then checks:

```python
if type(value) is not int:
```

and:

```python
if value < 0:
```

before storing the value.

---

## Why use a property?

A property lets us control access to an attribute.

Without validation, someone could potentially do:

```python
square.size = -10
```

The setter prevents this.

The process becomes:

```text
square.size = 5
       ↓
size setter
       ↓
Is it an integer?
       ↓
Is it >= 0?
       ↓
Store the value
```

This is an important OOP idea called **encapsulation**.

---

# 5-square.py

## Printing the square

This exercise adds:

```python
def my_print(self):
```

The method prints the square using the `#` character.

For example:

```python
square = Square(4)
square.my_print()
```

produces:

```text
####
####
####
####
```

The size determines both the number of rows and the number of `#` characters in each row.

---

## The `range()` loop

Your code contains:

```python
for _ in range(self.__size):
```

If the size is `4`, this loop runs four times.

Each time it prints:

```python
"#" * self.__size
```

`"#" * 4` produces:

```text
####
```

So the result becomes:

```text
####
####
####
####
```

---

## Why `_`?

The variable:

```python
_
```

is commonly used when we don't actually need the loop number.

For example:

```python
for _ in range(4):
```

means:

> Repeat this four times.

We don't care whether the current loop is `0`, `1`, `2`, or `3`.

---

## What happens when the size is 0?

Your method checks:

```python
if self.__size == 0:
    print()
    return
```

Instead of trying to print a square with zero rows, it simply prints a blank line and stops the method.

---

# 6-square.py

## Adding a position

The final Square exercise adds another attribute:

```python
position
```

The constructor is now:

```python
def __init__(self, size=0, position=(0, 0)):
```

A square now has:

```text
size
position
```

For example:

```python
square = Square(3, (2, 1))
```

---

# Understanding `(x, y)`

The position is represented by a tuple:

```python
(x, y)
```

The first number controls the horizontal position.

The second number controls the vertical position.

For example:

```python
position = (2, 1)
```

means:

```text
x = 2
y = 1
```

Your `my_print()` method uses:

```python
self.__position[0]
```

for the horizontal position.

It uses:

```python
self.__position[1]
```

for the vertical position.

---

## Position validation

Your setter checks that the position:

1. Is a tuple
2. Contains exactly two values
3. Contains integers
4. Contains values that are not negative

The expected structure is:

```python
(x, y)
```

For example:

```python
(2, 3)
```

is valid.

---

## Printing with a position

Your code uses:

```python
print("\n" * self.__position[1], end="")
```

This adds vertical space before printing the square.

It also uses:

```python
" " * self.__position[0]
```

to add spaces before each row.

For example, the square:

```text
###
###
###
```

can be moved to the right by adding spaces:

```text
  ###
  ###
  ###
```

---

# `__str__`

The final Square exercise also introduces:

```python
def __str__(self):
```

`__str__` is a special Python method.

It controls what happens when we convert an object to a string or print it.

For example:

```python
print(square)
```

can use the `__str__` method to decide what should be displayed.

---

## Difference between `my_print()` and `__str__()`

Your class contains both:

```python
my_print()
```

and:

```python
__str__()
```

They have different purposes.

### `my_print()`

It directly prints the square:

```python
square.my_print()
```

### `__str__()`

It creates and returns the string representation:

```python
print(square)
```

The important difference is that `__str__()` **returns a string**, while `my_print()` directly prints to the screen.

---

# The Rectangle Exercises

After learning about squares, the project introduces a `Rectangle` class.

There are currently two Rectangle exercises:

```text
1-rectangle.py
2-rectangle.py
```

The Rectangle exercises use many of the same OOP ideas learned with `Square`.

---

# 1-rectangle.py

## Creating a Rectangle

The class is:

```python
class Rectangle:
```

A rectangle has two important attributes:

```text
width
height
```

The constructor is:

```python
def __init__(self, width=0, height=0):
```

Both values default to `0`.

For example:

```python
rectangle = Rectangle(5, 3)
```

creates a rectangle with:

```text
width  = 5
height = 3
```

---

## Width and height properties

The class has a property for `width`:

```python
@property
def width(self):
    return self.__width
```

and a setter:

```python
@width.setter
def width(self, value):
```

The same approach is used for `height`.

This allows the class to validate the values.

---

## Width validation

The setter checks:

```python
if type(value) is not int:
    raise TypeError("width must be an integer")
```

and:

```python
if value < 0:
    raise ValueError("width must be >= 0")
```

The height setter does the same thing.

This means the rectangle cannot be created with invalid width or height values.

---

# 2-rectangle.py

## Calculating the area

The `Rectangle` class now contains:

```python
def area(self):
    return self.width * self.height
```

The formula is:

```text
area = width × height
```

For example:

```python
rectangle = Rectangle(5, 3)
print(rectangle.area())
```

produces:

```text
15
```

because:

```text
5 × 3 = 15
```

---

# Calculating the perimeter

The class also contains:

```python
def perimeter(self):
    if self.width == 0 or self.height == 0:
        return 0
    return 2 * (self.width + self.height)
```

The normal rectangle perimeter formula is:

```text
perimeter = 2 × (width + height)
```

For example:

```text
width  = 5
height = 3

perimeter = 2 × (5 + 3)
          = 2 × 8
          = 16
```

So:

```python
rectangle = Rectangle(5, 3)
print(rectangle.perimeter())
```

returns:

```text
16
```

---

## Why check for zero?

Your code contains:

```python
if self.width == 0 or self.height == 0:
    return 0
```

This follows the exercise requirement.

If either dimension is `0`, the perimeter returned by the method is:

```text
0
```

For example:

```python
rectangle = Rectangle(5, 0)
print(rectangle.perimeter())
```

returns:

```text
0
```

---

# Important Python Concepts Learned

By working through these files, you are learning several important Python concepts.

## 1. Classes

A class creates a blueprint for objects.

```python
class Square:
    pass
```

---

## 2. Objects

An object is an instance of a class.

```python
square = Square()
```

---

## 3. Attributes

Attributes store information about an object.

```python
self.__size = size
```

---

## 4. Methods

Methods are functions that belong to a class.

```python
def area(self):
```

---

## 5. `self`

`self` refers to the current object.

```python
self.__size
```

---

## 6. `__init__`

`__init__` runs when an object is created.

```python
def __init__(self, size=0):
```

---

## 7. Properties

Properties allow us to control how attributes are accessed.

```python
@property
```

---

## 8. Setters

Setters allow us to control what happens when an attribute is changed.

```python
@size.setter
```

---

## 9. Exceptions

Exceptions allow us to report invalid values.

```python
raise TypeError(...)
```

and:

```python
raise ValueError(...)
```

---

## 10. Special methods

Python provides special methods such as:

```python
__init__()
__str__()
```

These methods have special meanings to Python.

---

# How the Project Builds Up

The most important thing to notice is that the exercises gradually add functionality.

```text
0-square.py
│
└── Create an empty class
        ↓
1-square.py
│
└── Add size
        ↓
2-square.py
│
└── Validate size
        ↓
3-square.py
│
└── Add area()
        ↓
4-square.py
│
└── Add property and setter
        ↓
5-square.py
│
└── Add my_print()
        ↓
6-square.py
│
└── Add position and __str__()
        ↓
1-rectangle.py
│
└── Create Rectangle with width/height
        ↓
2-rectangle.py
│
└── Add area() and perimeter()
```

This progression is important because each exercise builds on the ideas from the previous one.

---

# Example: Following a Square Through the Code

Suppose we write:

```python
square = Square(4)
```

We can follow what happens.

### Step 1 — Create the object

Python creates a new `Square` object.

### Step 2 — Call `__init__`

Python runs:

```python
__init__(4)
```

### Step 3 — Set the size

The setter checks that `4` is a valid integer.

Then:

```python
self.__size = 4
```

stores the value.

### Step 4 — Calculate the area

If we run:

```python
square.area()
```

Python calculates:

```text
4 ** 2
```

which gives:

```text
16
```

### Step 5 — Print the square

If we run:

```python
square.my_print()
```

the result is:

```text
####
####
####
####
```

So the overall process is:

```text
Square(4)
    ↓
__init__()
    ↓
size setter
    ↓
__size = 4
    ↓
area()
    ↓
4 × 4
    ↓
16
```

---

# Running the Code

Each Python file can be executed using Python 3.

For example:

```bash
python3 3-square.py
```

The exercise files are classes, so they are normally tested by another Python file that imports the class.

For example:

```python
Square = __import__('3-square').Square

my_square = Square(4)

print(my_square.area())
```

This creates a `Square` object from `3-square.py` and calls its `area()` method.

---

# Things to Remember

When learning classes, these are the most important ideas to remember:

### A class is a blueprint

```python
class Square:
```

### An object is created from the class

```python
square = Square(4)
```

### `self` refers to the object

```python
self.__size
```

### `__init__` sets up the object

```python
def __init__(self, size=0):
```

### Methods give the object behaviour

```python
def area(self):
```

### Properties control access to attributes

```python
@property
```

### Setters allow validation

```python
@size.setter
```

### Exceptions handle invalid input

```python
raise TypeError(...)
raise ValueError(...)
```

---

# Project Summary

This directory is an introduction to **Python Object-Oriented Programming**.

The exercises begin with a very simple class and gradually introduce more functionality.

By the end of the exercises, the `Square` class can:

* Store a size
* Validate the size
* Calculate its area
* Print itself
* Have a position
* Return a string representation

The `Rectangle` class can:

* Store a width
* Store a height
* Validate both values
* Calculate its area
* Calculate its perimeter

The main lesson is that a class can combine **data and behaviour** into one object.

```text
              CLASS
                │
                ↓
              OBJECT
                │
        ┌───────┴───────┐
        ↓               ↓
    Attributes        Methods
        │               │
     size            area()
     width         perimeter()
    height         my_print()
    position
```

Understanding these concepts provides the foundation for more advanced Python topics such as **inheritance, polymorphism, abstraction, and larger object-oriented programs**.

