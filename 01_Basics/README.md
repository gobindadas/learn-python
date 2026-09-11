# Module 01: Python Basics

Welcome to your first Python module! Here you'll learn the fundamental building blocks of Python programming.

## Topics Covered

1. Variables and Assignment
2. Data Types
3. Basic Operators
4. Input and Output
5. Comments

## 1. Variables and Assignment

Variables are containers for storing data. In Python, you don't need to declare the type - Python figures it out automatically.

```python
name = "Alice"          # String variable
age = 25                # Integer variable
height = 5.6            # Float variable
is_student = True       # Boolean variable
```

### Variable Naming Rules:
- Must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Case-sensitive (age and Age are different)
- Cannot use Python keywords (if, while, for, etc.)

### Good naming practices:
```python
# Good
user_name = "Bob"
total_price = 99.99
is_active = True

# Avoid
x = "Bob"               # Not descriptive
userName = 99.99        # Mixed convention
2user = True            # Invalid - starts with number
```

## 2. Data Types

Python has several built-in data types:

### Numbers
```python
# Integer (whole numbers)
count = 10
temperature = -5

# Float (decimal numbers)
price = 19.99
pi = 3.14159

# Complex numbers (advanced)
complex_num = 3 + 4j
```

### Strings
```python
# Strings are text enclosed in quotes
name = "Alice"
message = 'Hello, World!'
multiline = """This is a
multiline string"""

# String operations
greeting = "Hello" + " " + "World"  # Concatenation
repeated = "Ha" * 3                  # Repetition -> "HaHaHa"
```

### Booleans
```python
# True or False values
is_valid = True
has_permission = False

# Result of comparisons
is_adult = age >= 18
```

### Type Checking and Conversion
```python
# Check type
type(42)           # <class 'int'>
type(3.14)         # <class 'float'>
type("hello")      # <class 'str'>

# Convert types
int("42")          # String to integer: 42
float("3.14")      # String to float: 3.14
str(100)           # Integer to string: "100"
bool(1)            # Integer to boolean: True
```

## 3. Basic Operators

### Arithmetic Operators
```python
a = 10
b = 3

addition = a + b        # 13
subtraction = a - b     # 7
multiplication = a * b  # 30
division = a / b        # 3.333...
floor_division = a // b # 3 (rounds down)
modulus = a % b         # 1 (remainder)
exponent = a ** b       # 1000 (10^3)
```

### Comparison Operators
```python
x = 5
y = 10

x == y    # False (equal to)
x != y    # True (not equal to)
x > y     # False (greater than)
x < y     # True (less than)
x >= y    # False (greater than or equal)
x <= y    # True (less than or equal)
```

### Logical Operators
```python
a = True
b = False

a and b   # False (both must be True)
a or b    # True (at least one must be True)
not a     # False (inverts the value)
```

## 4. Input and Output

### Output with print()
```python
print("Hello, World!")
print("My age is", 25)
print(f"My age is {25}")  # f-string (formatted string)

# Multiple items
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")
```

### Input from user
```python
name = input("What is your name? ")
print(f"Hello, {name}!")

# Converting input (input always returns a string)
age = int(input("Enter your age: "))
price = float(input("Enter the price: "))
```

## 5. Comments

Comments are notes in your code that Python ignores. They help explain what your code does.

```python
# This is a single-line comment

"""
This is a multi-line comment
or docstring. It can span
multiple lines.
"""

x = 5  # You can also add comments after code
```

## Key Takeaways

- Variables store data and don't need type declarations
- Python has several data types: int, float, str, bool
- Operators let you perform calculations and comparisons
- Use `print()` for output and `input()` for user input
- Comments make your code more readable

## Practice

Now open `examples.py` to see these concepts in action, then complete the exercises in `exercises.py`!

## Next Module

Once you're comfortable with these basics, move on to [Module 02: Control Flow](../02_Control_Flow/) to learn about making decisions in your code.
