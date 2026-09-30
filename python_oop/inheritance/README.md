# Python - Inheritance

This project introduces **inheritance** in Python.

Inheritance is an important part of **Object-Oriented Programming (OOP)**.

The exercises in this directory build on the classes and objects learned in the previous OOP exercises.

Instead of creating every class completely from scratch, inheritance allows one class to **reuse code from another class**.

The project starts with a basic geometry class and then builds:

```text
BaseGeometry
     │
     ↓
 Rectangle
     │
     ↓
  Square
```

This lets us see how classes can be connected together.

---

# What is Inheritance?

Inheritance allows a new class to use functionality that already exists in another class.

Think of it like a family tree.

For example:

```text
        Animal
          │
          ├──────────┐
          ↓          ↓
        Dog        Cat
```

`Dog` and `Cat` can inherit functionality from `Animal`.

The original class is called the **parent class**, **base class**, or **superclass**.

The class that inherits from it is called the **child class**, **subclass**, or **derived class**.

In this project:

```text
BaseGeometry
     │
     ↓
 Rectangle
     │
     ↓
 Square
```

So:

* `BaseGeometry` is the parent of `Rectangle`
* `Rectangle` is the child of `BaseGeometry`
* `Rectangle` is also the parent of `Square`
* `Square` is the child of `Rectangle`

---

# Files in This Directory

The inheritance exercises contain:

```text
base_geometry.py
1-rectangle.py
2-rectangle.py
1-square.py
2-square.py
```

The exercises gradually build on each other.

The overall progression is:

```text
BaseGeometry
     │
     │ provides validation
     ↓
Rectangle
     │
     │ adds area and string representation
     ↓
Square
     │
     │ reuses Rectangle
     ↓
Square with its own __str__()
```

---

# 1. Base Geometry

## `base_geometry.py`

This file creates the `BaseGeometry` class.

The class is:

```python
class BaseGeometry:
```

A **base class** is often used to provide common functionality that other classes can reuse.

In this project, `BaseGeometry` provides two important things:

```text
BaseGeometry
│
├── area()
│
└── integer_validator()
```

---

# The `area()` Method

The class contains:

```python
def area(self):
    raise Exception("area() is not implemented")
```

At first, this might seem strange.

Why create an `area()` method if it doesn't calculate an area?

The reason is that `BaseGeometry` is a general geometry class.

Different shapes have different formulas for calculating area.

For example:

```text
Rectangle
area = width × height

Square
area = size × size

Circle
area = π × radius²
```

The base class doesn't know which formula should be used.

So instead, it says:

> Every geometry class should have an `area()` method, but the specific shape must provide the actual calculation.

The method therefore raises:

```python
Exception("area() is not implemented")
```

This is a way of saying:

> "This method exists, but this class doesn't provide an implementation for it."

---

# The `integer_validator()` Method

The second method is:

```python
def integer_validator(self, name, value):
```

This method checks that a value is a valid positive integer.

It takes two arguments:

```text
name
value
```

For example:

```python
self.integer_validator("width", width)
```

Here:

```text
name  → "width"
value → width
```

The `name` is used when creating an error message.

---

# Checking the Type

The first check is:

```python
if type(value) is not int:
    raise TypeError(f"{name} must be an integer")
```

This asks:

> Is `value` an integer?

For example:

```python
5
```

is an integer.

But:

```python
"5"
```

is a string.

So:

```python
self.integer_validator("width", "5")
```

raises:

```text
TypeError: width must be an integer
```

---

# Checking the Value

The next check is:

```python
if value <= 0:
    raise ValueError(f"{name} must be greater than 0")
```

This makes sure the integer is greater than zero.

For example:

```python
5
```

is valid.

But:

```python
0
```

is not.

And:

```python
-5
```

is not.

These values cause a `ValueError`.

---

# Why Put Validation in BaseGeometry?

This is one of the important ideas behind inheritance.

Instead of writing the same validation code in every shape:

```python
if type(width) is not int:
    ...
```

```python
if type(height) is not int:
    ...
```

```python
if type(size) is not int:
    ...
```

we can write the validation once:

```python
integer_validator()
```

