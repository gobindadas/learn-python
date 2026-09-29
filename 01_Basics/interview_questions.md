# Python Basics - Interview Questions

## Level: Normal (1-5)

### Question 1: Variable Assignment and Memory
```python
a = 10
b = a
a = 20
print(b)
```
What will be printed and why? Explain how Python handles variable assignment for immutable types.

### Question 2: Type Conversion Edge Cases
What will be the output of the following and why?
```python
print(int(3.9))
print(int("100"))
print(int("10.5"))  # What happens here?
print(bool("False"))
print(bool(""))
```

### Question 3: String Immutability
```python
s = "hello"
s[0] = "H"
```
Why does this raise an error? How would you properly capitalize the first letter?

### Question 4: Operator Precedence
What is the output and why?
```python
result = 10 + 5 * 2
print(result)

result2 = (10 + 5) * 2
print(result2)

result3 = 2 ** 3 ** 2
print(result3)
```

### Question 5: String Formatting Methods
What are the three main ways to format strings in Python? Provide examples of each.

## Level: Medium (6-10)

### Question 6: Multiple Assignment Gotcha
```python
x = y = z = [1, 2, 3]
x.append(4)
print(y)
print(z)
```
What will be printed? Explain the behavior and how to avoid this issue.

### Question 7: Integer Division and Modulo
Write a function that takes an integer number of seconds and converts it to hours, minutes, and seconds format (HH:MM:SS). Use only integer division and modulo operators.

### Question 8: String Methods Chain
Given a string `s = "  Hello World  "`, write one line of code to:
- Remove leading/trailing whitespace
- Convert to lowercase
- Replace "world" with "python"

### Question 9: Input Validation
Write a function that takes user input and validates:
- It's a positive integer
- It's within a specified range
- Handle all possible exceptions

### Question 10: Memory Efficiency
```python
a = 256
b = 256
print(a is b)

c = 257
d = 257
print(c is d)
```
Why might these produce different results? Explain Python's integer caching.

## Level: Hard (11-15)

### Question 11: Dynamic Type System
```python
def process(data):
    if isinstance(data, int):
        return data * 2
    elif isinstance(data, str):
        return data.upper()
    elif isinstance(data, list):
        return len(data)
    else:
        return None

# What are the potential issues with this design?
# How would you improve it using duck typing principles?
```

### Question 12: String Interning
```python
a = "hello"
b = "hello"
c = "".join(['h', 'e', 'l', 'l', 'o'])

print(a is b)
print(a is c)
print(a == c)
```
Explain the output and the concept of string interning in Python.

### Question 13: Numeric Edge Cases
Write a function that handles the following edge cases properly:
```python
# Division by zero
# Floating point precision errors
# Integer overflow (if applicable in Python)
# Converting between numeric types without losing precision
```

### Question 14: Advanced String Operations
Write a function that takes a string and returns True if it's a valid Python identifier (variable name). Don't use built-in methods like `str.isidentifier()`.

### Question 15: Type Coercion and Comparison
```python
print(1 == True)
print(1 is True)
print(0 == False)
print([] == False)
print(bool([]))
```
Explain each output and the difference between `==` and `is`. What are the implications for type checking?

## Bonus Challenge

### Question 16: Build a Type Validator
Create a function `validate_type(value, expected_type)` that:
- Checks if value matches the expected type
- Handles union types (int or str)
- Handles None/Optional types
- Provides meaningful error messages
- Works with nested types (List[int], Dict[str, int])

Example usage:
```python
validate_type(42, int)  # True
validate_type("hello", int)  # False, raises TypeError with message
validate_type([1, 2, 3], list)  # True
```
