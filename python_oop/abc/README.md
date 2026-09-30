# Python - Abstract Base Classes and Advanced OOP

This directory introduces several more advanced **Object-Oriented Programming (OOP)** concepts in Python.

The exercises build on the ideas learned in the previous OOP and inheritance exercises.

The main topics covered are:

* Abstract Base Classes (ABC)
* Abstract methods
* Polymorphism
* Duck typing
* Multiple inheritance
* Mixins
* Method overriding
* Using `super()`
* Extending built-in Python classes

The files in this directory are:

```text
abc/
├── animals.py
├── shapes.py
├── flyingfish.py
├── dragon.py
└── verboselist.py
```

The examples are different from each other, but they all demonstrate ways that classes can be designed to **share behaviour, require certain methods, or build new functionality from existing classes**.

---

# What is OOP?

**Object-Oriented Programming**, or **OOP**, is a way of organising programs using objects.

An object can contain:

* **Data** — information about the object
* **Methods** — actions the object can perform

For example, a `Dog` object might have:

```text
Dog
│
├── name
├── age
│
└── sound()
```

The attributes contain information, while the methods describe behaviour.

This directory goes one step further and looks at how different classes can work together.

---

# What is an Abstract Base Class?

An **Abstract Base Class**, often shortened to **ABC**, is a class that acts as a blueprint for other classes.

It can define methods that child classes **must implement**.

For example:

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

Here, `Animal` says:

> Every animal must have a `sound()` method.

However, `Animal` does not decide what sound every animal should make.

A dog can bark:

```text
Dog → Bark
```

A cat can meow:

```text
Cat → Meow
```

The parent class defines the requirement, while the child classes provide the actual behaviour.

---

# Why Use Abstract Classes?

Imagine we have many different shapes:

```text
Shape
├── Circle
├── Rectangle
├── Triangle
└── Square
```

All of these shapes can have:

```text
area()
perimeter()
```

Instead of hoping that every programmer remembers to create those methods, an abstract class can require them.

This creates a common structure:

```text
Shape
│
├── area()
└── perimeter()
       │
       ├── Circle
       ├── Rectangle
       └── Square
```

This makes larger programs easier to organise.

---

# `animals.py`

## What this file demonstrates

`animals.py` demonstrates:

* Abstract Base Classes
* Abstract methods
* Inheritance
* Method implementation
* Polymorphism

The class structure is:

```text
        Animal
        /    \
       /      \
     Dog      Cat
```

`Animal` is the abstract parent class.

`Dog` and `Cat` inherit from it.

---

# Importing ABC

At the top of the file we have:

```python
from abc import ABC, abstractmethod
```

Python provides the `abc` module for creating Abstract Base Classes.

We import two things:

```text
ABC
abstractmethod
```

`ABC` allows us to create an abstract base class.

`abstractmethod` allows us to mark a method as one that child classes must implement.

---

# The `Animal` Class

The class is:

```python
class Animal(ABC):
```

The `(ABC)` means that `Animal` is an Abstract Base Class.

Inside it we have:

```python
@abstractmethod
def sound(self):
    pass
```

This creates an **abstract method**.

---

# What is an Abstract Method?

An abstract method is a method that defines something a child class is expected to provide.

In this case:

```python
def sound(self):
```

says:

> Every type of Animal should have a `sound()` method.

But the Animal class doesn't know what sound the animal should make.

A dog and cat make different sounds.

So the child classes provide the implementation.

---

# The `@abstractmethod` Decorator

This line:

```python
@abstractmethod
```

is called a **decorator**.

It tells Python:

> This method is required for concrete child classes.

The structure is:

```text
Animal
│
└── sound()
      ↑
      │
      │ must be implemented
      │
 ┌────┴────┐
 ↓         ↓
Dog       Cat
```

---

# The Dog Class

The Dog class is:

```python
class Dog(Animal):
```

This means:

```text
Dog
 ↓
inherits from
 ↓
Animal
```

Dog then provides its own implementation of `sound()`:

```python
def sound(self):
    return "Bark"
```

So:

```python
dog = Dog()
print(dog.sound())
```

produces:

```text
Bark
```

---

# The Cat Class

Cat works in the same way:

```python
class Cat(Animal):
```

It inherits from `Animal`.

It implements:

```python
def sound(self):
    return "Meow"
```

So:

```python
cat = Cat()
print(cat.sound())
```

produces:

```text
Meow
```

---

# Why This Is Useful

The parent class doesn't need to know exactly what sound an animal makes.

It only establishes the rule:

```text
Every Animal must have sound()
```

Then each child decides what that sound actually is.

```text
             Animal
                │
          sound() required
                │
        ┌───────┴───────┐
        ↓               ↓
       Dog             Cat
        │               │
     "Bark"           "Meow"
```

This is an example of **polymorphism**.

---

# What is Polymorphism?

Polymorphism means that different objects can respond to the **same method name** in different ways.

For example:

```python
dog.sound()
cat.sound()
```

Both use:

```python
sound()
```

But they produce different results:

```text
Dog  → Bark
Cat  → Meow
```

The method name is the same, but the behaviour is different.

---

# `shapes.py`

## What this file demonstrates

`shapes.py` introduces several important concepts:

* Abstract Base Classes
* Abstract methods
* Inheritance
* Polymorphism
* Duck typing
* The `math` module

The class structure is:

```text
            Shape
           /     \
          /       \
      Circle    Rectangle
```

---

# The `Shape` Class

The class is:

```python
class Shape(ABC):
```

This makes `Shape` an Abstract Base Class.

It contains two abstract methods:

```python
@abstractmethod
def area(self):
    pass
```

and:

```python
@abstractmethod
def perimeter(self):
    pass
```

This means every concrete shape is expected to provide:

```text
area()
perimeter()
```

---

# Why Does Shape Need These Methods?

Different shapes calculate their area and perimeter differently.

For a circle:

```text
area = π × radius²
```

For a rectangle:

```text
area = width × height
```

The formulas are different.

But both shapes still have an `area()` method.

The abstract class provides a common interface:

```text
Shape
│
├── area()
└── perimeter()
```

Then each child class decides how to perform the calculations.

---

# The Circle Class

Circle inherits from Shape:

```python
class Circle(Shape):
```

It has a constructor:

```python
def __init__(self, radius):
    self.radius = radius
```

When we create:

```python
circle = Circle(5)
```

the object stores:

```text
radius = 5
```

---

# Circle Area

The Circle class implements:

```python
def area(self):
    return math.pi * (self.radius ** 2)
```

The formula is:

```text
area = π × r²
```

If the radius is `5`:

```text
area = π × 5²
     = π × 25
     ≈ 78.54
```

The code uses:

```python
math.pi
```

to get the value of π.

---

# Circle Perimeter

The perimeter of a circle is also called its circumference.

The code is:

```python
def perimeter(self):
    return 2 * math.pi * self.radius
```

The formula is:

```text
perimeter = 2 × π × radius
```

---

# The Rectangle Class

Rectangle also inherits from Shape:

```python
class Rectangle(Shape):
```

It stores:

```text
width
height
```

The constructor is:

```python
def __init__(self, width, height):
    self.width = width
    self.height = height
```

For example:

```python
rectangle = Rectangle(5, 3)
```

creates:

```text
width  = 5
height = 3
```

---

# Rectangle Area

The Rectangle implementation is:

```python
def area(self):
    return self.width * self.height
```

The formula is:

```text
area = width × height
```

For a rectangle with width `5` and height `3`:

```text
5 × 3 = 15
```

---

# Rectangle Perimeter

The code is:

```python
def perimeter(self):
    return 2 * (self.width + self.height)
```

The formula is:

```text
perimeter = 2 × (width + height)
```

For width `5` and height `3`:

```text
2 × (5 + 3)
= 2 × 8
= 16
```

---

# The `shape_info()` Function

At the bottom of the file there is:

