# Introduction to Python

## What is Python?

Python is a high-level, interpreted, general-purpose programming language created by Guido van Rossum and first released in 1991. It emphasizes code readability and simplicity, making it an excellent choice for beginners and experienced developers alike.

## Key Characteristics

- **Interpreted**: Code is executed line-by-line, making debugging easier
- **Dynamically Typed**: Variable types are determined at runtime
- **Object-Oriented**: Supports OOP principles (classes, inheritance, polymorphism)
- **Multi-paradigm**: Supports procedural, functional, and OOP programming styles
- **Cross-platform**: Runs on Windows, macOS, Linux, and more
- **Extensive Standard Library**: "Batteries included" philosophy

## Python 2 vs Python 3

- **Python 2**: End-of-life as of January 1, 2020 (no longer supported)
- **Python 3**: Current version, introduced in 2008 with breaking changes
- **Always use Python 3** for new projects (current stable: 3.11+)

## Installation

```bash
# Check if Python is installed
python3 --version

# Install on Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# Install on macOS (using Homebrew)
brew install python3

# Install on Windows
# Download from python.org or use Microsoft Store
```

## Running Python Code

### Interactive REPL (Read-Eval-Print Loop)
```bash
python3
>>> print("Hello, World!")
Hello, World!
>>> exit()
```

### Running Python Files
```bash
# Create a file: hello.py
python3 hello.py

# Make script executable (Unix-like systems)
chmod +x hello.py
./hello.py  # Requires shebang: #!/usr/bin/env python3
```

## Basic Syntax Overview

### Variables and Data Types
```python
# No declaration needed, dynamically typed
name = "Python"           # str
version = 3.11            # float
is_awesome = True         # bool
numbers = [1, 2, 3]       # list
config = {"key": "value"} # dict
coordinates = (10, 20)    # tuple
unique_items = {1, 2, 3}  # set
```

### Indentation Matters
Python uses indentation (4 spaces) to define code blocks instead of braces:
```python
if True:
    print("Indented")     # Correct
    print("Same level")   # Correct
        print("Error")    # IndentationError
```

### Comments
```python
# Single-line comment

"""
Multi-line comment
or docstring
"""
```

### Functions
```python
def greet(name):
    """Function to greet a person"""
    return f"Hello, {name}!"

print(greet("World"))
```

### Control Flow
```python
# If-elif-else
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# For loop
for i in range(5):
    print(i)

# While loop
while condition:
    # code
    pass
```

## Package Management with pip

```bash
# Install a package
pip3 install requests

# Install from requirements.txt
pip3 install -r requirements.txt

# List installed packages
pip3 list

# Uninstall a package
pip3 uninstall package_name
```

## Virtual Environments

Virtual environments isolate project dependencies:

```bash
# Create virtual environment
python3 -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Deactivate
deactivate

# Create requirements.txt
pip freeze > requirements.txt
```

## Python's Philosophy (The Zen of Python)

```python
import this
```

Key principles:
- Beautiful is better than ugly
- Explicit is better than implicit
- Simple is better than complex
- Readability counts
- There should be one obvious way to do it

## Common Use Cases

- **Web Development**: Django, Flask, FastAPI
- **Data Science**: NumPy, Pandas, Matplotlib
- **Machine Learning**: TensorFlow, PyTorch, scikit-learn
- **Automation**: Scripts, DevOps, system administration
- **Testing**: pytest, unittest
- **GUI Applications**: Tkinter, PyQt, Kivy
- **API Development**: REST, GraphQL
- **Cloud Computing**: AWS (boto3), Google Cloud, Azure

## Important Built-in Functions

```python
print()      # Output to console
len()        # Length of object
type()       # Get type of object
int()        # Convert to integer
str()        # Convert to string
input()      # Get user input
range()      # Generate sequence of numbers
enumerate()  # Get index and value in loops
zip()        # Combine iterables
open()       # File operations
help()       # Get help on objects
dir()        # List attributes/methods
```

## File I/O Basics

```python
# Reading a file
with open('file.txt', 'r') as f:
    content = f.read()

# Writing to a file
with open('file.txt', 'w') as f:
    f.write("Hello, World!")

# Appending to a file
with open('file.txt', 'a') as f:
    f.write("\nNew line")
```

## Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("Always executes")
```

## Python Enhancement Proposals (PEPs)

- **PEP 8**: Style Guide for Python Code
- **PEP 20**: The Zen of Python
- **PEP 484**: Type Hints

## Learning Resources

- Official Python Documentation: https://docs.python.org
- Python Tutorial: https://docs.python.org/3/tutorial/
- Real Python: https://realpython.com
- Python Package Index (PyPI): https://pypi.org

## Quick Tips

1. **Use meaningful variable names**: `user_count` not `uc`
2. **Follow PEP 8**: Use tools like `black` or `flake8`
3. **Use virtual environments**: Always isolate project dependencies
4. **Write docstrings**: Document your functions and classes
5. **Use list comprehensions**: More Pythonic than traditional loops
6. **Leverage the standard library**: Don't reinvent the wheel
7. **Use f-strings**: Modern way to format strings (Python 3.6+)

```python
# List comprehension example
squares = [x**2 for x in range(10)]

# F-string example
name = "Python"
print(f"I love {name}!")
```

## Next Steps

1. Learn data structures (lists, dictionaries, sets, tuples)
2. Understand functions and scope
3. Master object-oriented programming
4. Explore the standard library
5. Learn multithreading and concurrency (see `11_Multithreading_and_Concurrency/`)
6. Practice with real projects
7. Learn testing and debugging
8. Study algorithms and design patterns
