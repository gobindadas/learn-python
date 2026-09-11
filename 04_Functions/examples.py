"""
Module 04: Functions - Examples
Learn how to create and use functions effectively!
"""

print("=" * 50)
print("FUNCTIONS - EXAMPLES")
print("=" * 50)

# 1. BASIC FUNCTIONS
print("\n1. Basic Functions")
print("-" * 30)

def say_hello():
    print("Hello, World!")

def display_separator():
    print("-" * 20)

say_hello()
display_separator()

# 2. FUNCTIONS WITH PARAMETERS
print("\n2. Functions with Parameters")
print("-" * 30)

def greet_person(name):
    print(f"Hello, {name}!")

def calculate_square(number):
    square = number ** 2
    print(f"The square of {number} is {square}")

greet_person("Alice")
greet_person("Bob")
calculate_square(5)

# 3. MULTIPLE PARAMETERS
print("\n3. Multiple Parameters")
print("-" * 30)

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}")

# Positional arguments
describe_pet("dog", "Buddy")
describe_pet("cat", "Whiskers")

# Keyword arguments
describe_pet(pet_name="Tweety", animal_type="bird")

# 4. RETURN VALUES
print("\n4. Return Values")
print("-" * 30)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result1 = add(5, 3)
result2 = multiply(4, 7)
print(f"5 + 3 = {result1}")
print(f"4 * 7 = {result2}")

# Using return value in expression
total = add(10, 20) + add(5, 15)
print(f"Total: {total}")

# 5. RETURNING MULTIPLE VALUES
print("\n5. Returning Multiple Values")
print("-" * 30)

def get_min_max(numbers):
    return min(numbers), max(numbers)

def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return total, count, average

nums = [10, 20, 30, 40, 50]
minimum, maximum = get_min_max(nums)
print(f"Min: {minimum}, Max: {maximum}")

total, count, avg = calculate_stats(nums)
print(f"Total: {total}, Count: {count}, Average: {avg}")

# 6. DEFAULT PARAMETERS
print("\n6. Default Parameters")
print("-" * 30)

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))
print(greet("Charlie", greeting="Hey"))

def make_coffee(size="medium", sugar=1):
    return f"{size.capitalize()} coffee with {sugar} sugar(s)"

print(make_coffee())
print(make_coffee("large"))
print(make_coffee("small", 2))
print(make_coffee(sugar=0, size="large"))

# 7. VARIABLE SCOPE
print("\n7. Variable Scope")
print("-" * 30)

# Global variable
global_var = "I'm global"

def scope_demo():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

scope_demo()
print(f"Outside function - Global: {global_var}")
# print(local_var)  # Would cause error

# Modifying global variable
counter = 0

def increment_counter():
    global counter
    counter += 1
    print(f"Counter: {counter}")

increment_counter()
increment_counter()
print(f"Final counter: {counter}")

# 8. LAMBDA FUNCTIONS
print("\n8. Lambda Functions")
print("-" * 30)

# Regular function
def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

print(f"Regular function: square(5) = {square(5)}")
print(f"Lambda function: square_lambda(5) = {square_lambda(5)}")

# Lambda with multiple parameters
add_lambda = lambda a, b: a + b
print(f"Lambda add: {add_lambda(3, 7)}")

# Using lambda with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# Using lambda with filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# 9. LAMBDA WITH SORTED
print("\n9. Lambda with Sorted")
print("-" * 30)

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("Diana", 95)
]

# Sort by grade (second element)
sorted_by_grade = sorted(students, key=lambda x: x[1])
print("Sorted by grade:")
for name, grade in sorted_by_grade:
    print(f"  {name}: {grade}")

# Sort by name length
sorted_by_length = sorted(students, key=lambda x: len(x[0]))
print("\nSorted by name length:")
for name, grade in sorted_by_length:
    print(f"  {name}: {grade}")

# 10. DOCSTRINGS
print("\n10. Docstrings")
print("-" * 30)

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

area = calculate_area(5, 3)
print(f"Area: {area}")
print("\nFunction docstring:")
print(calculate_area.__doc__)

# 11. PRACTICAL EXAMPLE: Temperature Converter
print("\n11. Practical Example: Temperature Converter")
print("-" * 30)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

c_temp = 25
f_temp = celsius_to_fahrenheit(c_temp)
print(f"{c_temp}°C = {f_temp}°F")

f_temp = 77
c_temp = fahrenheit_to_celsius(f_temp)
print(f"{f_temp}°F = {c_temp:.1f}°C")

# 12. PRACTICAL EXAMPLE: Password Validator
print("\n12. Practical Example: Password Validator")
print("-" * 30)

def is_valid_password(password):
    """Check if password meets security requirements."""
    if len(password) < 8:
        return False, "Too short (minimum 8 characters)"

    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        return False, "Must contain at least one digit"

    has_upper = any(char.isupper() for char in password)
    if not has_upper:
        return False, "Must contain at least one uppercase letter"

    return True, "Password is valid"

passwords = ["Pass123", "password", "PASS123", "Pass1234"]
for pwd in passwords:
    valid, message = is_valid_password(pwd)
    status = "✓" if valid else "✗"
    print(f"{status} '{pwd}': {message}")

# 13. PRACTICAL EXAMPLE: Grade Calculator
print("\n13. Practical Example: Grade Calculator")
print("-" * 30)

def calculate_letter_grade(score):
    """Convert numerical score to letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def calculate_class_average(grades):
    """Calculate the average of a list of grades."""
    if not grades:
        return 0
    return sum(grades) / len(grades)

student_grades = [85, 92, 78, 95, 88]
for grade in student_grades:
    letter = calculate_letter_grade(grade)
    print(f"Score: {grade} → Grade: {letter}")

average = calculate_class_average(student_grades)
print(f"\nClass average: {average:.2f} → {calculate_letter_grade(average)}")

print("\n" + "=" * 50)
print("Examples completed! Now try the exercises.")
print("=" * 50)