Then other classes can reuse it.

This is one of the benefits of inheritance:

> **Write common functionality once and reuse it.**

---

# 2. Rectangle

## `1-rectangle.py`

The next exercise creates a `Rectangle` class.

The important line is:

```python
class Rectangle(BaseGeometry):
```

This is where inheritance is introduced.

It means:

```text
Rectangle
    ↓ inherits from
BaseGeometry
```

Because `Rectangle` inherits from `BaseGeometry`, it can use methods from `BaseGeometry`.

That means the Rectangle can use:

```python
self.integer_validator(...)
```

even though `integer_validator()` is not written inside the Rectangle class.

---

# Importing BaseGeometry

The file contains:

```python
BaseGeometry = __import__('0-base_geometry').BaseGeometry
```

This loads the `BaseGeometry` class from another Python file.

The result is then assigned to:

```python
BaseGeometry
```

So Python can use it here:

```python
class Rectangle(BaseGeometry):
```

The important idea is:

```text
0-base_geometry.py
        │
        │ contains
        ↓
BaseGeometry
        │
        │ imported by
        ↓
1-rectangle.py
        │
        ↓
Rectangle
```

---

# Creating the Rectangle

The Rectangle constructor is:

```python
def __init__(self, width, height):
```

A rectangle needs two pieces of information:

```text
width
height
```

For example:

```python
rectangle = Rectangle(5, 3)
```

This creates a rectangle with:

```text
width  = 5
height = 3
```

---

# Validating the Width

The constructor calls:

```python
self.integer_validator("width", width)
```

Remember, `integer_validator()` comes from `BaseGeometry`.

Because `Rectangle` inherits from `BaseGeometry`, it can use that method.

The process looks like this:

```text
Rectangle(5, 3)
      │
      ↓
Check width
      │
      ↓
integer_validator()
      │
      ↓
Is 5 an integer?
      │
      ↓
Is 5 greater than 0?
      │
      ↓
Valid
```

---

# Storing the Width

After validation:

```python
self.__width = width
```

stores the width inside the object.

The double underscore:

```python
__width
```

makes this an internal/private-style attribute through Python's name-mangling mechanism.

The same process happens for height:

```python
self.integer_validator("height", height)
self.__height = height
```

---

# Rectangle Object

If we create:

```python
rectangle = Rectangle(5, 3)
```

the object can be thought of like this:

```text
rectangle
│
├── __width  → 5
└── __height → 3
```

And because it inherits from `BaseGeometry`, it also has access to:

```text
integer_validator()
area()
```

Although the inherited `area()` method has not yet been replaced by Rectangle.

---

# 3. Rectangle with Area

## `2-rectangle.py`

The next exercise builds on the previous Rectangle.

It still inherits from:

```python
BaseGeometry
```

but now it adds an `area()` method.

```python
def area(self):
    return self.__width * self.__height
```

---

# Calculating Rectangle Area

The formula for a rectangle is:

```text
area = width × height
```

For example:

```python
rectangle = Rectangle(5, 3)
```

The area is:

```text
5 × 3 = 15
```

So:

```python
print(rectangle.area())
```

produces:

```text
15
```

---

# Method Overriding

This is an important inheritance concept.

`BaseGeometry` already has:

```python
def area(self):
    raise Exception("area() is not implemented")
```

But `Rectangle` creates its own:

```python
def area(self):
    return self.__width * self.__height
```

The Rectangle's version **overrides** the version inherited from `BaseGeometry`.

So when we call:

```python
rectangle.area()
```

Python uses the Rectangle's version.

Think of it like:

```text
BaseGeometry
│
└── area()
      │
      │ originally not implemented
      ↓
Rectangle
│
└── area()
      │
      └── width × height
```

This allows the child class to provide behaviour that is specific to that type of object.

---

# The Rectangle `__str__()` Method

The Rectangle also defines:

```python
def __str__(self):
    return "[Rectangle] {}/{}".format(
        self.__width,
        self.__height
    )
```

`__str__()` is a special Python method.

It controls what the object looks like when we print it.

For example:

```python
rectangle = Rectangle(5, 3)
print(rectangle)
```