```python
def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
```

This function is particularly useful for understanding **polymorphism** and **duck typing**.

The function doesn't care whether it receives a:

```text
Circle
Rectangle
```

or another object.

It only cares that the object provides:

```text
area()
perimeter()
```

---

# What is Duck Typing?

Python often follows the idea:

> If an object behaves like the thing we need, we can use it.

The `shape_info()` function doesn't check:

```python
if type(shape) is Circle:
```

or:

```python
if type(shape) is Rectangle:
```

Instead, it simply does:

```python
shape.area()
shape.perimeter()
```

If the object has those methods, the function can use it.

This is called **duck typing**.

A simple way to remember it is:

```text
If it can do what I need,
I can use it.
```

---

# Example of `shape_info()`

For a circle:

```python
circle = Circle(5)
shape_info(circle)
```

The function calls:

```python
circle.area()
circle.perimeter()
```

For a rectangle:

```python
rectangle = Rectangle(5, 3)
shape_info(rectangle)
```

The function calls:

```python
rectangle.area()
rectangle.perimeter()
```

The function is the same in both cases.

The object determines what calculations happen.

---

# The Polymorphism Flow

The process looks like this:

```text
                 shape_info()
                      │
                      ↓
             What object was given?
                      │
             ┌────────┴────────┐
             ↓                 ↓
          Circle            Rectangle
             │                 │
             ↓                 ↓
         area()             area()
         perimeter()        perimeter()
             │                 │
             ↓                 ↓
       Circle formulas    Rectangle formulas
```

This is polymorphism in action.

---

# `flyingfish.py`

## What this file demonstrates

This file introduces **multiple inheritance**.

The classes are:

```text
Fish
Bird
  \ /
   ↓
FlyingFish
```

A `FlyingFish` inherits from both:

```python
class FlyingFish(Fish, Bird):
```

This means it gets functionality from both parent classes.

---

# The Fish Class

Fish provides:

```python
def swim(self):
    print("The fish is swimming")
```

and:

```python
def habitat(self):
    print("The fish lives in water")
```

So a Fish can:

```text
swim()
habitat()
```

---

# The Bird Class

Bird provides:

```python
def fly(self):
    print("The bird is flying")
```

and:

```python
def habitat(self):
    print("The bird lives in the sky")
```

So a Bird can:

```text
fly()
habitat()
```

---

# Multiple Inheritance

FlyingFish is defined as:

```python
class FlyingFish(Fish, Bird):
```

This means it inherits from **two parent classes**.

```text
       Fish             Bird
        │                 │
        │                 │
        └────────┬────────┘
                 ↓
            FlyingFish
```

FlyingFish therefore has access to behaviour from both classes.

---

# Method Overriding

FlyingFish provides its own versions of:

```python
def fly(self):
```

```python
def swim(self):
```

and:

```python
def habitat(self):
```

For example:

```python
def fly(self):
    print("The flying fish is soaring!")
```

This replaces the normal Bird implementation when working with a FlyingFish object.

Similarly:

```python
def swim(self):
    print("The flying fish is swimming!")
```

replaces the normal Fish implementation.

---

# Why Override the Methods?

A FlyingFish behaves differently from an ordinary fish or bird.

Instead of:

```text
The fish is swimming
```

it says:

```text
The flying fish is swimming!
```

Instead of:

```text
The bird is flying
```

it says:

```text
The flying fish is soaring!
```

The class is using inheritance to obtain behaviour and then **customising that behaviour**.

---

# FlyingFish Habitat

Both Fish and Bird have a `habitat()` method.

Fish says:

```text
The fish lives in water
```

Bird says:

```text
The bird lives in the sky
```

FlyingFish overrides both with:

```text
The flying fish lives both in water and the sky!
```

This is a useful example of why method overriding is important when using multiple inheritance.

---

# Dragon

## `dragon.py`

This file demonstrates **mixins**.

The classes are:

```text
SwimMixin
FlyMixin
     \   /
      \ /
     Dragon
```

