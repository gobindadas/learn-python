# Python Quick Reference Guide

Your handy cheat sheet for Python syntax and common patterns!

## Data Types

```python
# Numbers
integer = 42
floating = 3.14
complex_num = 3 + 4j

# Strings
single_quotes = 'Hello'
double_quotes = "World"
multiline = """Multiple
lines"""

# Boolean
is_true = True
is_false = False

# Collections
list_example = [1, 2, 3]
tuple_example = (1, 2, 3)
dict_example = {"key": "value"}
set_example = {1, 2, 3}
```

## Variables and Operations

```python
# Assignment
x = 5
y = 10

# Arithmetic
x + y   # 15 (addition)
x - y   # -5 (subtraction)
x * y   # 50 (multiplication)
x / y   # 0.5 (division)
x // y  # 0 (floor division)
x % y   # 5 (modulus)
x ** y  # 9765625 (exponent)

# Comparison
x == y  # False (equal)
x != y  # True (not equal)
x < y   # True (less than)
x > y   # False (greater than)
x <= y  # True (less than or equal)
x >= y  # False (greater than or equal)

# Logical
True and False  # False
True or False   # True
not True        # False

# String operations
"Hello" + " " + "World"  # "Hello World"
"Ha" * 3                 # "HaHaHa"
len("Python")            # 6
"python".upper()         # "PYTHON"
"PYTHON".lower()         # "python"
```

## Control Flow

```python
# If-Elif-Else
if x > 10:
    print("Greater than 10")
elif x > 5:
    print("Greater than 5")
else:
    print("5 or less")

# For Loop
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for item in [1, 2, 3]:
    print(item)

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break and Continue
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break     # Stop at 7
    print(i)
```

## Lists

```python
# Creating
fruits = ["apple", "banana", "cherry"]

# Accessing
first = fruits[0]      # "apple"
last = fruits[-1]      # "cherry"
slice = fruits[0:2]    # ["apple", "banana"]

# Modifying
fruits.append("date")       # Add to end
fruits.insert(1, "avocado") # Insert at index
fruits.remove("banana")     # Remove by value
popped = fruits.pop()       # Remove and return last

# Other operations
fruits.sort()           # Sort in place
fruits.reverse()        # Reverse in place
len(fruits)             # Get length
"apple" in fruits       # Check membership

# List comprehension
squares = [x**2 for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]
```

## Dictionaries

```python
# Creating
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

# Accessing
name = person["name"]
age = person.get("age", 0)

# Modifying
person["email"] = "alice@example.com"  # Add/update
del person["city"]                     # Remove
age = person.pop("age")                # Remove and return

# Iteration
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

# Dict comprehension
squares = {x: x**2 for x in range(5)}
```

## Functions

```python
# Basic function
def greet(name):
    print(f"Hello, {name}!")

# Return value
def add(a, b):
    return a + b

# Default parameters
def power(base, exp=2):
    return base ** exp

# Multiple returns
def min_max(numbers):
    return min(numbers), max(numbers)

# Lambda function
square = lambda x: x**2
```

## String Formatting

```python
name = "Alice"
age = 25

# f-strings (recommended)
f"Name: {name}, Age: {age}"

# format()
"Name: {}, Age: {}".format(name, age)
"Name: {n}, Age: {a}".format(n=name, a=age)

# % formatting (old style)
"Name: %s, Age: %d" % (name, age)

# Formatting numbers
pi = 3.14159
f"{pi:.2f}"  # "3.14" (2 decimal places)
```

## File Handling

```python
# Reading
with open('file.txt', 'r') as f:
    content = f.read()        # Entire file
    # or
    lines = f.readlines()     # List of lines
    # or
    for line in f:            # Line by line
        print(line)

# Writing
with open('file.txt', 'w') as f:
    f.write("Hello, World!")

# Appending
with open('file.txt', 'a') as f:
    f.write("New line\n")

# JSON
import json

# Write JSON
with open('data.json', 'w') as f:
    json.dump({"name": "Alice"}, f)

# Read JSON
with open('data.json', 'r') as f:
    data = json.load(f)
```

## Common Patterns

```python
# Swap variables
a, b = b, a

# Multiple assignment
x, y, z = 1, 2, 3

# Enumerate (index + value)
for i, item in enumerate(['a', 'b', 'c']):
    print(i, item)  # 0 a, 1 b, 2 c

# Zip (combine lists)
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(name, age)

# Range variations
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8

# Check type
type(42)        # <class 'int'>
isinstance(42, int)  # True

# Convert types
int("42")       # 42
float("3.14")   # 3.14
str(100)        # "100"
list("abc")     # ['a', 'b', 'c']
```

## Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError as e:
    print(f"Value error: {e}")
else:
    print("No errors occurred")
finally:
    print("Always runs")

# Raising exceptions
if age < 0:
    raise ValueError("Age cannot be negative")
```

## Classes (Basic OOP)

```python
class Dog:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method
    def bark(self):
        return f"{self.name} says Woof!"
    
    # String representation
    def __str__(self):
        return f"Dog({self.name}, {self.age})"

# Creating object
my_dog = Dog("Buddy", 3)
print(my_dog.bark())
print(my_dog)

# Inheritance
class Puppy(Dog):
    def __init__(self, name, age, toy):
        super().__init__(name, age)
        self.toy = toy
```

## Common Modules

```python
# Math
import math
math.sqrt(16)    # 4.0
math.pi          # 3.14159...

# Random
import random
random.randint(1, 10)        # Random int
random.choice([1, 2, 3])     # Random item
random.shuffle(my_list)      # Shuffle in place

# Datetime
from datetime import datetime
now = datetime.now()
today = datetime.today()
formatted = now.strftime("%Y-%m-%d")

# OS
import os
os.getcwd()              # Current directory
os.path.exists('file.txt')  # Check if exists
```

## List Methods Quick Reference

```python
list.append(x)       # Add item to end
list.extend(iterable) # Add all items
list.insert(i, x)    # Insert at position
list.remove(x)       # Remove first occurrence
list.pop([i])        # Remove and return item
list.clear()         # Remove all items
list.index(x)        # Find index
list.count(x)        # Count occurrences
list.sort()          # Sort in place
list.reverse()       # Reverse in place
list.copy()          # Shallow copy
```

## String Methods Quick Reference

```python
str.upper()          # UPPERCASE
str.lower()          # lowercase
str.title()          # Title Case
str.strip()          # Remove whitespace
str.split(sep)       # Split into list
str.join(iterable)   # Join list to string
str.replace(old, new) # Replace substring
str.startswith(prefix) # Check start
str.endswith(suffix)   # Check end
str.find(substring)    # Find index (-1 if not found)
```

## Remember

- **Indentation matters** (use 4 spaces)
- **Index starts at 0**
- **Use `with` for files**
- **f-strings are your friend**
- **List comprehensions are powerful**
- **Read error messages carefully**

Keep this reference handy while coding!