produces:

```text
[Rectangle] 5/3
```

The `/` separates the width and height.

---

# Why Use `__str__()`?

Without a custom `__str__()` method, printing an object normally produces something similar to:

```text
<Rectangle object at 0x...>
```

That doesn't tell us much.

By creating:

```python
def __str__(self):
```

we can tell Python exactly what information should be displayed.

---

# 4. Square

## `1-square.py`

The next exercise introduces a `Square`.

The important line is:

```python
class Square(Rectangle):
```

This means:

```text
Square
   ↓ inherits from
Rectangle
   ↓ inherits from
BaseGeometry
```

So the inheritance chain becomes:

```text
BaseGeometry
      │
      ↓
 Rectangle
      │
      ↓
   Square
```

This is a very important example of **multi-level inheritance**.

---

# Why Does Square Inherit from Rectangle?

A square is a special type of rectangle.

A rectangle can have:

```text
width  = 5
height = 3
```

A square must have:

```text
width  = 5
height = 5
```

The two sides are always equal.

Instead of rewriting all the Rectangle functionality, the Square can reuse it.

For example:

```python
super().__init__(size, size)
```

sets:

```text
width  = size
height = size
```

---

# Understanding `super()`

This is one of the most important parts of the exercise.

The code contains:

```python
super().__init__(size, size)
```

`super()` allows a child class to call functionality from its parent class.

In this case:

```text
Square
  │
  │ super()
  ↓
Rectangle
```

So when Square runs:

```python
super().__init__(size, size)
```

it is asking the Rectangle's constructor to run.

The Rectangle receives:

```text
width  = size
height = size
```

---

# Example of `super()`

Suppose:

```python
square = Square(5)
```

The Square constructor receives:

```text
size = 5
```

Then:

```python
super().__init__(size, size)
```

effectively sends:

```text
width  = 5
height = 5
```

to the Rectangle constructor.

The process is:

```text
Square(5)
   │
   ↓
Square.__init__()
   │
   ↓
super().__init__(5, 5)
   │
   ↓
Rectangle.__init__()
   │
   ├── width = 5
   └── height = 5
```

This means Square can reuse the Rectangle's existing validation and setup code.

---

# Validating the Square Size

Before calling `super()`, Square runs:

```python
self.integer_validator("size", size)
```

Remember that `integer_validator()` comes from `BaseGeometry`.

Because:

```text
Square
  ↓
Rectangle
  ↓
BaseGeometry
```

Square can access the inherited method.

The process is:

```text
Square(5)
   ↓
integer_validator()
   ↓
Is 5 an integer?
   ↓
Is 5 greater than 0?
   ↓
Valid
```

---

# Why Store `__size`?

The Square also stores:

```python
self.__size = size
```

This gives the Square its own size attribute.

The Rectangle parent class is storing:

```text
__width
__height
```

while Square stores:

```text
__size
```

So conceptually:

```text
Square
│
├── __size
│
└── inherited Rectangle functionality
    ├── __width
    └── __height
```

The Square can therefore keep track of its own size while using Rectangle functionality.

---

# 5. Square with `__str__()`

## `2-square.py`

The final exercise adds a `__str__()` method to the Square.

The Square still inherits from Rectangle:

```python
class Square(Rectangle):
```

and still uses:

```python
super().__init__(size, size)
```

But now it provides its own string representation.

---

# Square `__str__()`

The method is:

```python
def __str__(self):
    return "[Square] {}/{}".format(
        self.__size,
        self.__size
    )
```

If we create:

```python
square = Square(5)
```

and run:

```python
print(square)
```

the result is:

```text
[Square] 5/5
```

---

# Overriding `__str__()`

The Rectangle parent already has a `__str__()` method:

```python
return "[Rectangle] {}/{}".format(
    self.__width,
    self.__height
)
```

But Square provides its own version.

This is another example of **method overriding**.

The inheritance relationship is:

```text
Rectangle
│
└── __str__()
       │
       ↓
Square
│
└── __str__()
```

When we print a Square, Python uses the Square's version.

---

# Rectangle vs Square

The two classes are related:

