"""
Module 01: Python Basics - Solutions
Compare your solutions with these answers.
Remember: There might be multiple correct ways to solve each exercise!
"""

print("PYTHON BASICS - SOLUTIONS")
print("=" * 50)

# Exercise 1: Variables and Data Types
print("\nExercise 1: Create Variables")
print("-" * 30)

your_name = "Alice"
your_age = 25
your_height = 1.75
is_learning_python = True

print(f"Name: {your_name}")
print(f"Age: {your_age}")
print(f"Height: {your_height} meters")
print(f"Learning Python: {is_learning_python}")

# Exercise 2: Arithmetic Operations
print("\nExercise 2: Calculate Rectangle Properties")
print("-" * 30)

length = 10
width = 5

area = length * width
perimeter = 2 * (length + width)

print(f"Rectangle - Length: {length}, Width: {width}")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

# Exercise 3: Type Conversion
print("\nExercise 3: Type Conversions")
print("-" * 30)

str_to_int = int('987')
print(f"String '987' to integer: {str_to_int}, type: {type(str_to_int)}")

float_to_int = int(7.89)
print(f"Float 7.89 to integer: {float_to_int}, type: {type(float_to_int)}")

int_to_str = str(100)
print(f"Integer 100 to string: '{int_to_str}', type: {type(int_to_str)}")

int_to_bool = bool(0)
print(f"Integer 0 to boolean: {int_to_bool}, type: {type(int_to_bool)}")

# Exercise 4: String Operations
print("\nExercise 4: String Manipulation")
print("-" * 30)

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

print(f"Full name: {full_name}")
print(f"Repeated 3 times: {full_name * 3}")

# Alternative with separator
print(f"Repeated with separator: {(full_name + ' ') * 3}")

# Exercise 5: Comparison and Logical Operators
print("\nExercise 5: Logical Checks")
print("-" * 30)

age = 16
has_adult = True
has_ticket = False

can_watch_pg13 = age >= 13
can_watch_r_rated = age >= 17 or has_adult
can_enter = has_ticket and can_watch_pg13

print(f"Age: {age}, Has adult: {has_adult}, Has ticket: {has_ticket}")
print(f"Can watch PG-13: {can_watch_pg13}")
print(f"Can watch R-rated: {can_watch_r_rated}")
print(f"Can enter theater: {can_enter}")

# Exercise 6: Input and Output
print("\nExercise 6: User Input")
print("-" * 30)
print("(Solution shown as code, not executed)")

solution_code = """
name = input("What is your name? ")
age = input("What is your age? ")
print(f"Hello {name}, you are {age} years old!")
"""
print(solution_code)

# Exercise 7: Temperature Converter
print("\nExercise 7: Temperature Conversion")
print("-" * 30)

fahrenheit = 100
celsius = (fahrenheit - 32) * 5/9

print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

# Exercise 8: Circle Calculator
print("\nExercise 8: Circle Properties")
print("-" * 30)

radius = 7
pi = 3.14159

area = pi * radius ** 2
circumference = 2 * pi * radius

print(f"Circle with radius: {radius}")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")

# Exercise 9: Price Calculator
print("\nExercise 9: Shopping Cart Total")
print("-" * 30)

item1 = 12.99
item2 = 7.50
item3 = 23.75

subtotal = item1 + item2 + item3
tax = subtotal * 0.08
total = subtotal + tax

print(f"Item 1: ${item1}")
print(f"Item 2: ${item2}")
print(f"Item 3: ${item3}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total: ${total:.2f}")

# Exercise 10: Bonus Challenge
print("\nExercise 10: Time Converter")
print("-" * 30)

total_seconds = 3665

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"Total seconds: {total_seconds}")
print(f"Converted: {hours} hours, {minutes} minutes, {seconds} seconds")

# Alternative one-liner approach
print(f"Alternative calculation: {total_seconds // 3600}h {(total_seconds % 3600) // 60}m {total_seconds % 60}s")

print("\n" + "=" * 50)
print("All solutions completed!")
print("=" * 50)

# Additional Notes
print("\nKey Learning Points:")
print("- Variable naming should be descriptive")
print("- Type conversion is important when working with different data types")
print("- String concatenation uses + operator")
print("- Floor division (//) and modulus (%) are useful for conversions")
print("- f-strings are the modern way to format output")
print("- .2f in f-strings formats numbers to 2 decimal places")