---

# What is a Mixin?

A **mixin** is a class designed to provide a specific piece of functionality to another class.

A mixin usually represents a behaviour rather than a complete object.

For example:

```python
class SwimMixin:
```

provides swimming.

And:

```python
class FlyMixin:
```

provides flying.

The Dragon can then combine those behaviours.

---

# `SwimMixin`

The class contains:

```python
def swim(self):
    print("The creature swims!")
```

Its job is simple:

> Give another class the ability to swim.

---

# `FlyMixin`

The FlyMixin contains:

```python
def fly(self):
    print("The creature flies!")
```

Its job is:

> Give another class the ability to fly.

---

# The Dragon Class

Dragon inherits from both mixins:

```python
class Dragon(SwimMixin, FlyMixin):
```

So it gets:

```text
SwimMixin
    │
    └── swim()

FlyMixin
    │
    └── fly()

Dragon
    │
    ├── swim()
    └── fly()
```

Dragon also defines its own method:

```python
def roar(self):
    print("The dragon roars!")
```

So a Dragon has three behaviours:

```text
swim()
fly()
roar()
```

---

# Why Use Mixins?

Mixins allow us to separate behaviours into small reusable pieces.

Instead of writing:

```python
class Dragon:
    def swim(self):
        ...

    def fly(self):
        ...

    def roar(self):
        ...
```

we can separate the behaviours:

```text
SwimMixin
    ↓
swimming

FlyMixin
    ↓
flying

Dragon
    ↓
roaring
```

This can make code easier to reuse.

For example, another class could also inherit from `FlyMixin` if it needs flying behaviour.

---

# `verboselist.py`

## What this file demonstrates

This file demonstrates a different type of inheritance.

Instead of creating our own parent class, we inherit from one of Python's **built-in classes**.

The class is:

```python
class VerboseList(list):
```

This means:

```text
VerboseList
     ↓ inherits from
list
```

`list` is Python's built-in list class.

---

# What is a Python List?

A list stores multiple values.

For example:

```python
numbers = [1, 2, 3]
```

Python's list already provides methods such as:

```text
append()
extend()
remove()
pop()
```

Normally these methods perform their operation without printing anything.

`VerboseList` changes that behaviour.

---

# Creating a VerboseList

For example:

```python
my_list = VerboseList()
```

The object is still a list.

We can use normal list functionality:

```python
my_list.append(10)
```

But `VerboseList` has changed what happens when `append()` is called.

---

# Overriding `append()`

The class defines:

```python
def append(self, item):
    super().append(item)
    print(f"Added [{item}] to the list.")
```

This overrides the normal `list.append()` method.

First:

```python
super().append(item)
```

calls the original list behaviour.

Then:

```python
print(...)
```

prints a message.

So:

```python
my_list.append(10)
```

results in:

```text
Added [10] to the list.
```

and the value is still added to the list.

---

# Why Use `super()` Here?

Remember that `VerboseList` inherits from `list`.

So:

```python
super().append(item)
```

means:

> Use the original `append()` method from the parent class.

The process is:

```text
my_list.append(10)
       ↓
VerboseList.append()
       ↓
super().append(10)
       ↓
original list.append()
       ↓
10 is added
       ↓
print notification
```

This lets us add extra behaviour without rewriting how Python's list works internally.

---

# Overriding `extend()`

The class also overrides:

```python
def extend(self, iterable):
```

It first converts the iterable into a list:

```python
items_list = list(iterable)
```

Then counts the items:

```python
count = len(items_list)
```

Then calls the original list method:

```python
super().extend(items_list)
```

Finally, it prints:

```text
Extended the list with [number] items.
```

For example:

```python
my_list.extend([1, 2, 3])
```

prints:

```text
Extended the list with [3] items.
```

---

# Why Convert the Iterable to a List?

The parameter is called:

```python
iterable
```

An iterable is something Python can go through one item at a time.

Examples include:

```text
list
tuple
string
```

The code converts it to a list:

