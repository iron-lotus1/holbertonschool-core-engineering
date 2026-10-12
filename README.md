# Holberton School - Core Engineering 🛠️ Python Curriculum

Welcome to my **Core Engineering** repository! This repository tracks my journey through Holberton School's software engineering curriculum, focusing on building strong core programming skills, problem-solving techniques, and best practices in Python—from absolute fundamentals to object-oriented programming, UML modeling, and advanced language features.

---

## 📂 Repository Structure

Below is an overview of the key directories within this repository and what concepts each section covers:

```text
holbertonschool-core-engineering/
├── python_fundamentals/
│   ├── hello_world/
│   ├── control_flow/
│   ├── core_data_structures/
│   └── exception_handling/
├── python_oop/
│   ├── classes_and_objects/
│   ├── inheritance_and_polymorphism/
│   └── encapsulation_and_properties/
├── uml_intro/
│   ├── class_diagrams/
│   └── sequence_and_use_case/
└── python_advanced/
    ├── decorators_and_generators/
    ├── context_managers/
    └── magic_methods/

```

---

# 🗺️ Module Overview

## 1. 🐍 python_fundamentals/

The main entry point for core Python programming concepts. This directory is broken down into thematic modules:

### 🟢 hello_world/

* **What it covers:** The very basics of Python syntax, printing strings, variable declarations, and executing your first Python scripts.
* **Key Concept:** Learning how Python runs code line-by-line and formatting output.

### 🔀 control_flow/

* **What it covers:** How programs make decisions and repeat actions using `if`/`elif`/`else` statements, `while` loops, and `for` loops.
* **Key Concept:** Managing execution logic and controlling the flow of a script based on conditions.

### 🧱 core_data_structures/

* **What it covers:** Storing and organizing collections of data using Python's 4 main built-in data types: Lists, Tuples, Sets, and Dictionaries.
* **Key Concept:** Choosing the right structure for the job based on ordering, mutability, and uniqueness.

### ⚡ exception_handling/

* **What it covers:** Intercepting runtime errors smoothly using `try`, `except`, `else`, `finally`, and custom `raise` statements.
* **Key Concept:** Preventing program crashes and handling invalid inputs safely.

---

## 2. 🧩 python_oop/

Focuses on Object-Oriented Programming (OOP) to design modular, reusable, and maintainable software architectures.

### 📦 classes_and_objects/

* **What it covers:** Defining classes, creating instances (objects), assigning attributes, and writing instance methods using `__init__` and `self`.
* **Key Concept:** Modeling real-world entities into self-contained code blueprints.

### 🧬 inheritance_and_polymorphism/

* **What it covers:** Extending existing classes using parent/child relationships, overriding methods, and using `super()`.
* **Key Concept:** Reusing existing code structures while enabling customized behaviors for sub-classes.

### 🔒 encapsulation_and_properties/

* **What it covers:** Protecting internal object states using private attributes (`__attribute`) and controlling read/write access via Python `@property` getters and setters.
* **Key Concept:** Data hiding and enforcing valid states before updating object attributes.

---

## 3. 📐 uml_intro/

Translating software ideas and designs into Unified Modeling Language (UML) diagrams before writing code.

### 📊 class_diagrams/

* **What it covers:** Creating class diagrams with attributes, methods, access modifiers (`+` public, `-` private, `#` protected), and class relationships (associations, aggregations, compositions).
* **Key Concept:** Visualizing object relationships and system structure prior to implementation.

### 🔄 sequence_and_use_case/

* **What it covers:** Mapping interactions between objects over time and outlining user interactions with the system using use case and sequence diagrams.
* **Key Concept:** Understanding system workflow, call order, and user requirements.

---

## 4. 🚀 python_advanced/

Diving deeper into Python's powerful inner mechanisms, metaprogramming techniques, and advanced patterns.

### 🎨 decorators_and_generators/

* **What it covers:** Higher-order functions, functions as first-class objects, function wrappers (`@decorator`), and memory-efficient iterators using `yield`.
* **Key Concept:** Modifying function behaviors dynamically without altering their source code and handling large datasets efficiently.

### 🛠️ context_managers/

* **What it covers:** Custom context management using the `with` statement via `__enter__` and `__exit__` dunder methods or the `contextlib` module.
* **Key Concept:** Automating setup and teardown tasks such as file handling, database connections, and locks.

### 🪄 magic_methods/

* **What it covers:** Dunder (double underscore) methods such as `__str__`, `__repr__`, `__eq__`, `__add__`, and `__len__`.
* **Key Concept:** Customizing default Python operators and built-in behaviors for custom objects.

---

## 🛠️ General Requirements & Style Guide

All Python scripts in this repository strictly adhere to:

* **Interpreter:** Compiled and run using Python 3.x on Ubuntu / Linux.
* **Style Standard:** PEP 8 style guidelines (4 spaces per indentation level, proper file headers, and clean docstrings).
* **Executability:** All `.py` files begin with `#!/usr/bin/python3` and have executable permissions (`chmod +x`).