```text
        BaseGeometry
             │
             ↓
         Rectangle
             │
             ↓
           Square
```

The Rectangle has:

```text
width
height
area()
__str__()
```

The Square has:

```text
size
area()        ← inherited through Rectangle
__str__()     ← its own version
```

Because a square has equal width and height, Square can call:

```python
super().__init__(size, size)
```

instead of writing the Rectangle setup again.

---

# Understanding the Whole Project

The easiest way to understand the project is to follow the inheritance chain.

```text
                    BaseGeometry
                         │
             ┌───────────┴───────────┐
             │                       │
      integer_validator()           area()
             │
             │ inherited by
             ↓
         Rectangle
             │
       ┌─────┴─────┐
       │           │
   width/height   area()
       │           │
       │         __str__()
       │
       │ inherited by
       ↓
      Square
       │
       ├── size
       │
       ├── inherited area()
       │
       └── own __str__()
```

---

# Important OOP Concepts

This directory introduces several important concepts.

## 1. Parent Class

A parent class provides functionality that another class can inherit.

Example:

```python
class Rectangle(BaseGeometry):
```

`BaseGeometry` is the parent.

---

## 2. Child Class

A child class inherits from another class.

Example:

```python
class Square(Rectangle):
```

`Square` is the child.

---

## 3. Inheritance

Inheritance allows a class to reuse functionality from another class.

```text
BaseGeometry
      ↓
Rectangle
      ↓
Square
```

---

## 4. Method Overriding

A child class can replace a method inherited from its parent.

For example:

```python
class Rectangle(BaseGeometry):
    def area(self):
        return self.__width * self.__height
```

Rectangle replaces the generic `BaseGeometry.area()` method with its own implementation.

Square then provides its own `__str__()` method instead of using Rectangle's version.

---

## 5. `super()`

`super()` allows a child class to call a method from its parent.

Example:

```python
super().__init__(size, size)
```

This allows Square to reuse Rectangle's constructor.

---

## 6. Code Reuse

One of the biggest advantages of inheritance is avoiding duplicate code.

Without inheritance, Square would need to write its own validation and rectangle setup.

Instead, it can use:

```python
self.integer_validator(...)
```

and:

```python
super().__init__(size, size)
```

The existing code does the work.

---

## 7. Encapsulation

The classes use double underscores:

```python
self.__width
self.__height
self.__size
```

These are intended to keep implementation details internal to the class.

This helps control how the data is used.

---

# Understanding the Exceptions

The project uses two important exceptions.

## `TypeError`

A `TypeError` is raised when the value has the wrong type.

For example:

```python
Rectangle("5", 3)
```

The width should be an integer, but `"5"` is a string.

The result is:

```text
TypeError: width must be an integer
```

---

## `ValueError`

A `ValueError` is raised when the type is correct but the value is not acceptable.

For example:

```python
Rectangle(-5, 3)
```

`-5` is an integer, but it is not greater than zero.

The result is:

```text
ValueError: width must be greater than 0
```

---

# Following a Square Through the Program

Let's follow:

```python
square = Square(5)
```

step by step.

### Step 1 — Create the Square

Python sees:

```python
Square(5)
```

and starts the Square constructor.

---

### Step 2 — Validate the size

Square calls:

```python
self.integer_validator("size", size)
```

The method comes from `BaseGeometry`.

It checks:

```text
Is 5 an integer?
        ↓
      Yes

Is 5 greater than 0?
        ↓
      Yes
```

The value is valid.

---

### Step 3 — Call the parent constructor

Square runs:

```python
super().__init__(size, size)
```

Because `size` is `5`, this becomes:

```text
Rectangle.__init__(5, 5)
```

---

### Step 4 — Rectangle validates the width

Rectangle calls:

```python
self.integer_validator("width", width)
```

`5` passes validation.

Then:

```python
self.__width = 5
```

---

### Step 5 — Rectangle validates the height

Rectangle calls:

```python
self.integer_validator("height", height)
```

Again, `5` passes.

Then:

```python
self.__height = 5
```

---

### Step 6 — Square stores its size

Square then stores:

```python
self.__size = size
```