```python
items_list = list(iterable)
```

This makes it easy to:

1. Count the items
2. Pass the same values to `extend()`

---

# Overriding `remove()`

The class also overrides:

```python
def remove(self, item):
```

It first prints:

```python
print(f"Removed [{item}] from the list.")
```

Then calls:

```python
super().remove(item)
```

This uses the original list's `remove()` method.

If the item isn't in the list, Python's normal `ValueError` behaviour still occurs.

---

# Overriding `pop()`

The `pop()` method is:

```python
def pop(self, index=-1):
```

The default index is:

```text
-1
```

which means the last item in the list.

The method first gets the item:

```python
item = self[index]
```

Then prints:

```python
print(f"Popped [{item}] from the list.")
```

Finally:

```python
return super().pop(index)
```

removes and returns the item using the original list behaviour.

---

# VerboseList Example

Suppose we write:

```python
my_list = VerboseList()

my_list.append(5)
```

The process is:

```text
append(5)
   ↓
VerboseList.append()
   ↓
super().append(5)
   ↓
5 added to list
   ↓
"Added [5] to the list."
```

The result is both the normal list operation and an additional message.

---

# The Main Concepts in This Directory

The five files demonstrate several different OOP ideas.

## Abstract Base Classes

Shown in:

```text
animals.py
shapes.py
```

An abstract class defines a structure that child classes must follow.

---

## Abstract Methods

Shown in:

```python
@abstractmethod
def sound(self):
```

and:

```python
@abstractmethod
def area(self):
```

An abstract method says that child classes are expected to implement that method.

---

## Polymorphism

Shown in:

```text
animals.py
shapes.py
```

Different objects can respond to the same method in different ways.

For example:

```text
Dog.sound() → Bark
Cat.sound() → Meow
```

---

## Duck Typing

Shown in:

```text
shapes.py
```

`shape_info()` doesn't care what specific class an object belongs to.

It only requires:

```text
area()
perimeter()
```

---

## Multiple Inheritance

Shown in:

```text
flyingfish.py
dragon.py
```

A class can inherit from more than one parent.

For example:

```python
class FlyingFish(Fish, Bird):
```

---

## Mixins

Shown in:

```text
dragon.py
```

Mixins provide small pieces of reusable behaviour.

```text
SwimMixin → swimming
FlyMixin  → flying
Dragon    → roaring
```

---

## Method Overriding

Shown in:

```text
flyingfish.py
verboselist.py
```

A child class replaces or changes a method inherited from its parent.

---

## Extending Built-in Classes

Shown in:

```text
verboselist.py
```

`VerboseList` inherits directly from Python's built-in:

```python
list
```

This allows us to customise normal list behaviour.

---

# Comparing the Different Techniques

These examples use inheritance in different ways.

| File             | Main concept         | What it demonstrates                             |
| ---------------- | -------------------- | ------------------------------------------------ |
| `animals.py`     | Abstract classes     | Animals must implement `sound()`                 |
| `shapes.py`      | ABC + polymorphism   | Shapes must implement `area()` and `perimeter()` |
| `flyingfish.py`  | Multiple inheritance | One class inherits from Fish and Bird            |
| `dragon.py`      | Mixins               | Combines swimming and flying behaviours          |
| `verboselist.py` | Built-in inheritance | Extends Python's `list` class                    |

---

# How the Concepts Fit Together

The directory can be thought of as several different approaches to building reusable classes.

```text
                 Object-Oriented Programming
                           │
          ┌────────────────┼─────────────────┐
          │                │                 │
          ↓                ↓                 ↓
       Abstract         Multiple          Extending
        Classes        Inheritance        Existing Classes
          │                │                 │
          ↓                ↓                 ↓
      Animal/Shape     FlyingFish       VerboseList
          │
          ↓
     Polymorphism
```

Mixins provide another way of combining behaviour:

```text
        SwimMixin       FlyMixin
             \             /
              \           /
               ↓         ↓
                  Dragon
```

---

# A Beginner's Guide to Reading These Files

