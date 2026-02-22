# Smart Library System (Python)

## Project Description

This project is a Smart Library System implemented in Python.
It simulates a small library where books can be added, borrowed, and returned without using a database.

The purpose of the project is to demonstrate advanced Python concepts including Object-Oriented Programming, magic methods, decorators, closures, packaging, and duck typing.

---

## Features

* Admin can add books
* Users can borrow books
* Users can return books
* Automatic logging with timestamps
* Library can be iterated using a for loop
* Works with any object that has a `title` attribute (duck typing)

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Magic Methods (Dunder Methods)
* Decorators
* Closures
* Python Packages

---

## Project Structure

library_system/

* **init**.py
* core.py
* utils.py
* **main**.py

---

## Magic Methods Implemented

* `__str__` : Defines how a Book is printed
* `__len__` : Returns number of pages
* `__eq__` : Compares two books based on title and author
* `__getitem__` : Allows iteration through the library

---

## Decorator

The `track_access` decorator logs when a book is borrowed or returned and prints the current timestamp.

---

## Closure (Permission System)

The `permission_check` function is a closure that restricts adding books to Admin users only.

---

## Duck Typing

The function `borrow_item(item)` accepts any object that has a `.title` attribute.
This demonstrates the Python principle: "If it behaves like a book, it can be treated like a book."

---

## Method Resolution Order (MRO)

If a class `DigitalBook` inherits from both `Book` and `Software`:

class Software:
pass

class DigitalBook(Book, Software):
pass

Python searches for methods in this order:
DigitalBook → Book → Software → object

---

## How to Run

Open terminal inside the project folder and run:

python -m library_system

---

## Author

Emmanuel Gentil