So the object now represents a square with a side length of `5`.

---

### Step 7 — Calculate the area

Because Square inherits from Rectangle, it can use Rectangle's:

```python
area()
```

The calculation is:

```text
width × height

5 × 5

= 25
```

---

### Step 8 — Print the Square

The final Square has its own `__str__()` method.

So:

```python
print(square)
```

produces:

```text
[Square] 5/5
```

---

# Visual Flow

The whole process can be represented like this:

```text
                 Square(5)
                     │
                     ↓
             Square.__init__()
                     │
                     ↓
          integer_validator()
                     │
                     ↓
                size = 5
                     │
                     ↓
       super().__init__(5, 5)
                     │
                     ↓
            Rectangle.__init__()
                     │
             ┌───────┴───────┐
             ↓               ↓
          width = 5       height = 5
             │               │
             └───────┬───────┘
                     ↓
                  Square
                     │
             ┌───────┴────────┐
             ↓                ↓
          area()            __str__()
             │                │
             ↓                ↓
          25             [Square] 5/5
```

---

# How the Files Build on Each Other

The exercises follow a logical progression.

```text
base_geometry.py
│
├── Create BaseGeometry
├── Create area()
└── Create integer_validator()
          │
          ↓
1-rectangle.py
│
├── Inherit BaseGeometry
├── Create Rectangle
├── Validate width
└── Validate height
          │
          ↓
2-rectangle.py
│
├── Keep Rectangle
├── Add area()
└── Add __str__()
          │
          ↓
1-square.py
│
├── Inherit Rectangle
├── Validate size
├── Use super()
└── Create a Square
          │
          ↓
2-square.py
│
└── Add Square's own __str__()
```

Each exercise adds a new idea without throwing away the ideas from the previous exercise.

---

# Key Things to Remember

If you are new to programming, these are the most important ideas to take away from this project.

### A parent class provides functionality

```python
class Rectangle(BaseGeometry):
```

Rectangle gets functionality from BaseGeometry.

---

### A child class can reuse its parent's methods

```python
self.integer_validator(...)
```

Rectangle and Square can use the method from BaseGeometry.

---

### A child can add its own methods

Rectangle adds:

```python
area()
```

and:

```python
__str__()
```

---

### A child can replace an inherited method

This is called **method overriding**.

For example, Square creates its own:

```python
__str__()
```

instead of using Rectangle's version.

---

### `super()` lets a child use the parent's implementation

```python
super().__init__(size, size)
```

lets Square reuse Rectangle's constructor.

---

# A Simple Real-World Example

Think about the classes as different types of vehicles.

You might have:

```text
Vehicle
  │
  ├── Car
  │
  └── Motorcycle
```

`Vehicle` could contain common functionality:

```text
start()
stop()
```

A `Car` could inherit those methods and add:

```text
open_trunk()
```

A `Motorcycle` could inherit them and add:

```text
kickstand()
```

The same idea is being used in this project:

```text
BaseGeometry
      │
      ↓
Rectangle
      │
      ↓
Square
```

The more specific class can reuse the functionality of the more general class.

---

# Summary

The main purpose of this project is to understand **inheritance in Python**.

The important relationship is:

```text
BaseGeometry
      ↓
Rectangle
      ↓
Square
```

`BaseGeometry` provides common geometry functionality such as validation.

`Rectangle` inherits that functionality and adds rectangle-specific behaviour such as calculating area.

`Square` inherits from `Rectangle` and reuses its functionality because a square can be represented as a rectangle where the width and height are equal.

The most important concepts introduced are:

* Classes
* Objects
* Parent classes
* Child classes
* Inheritance
* Method overriding
* `super()`
* Code reuse
* Encapsulation
* Special methods
* Exception handling
* Type validation
* Value validation

The key idea is:

> **Inheritance allows us to create a new class from an existing class and reuse its code.**

Instead of starting from nothing every time, we can build classes on top of classes:

```text
        BaseGeometry
             │
             │ common functionality
             ↓
         Rectangle
             │
             │ more specific functionality
             ↓
           Square
```

This is one of the foundations of Object-Oriented Programming in Python.

