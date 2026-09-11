# Module 04: Functions

Functions are reusable blocks of code that perform specific tasks. They help organize code, avoid repetition, and make programs more maintainable.

## Topics Covered

1. Defining Functions
2. Parameters and Arguments
3. Return Values
4. Default Parameters
5. Variable Scope
6. Lambda Functions
7. Docstrings

## 1. Defining Functions

Functions are defined using the `def` keyword.

```python
# Basic function
def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!
```

### Function Naming
- Use lowercase with underscores
- Be descriptive about what it does
- Use verbs: `calculate_total()`, `send_email()`

## 2. Parameters and Arguments

Parameters allow functions to accept input.

```python
# Function with one parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

# Function with multiple parameters
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add(5, 3)  # Output: 5 + 3 = 8
```

### Positional vs Keyword Arguments
```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}")

# Positional arguments (order matters)
describe_pet("dog", "Buddy")

# Keyword arguments (order doesn't matter)
describe_pet(pet_name="Whiskers", animal_type="cat")

# Mix (positional must come first)
describe_pet("hamster", pet_name="Fluffy")
```

## 3. Return Values

Functions can return values using the `return` statement.

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8

# Without return, function returns None
def greet(name):
    print(f"Hello, {name}")

result = greet("Alice")  # Prints: Hello, Alice
print(result)            # Prints: None
```

### Returning Multiple Values
```python
def calculate(a, b):
    sum_result = a + b
    diff_result = a - b
    return sum_result, diff_result

# Unpack returned values
total, difference = calculate(10, 3)
print(f"Sum: {total}, Difference: {difference}")
```

## 4. Default Parameters

Parameters can have default values.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Uses default: Hello, Alice!
greet("Bob", "Hi")          # Custom greeting: Hi, Bob!
greet("Charlie", greeting="Hey")  # Hey, Charlie!
```

### Best Practice
Put parameters with defaults after those without:
```python
# Good
def make_pizza(size, topping="cheese"):
    pass

# Bad - will cause error
# def make_pizza(size="medium", topping):
#     pass
```

## 5. Variable Scope

Variables have different scopes depending on where they're defined.

### Local Scope
```python
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Works: 10
# print(x)     # Error: x is not defined outside function
```

### Global Scope
```python
x = 10  # Global variable

def my_function():
    print(x)  # Can read global variable

my_function()  # Output: 10

# To modify global variable
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1
```

### Best Practice
Avoid using `global` when possible. Instead, use parameters and return values:
```python
# Better approach
def increment(count):
    return count + 1

count = 0
count = increment(count)
```

## 6. Lambda Functions

Lambda functions are small anonymous functions defined in one line.

```python
# Regular function
def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

print(square(5))         # Output: 25
print(square_lambda(5))  # Output: 25

# Lambda with multiple parameters
add = lambda a, b: a + b
print(add(3, 5))  # Output: 8
```

### When to Use Lambda
- Short, simple operations
- When passing function as argument
- In `map()`, `filter()`, `sorted()`

```python
numbers = [1, 2, 3, 4, 5]

# Square each number using map
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]

# Sort by custom key
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1])
# [('Charlie', 78), ('Alice', 85), ('Bob', 92)]
```

## 7. Docstrings

Docstrings document what a function does.

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    """
    return length * width

# Access docstring
print(calculate_area.__doc__)
help(calculate_area)
```

## Common Patterns

### Validation Pattern
```python
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
```

### Early Return Pattern
```python
def is_adult(age):
    if age < 18:
        return False
    return True
```

### Helper Functions
```python
def is_even(num):
    return num % 2 == 0

def count_evens(numbers):
    count = 0
    for num in numbers:
        if is_even(num):
            count += 1
    return count
```

## Best Practices

1. **One task per function**: Each function should do one thing well
2. **Keep functions short**: Aim for <20 lines
3. **Use descriptive names**: Function name should explain what it does
4. **Document complex functions**: Use docstrings
5. **Avoid side effects**: Return values instead of modifying global state
6. **Use type hints** (optional but helpful):
```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

## Key Takeaways

- Functions organize code into reusable blocks
- Use parameters to accept input
- Use `return` to send back results
- Default parameters provide flexibility
- Scope determines variable visibility
- Lambda functions for simple operations
- Docstrings document your functions

## Practice

Review `examples.py` for practical demonstrations, then complete `exercises.py`!

## Next Module

After mastering functions, move to [Module 05: Modules and Packages](../05_Modules_and_Packages/) to learn about code organization!
