# Module 03: Data Structures

Learn about Python's built-in data structures to organize and manage collections of data efficiently!

## Topics Covered

1. Lists - Ordered, mutable collections
2. Tuples - Ordered, immutable collections
3. Dictionaries - Key-value pairs
4. Sets - Unordered, unique elements
5. List Comprehensions
6. Common Operations and Methods

## 1. Lists

Lists are ordered, mutable (changeable) collections that can hold items of different types.

### Creating Lists
```python
# Empty list
empty_list = []

# List with items
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
```

### Accessing Elements
```python
fruits = ["apple", "banana", "cherry"]

# Indexing (starts at 0)
first = fruits[0]        # "apple"
last = fruits[-1]        # "cherry" (negative index from end)

# Slicing
subset = fruits[0:2]     # ["apple", "banana"]
```

### Modifying Lists
```python
fruits = ["apple", "banana", "cherry"]

# Change item
fruits[1] = "blueberry"

# Add items
fruits.append("date")           # Add to end
fruits.insert(1, "avocado")     # Insert at index

# Remove items
fruits.remove("apple")          # Remove by value
popped = fruits.pop()           # Remove and return last item
del fruits[0]                   # Delete by index
```

### List Methods
```python
numbers = [3, 1, 4, 1, 5]

numbers.sort()          # Sort in place
numbers.reverse()       # Reverse in place
count = numbers.count(1)  # Count occurrences
index = numbers.index(4)  # Find index of value
numbers.clear()         # Remove all items
```

## 2. Tuples

Tuples are ordered, immutable (cannot be changed) collections.

### Creating Tuples
```python
# Tuple with parentheses
coordinates = (10, 20)
person = ("Alice", 25, "Engineer")

# Tuple without parentheses (tuple packing)
point = 5, 10

# Single item tuple (comma required)
single = (42,)
```

### Why Use Tuples?
- Faster than lists
- Protect data from modification
- Can be used as dictionary keys
- Return multiple values from functions

### Accessing Tuples
```python
person = ("Alice", 25, "Engineer")

name = person[0]        # "Alice"
age = person[1]         # 25

# Tuple unpacking
name, age, job = person
```

## 3. Dictionaries

Dictionaries store key-value pairs for fast lookups.

### Creating Dictionaries
```python
# Empty dictionary
empty_dict = {}

# Dictionary with data
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Using dict()
person = dict(name="Bob", age=25)
```

### Accessing and Modifying
```python
student = {"name": "Alice", "age": 20, "grade": "A"}

# Access values
name = student["name"]          # "Alice"
age = student.get("age")        # 20 (safer, returns None if missing)

# Add or update
student["email"] = "alice@example.com"
student["age"] = 21

# Remove items
del student["grade"]
email = student.pop("email")    # Remove and return value
```

### Dictionary Methods
```python
student = {"name": "Alice", "age": 20}

keys = student.keys()           # All keys
values = student.values()       # All values
items = student.items()         # All key-value pairs

# Check if key exists
if "name" in student:
    print("Name exists")
```

### Looping Through Dictionaries
```python
student = {"name": "Alice", "age": 20, "grade": "A"}

# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
```

## 4. Sets

Sets are unordered collections of unique elements.

### Creating Sets
```python
# Using curly braces
numbers = {1, 2, 3, 4, 5}

# Using set()
letters = set("hello")  # {'h', 'e', 'l', 'o'}

# Empty set (must use set(), {} creates empty dict)
empty_set = set()
```

### Set Operations
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Add and remove
a.add(5)
a.remove(1)         # Error if not found
a.discard(10)       # No error if not found

# Set mathematics
union = a | b           # {1, 2, 3, 4, 5, 6}
intersection = a & b    # {3, 4}
difference = a - b      # {1, 2}
symmetric_diff = a ^ b  # {1, 2, 5, 6}
```

## 5. List Comprehensions

A concise way to create lists.

### Basic Syntax
```python
# Traditional way
squares = []
for x in range(5):
    squares.append(x ** 2)

# List comprehension
squares = [x ** 2 for x in range(5)]
# [0, 1, 4, 9, 16]
```

### With Conditions
```python
# Only even numbers
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Transform strings
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
# ["ALICE", "BOB", "CHARLIE"]
```

### Dictionary and Set Comprehensions
```python
# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
unique_lengths = {len(word) for word in ["hi", "hello", "hey"]}
# {2, 3, 5}
```

## 6. Common Patterns

### Finding Maximum/Minimum
```python
numbers = [3, 7, 2, 9, 4]
maximum = max(numbers)      # 9
minimum = min(numbers)      # 2
```

### Summing and Length
```python
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)        # 15
length = len(numbers)       # 5
average = sum(numbers) / len(numbers)  # 3.0
```

### Checking Membership
```python
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("We have bananas!")

if "grape" not in fruits:
    print("No grapes!")
```

### Combining Lists
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2        # [1, 2, 3, 4, 5, 6]
list1.extend(list2)             # Adds list2 to list1
```

## When to Use Each Structure?

| Structure | Use When |
|-----------|----------|
| **List** | Ordered collection, need to modify, duplicates OK |
| **Tuple** | Ordered collection, don't need to modify, faster |
| **Dictionary** | Need key-value mapping, fast lookups |
| **Set** | Need unique elements, set operations |

## Key Takeaways

- **Lists**: Ordered, mutable, allow duplicates `[]`
- **Tuples**: Ordered, immutable, allow duplicates `()`
- **Dictionaries**: Key-value pairs, mutable `{}`
- **Sets**: Unordered, unique elements, mutable `{}`
- List comprehensions provide concise syntax
- Choose structure based on your needs

## Practice

Check `examples.py` for practical demonstrations, then complete `exercises.py`!

## Next Module

Master data structures, then move to [Module 04: Functions](../04_Functions/) to learn how to organize your code!
