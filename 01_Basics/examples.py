"""
Module 01: Python Basics - Examples
Run this file to see basic Python concepts in action.
"""

print("=" * 50)
print("PYTHON BASICS - EXAMPLES")
print("=" * 50)

# 1. VARIABLES AND ASSIGNMENT
print("\n1. Variables and Assignment")
print("-" * 30)

name = "Alice"
age = 25
height = 5.6
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Is student: {is_student}")

# 2. DATA TYPES
print("\n2. Data Types")
print("-" * 30)

# Numbers
integer_num = 42
float_num = 3.14
print(f"Integer: {integer_num}, Type: {type(integer_num)}")
print(f"Float: {float_num}, Type: {type(float_num)}")

# Strings
greeting = "Hello, Python!"
print(f"String: {greeting}, Type: {type(greeting)}")

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

laugh = "Ha" * 3
print(f"Repeated string: {laugh}")

# Booleans
is_sunny = True
is_raining = False
print(f"Is sunny: {is_sunny}, Type: {type(is_sunny)}")

# 3. TYPE CONVERSION
print("\n3. Type Conversion")
print("-" * 30)

# String to number
str_number = "123"
converted_int = int(str_number)
print(f"String '{str_number}' converted to int: {converted_int}")

# Number to string
num = 456
converted_str = str(num)
print(f"Number {num} converted to string: '{converted_str}'")

# Float to int (loses decimal part)
decimal = 9.99
converted = int(decimal)
print(f"Float {decimal} converted to int: {converted}")

# 4. ARITHMETIC OPERATORS
print("\n4. Arithmetic Operators")
print("-" * 30)

a = 15
b = 4

print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Floor Division (a // b): {a // b}")
print(f"Modulus (a % b): {a % b}")
print(f"Exponent (a ** b): {a ** b}")

# 5. COMPARISON OPERATORS
print("\n5. Comparison Operators")
print("-" * 30)

x = 10
y = 20

print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}")

# 6. LOGICAL OPERATORS
print("\n6. Logical Operators")
print("-" * 30)

has_ticket = True
has_id = False

print(f"has_ticket = {has_ticket}, has_id = {has_id}")
print(f"has_ticket AND has_id: {has_ticket and has_id}")
print(f"has_ticket OR has_id: {has_ticket or has_id}")
print(f"NOT has_ticket: {not has_ticket}")

# 7. INPUT AND OUTPUT
print("\n7. Input and Output")
print("-" * 30)

# Different ways to print
print("Simple message")
print("Multiple", "items", "in", "print")
print(f"Formatted string with variable: {name}")

# Print with custom separator and end
print("Apple", "Banana", "Cherry", sep=" | ")
print("This is on one line...", end=" ")
print("and this continues it!")

# 8. PRACTICAL EXAMPLE: Simple Calculator
print("\n8. Practical Example: Simple Calculator")
print("-" * 30)

num1 = 15
num2 = 3
operation = "multiply"

print(f"Number 1: {num1}")
print(f"Number 2: {num2}")
print(f"Operation: {operation}")

if operation == "add":
    result = num1 + num2
elif operation == "multiply":
    result = num1 * num2
else:
    result = "Unknown operation"

print(f"Result: {result}")

# 9. PRACTICAL EXAMPLE: Temperature Converter
print("\n9. Practical Example: Temperature Converter")
print("-" * 30)

celsius = 25
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {fahrenheit}°F")

# Convert back
celsius_back = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F is equal to {celsius_back}°C")

print("\n" + "=" * 50)
print("Examples completed! Now try the exercises.")
print("=" * 50)