When looking at one of these classes, ask yourself five questions.

## 1. What class is being created?

Look for:

```python
class Something:
```

or:

```python
class Something(Parent):
```

---

## 2. Does it inherit from another class?

Look inside the parentheses.

For example:

```python
class Dog(Animal):
```

means:

```text
Dog inherits from Animal
```

---

## 3. What methods does it have?

Look for:

```python
def method_name(self):
```

These are the behaviours the object can perform.

---

## 4. Is it overriding a parent method?

If the parent already has a method with the same name, the child version overrides it.

For example:

```text
Parent
└── fly()

Child
└── fly()
```

The child's version is used for the child object.

---

## 5. Is it using `super()`?

Look for:

```python
super()
```

This usually means the class is asking its parent class to perform some of the work.

For example:

```python
super().append(item)
```

uses the original `list.append()` behaviour.

---

# The Big Picture

All of these exercises are teaching a similar idea:

> **We can create classes that build on existing classes and behaviour.**

Sometimes we want a class to define rules:

```text
Shape
 ├── area()
 └── perimeter()
```

Sometimes we want to combine behaviours:

```text
SwimMixin + FlyMixin
          ↓
        Dragon
```

Sometimes we want to customise existing behaviour:

```text
list
 ↓
VerboseList
```

And sometimes we want different objects to respond differently to the same method:

```text
Dog.sound() → Bark
Cat.sound() → Meow
```

These are all important parts of Object-Oriented Programming.

---

# Final Summary

The main concepts to understand from this directory are:

### Abstract Base Class

A class used as a blueprint for other classes.

```python
class Animal(ABC):
```

### Abstract Method

A method that child classes are expected to implement.

```python
@abstractmethod
def sound(self):
```

### Inheritance

A class can inherit functionality from another class.

```python
class Dog(Animal):
```

### Polymorphism

Different objects can use the same method name but behave differently.

```text
Dog.sound() → Bark
Cat.sound() → Meow
```

### Duck Typing

Python can use an object based on what it can do rather than its exact class.

```python
shape.area()
shape.perimeter()
```

### Multiple Inheritance

A class can inherit from multiple classes.

```python
class FlyingFish(Fish, Bird):
```

### Mixins

Small classes that provide specific behaviours.

```text
SwimMixin → swim()
FlyMixin  → fly()
```

### Method Overriding

A child class can provide its own version of a parent's method.

```python
def fly(self):
```

### `super()`

Allows a child class to use the parent's implementation.

```python
super().append(item)
```

### Extending Built-in Classes

Python's existing classes can be inherited and customised.

```python
class VerboseList(list):
```

---

# Final Inheritance Map

The classes in this directory can be visualised like this:

```text
                         Animal
                         /    \
                        /      \
                      Dog      Cat
                       │        │
                    sound()   sound()
                       │        │
                     Bark     Meow


                         Shape
                         /   \
                        /     \
                   Circle    Rectangle
                      │          │
                  area()     area()
               perimeter()  perimeter()
                       \       /
                        \     /
                      shape_info()


              ┌────────────┐   ┌────────────┐
              │    Fish    │   │    Bird    │
              │            │   │            │
              │  swim()    │   │   fly()    │
              │  habitat() │   │  habitat() │
              └─────┬──────┘   └─────┬──────┘
                    │                │
                    └───────┬────────┘
                            ↓
                       FlyingFish


                  SwimMixin    FlyMixin
                       \          /
                        \        /
                         ↓      ↓
                          Dragon
                            │
                          roar()


                           list
                            │
                            ↓
                      VerboseList
                            │
                  ┌─────────┼─────────┐
                  ↓         ↓         ↓
               append()  extend()  remove()
                                      │
                                    pop()
```

The most important lesson is that inheritance is not just about making one class the "child" of another. It gives us ways to **reuse code, enforce common rules, customise behaviour, combine behaviours, and make different objects work through the same interface**.

Once these ideas become comfortable, more advanced Python programs become much easier to understand.

