"""
Module 04: Functions - Solutions
Compare your solutions here!
"""

print("FUNCTIONS - SOLUTIONS")
print("=" * 50)

# Exercise 1: Basic Function
print("\nExercise 1: Create a Simple Function")
print("-" * 30)

def welcome():
    print("Welcome to Python!")

welcome()

# Exercise 2: Function with Parameter
print("\nExercise 2: Greet by Name")
print("-" * 30)

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")

# Exercise 3: Multiple Parameters
print("\nExercise 3: Full Name")
print("-" * 30)

def create_full_name(first, last):
    print(f"{first} {last}")

create_full_name("John", "Doe")

# Exercise 4: Return Value
print("\nExercise 4: Calculate Sum")
print("-" * 30)

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print(f"Sum: {result}")

# Exercise 5: Multiple Returns
print("\nExercise 5: Rectangle Calculator")
print("-" * 30)

def rectangle_calc(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

area, perimeter = rectangle_calc(5, 3)
print(f"Area: {area}, Perimeter: {perimeter}")

# Exercise 6: Default Parameters
print("\nExercise 6: Power Function")
print("-" * 30)

def power(base, exponent=2):
    return base ** exponent

print(f"power(5): {power(5)}")
print(f"power(5, 3): {power(5, 3)}")

# Exercise 7: Temperature Converter
print("\nExercise 7: Celsius to Fahrenheit")
print("-" * 30)

def c_to_f(celsius):
    return (celsius * 9/5) + 32

print(f"0°C = {c_to_f(0)}°F")
print(f"100°C = {c_to_f(100)}°F")
print(f"37°C = {c_to_f(37)}°F")

# Exercise 8: Even or Odd
print("\nExercise 8: Check Even or Odd")
print("-" * 30)

def is_even(number):
    return number % 2 == 0

print(f"is_even(4): {is_even(4)}")
print(f"is_even(7): {is_even(7)}")
print(f"is_even(10): {is_even(10)}")

# Exercise 9: Maximum of Three
print("\nExercise 9: Find Maximum")
print("-" * 30)

def max_of_three(a, b, c):
    return max(a, b, c)

# Alternative without using max()
def max_of_three_alt(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(f"max_of_three(5, 2, 8): {max_of_three(5, 2, 8)}")

# Exercise 10: String Reverser
print("\nExercise 10: Reverse String")
print("-" * 30)

def reverse_string(text):
    return text[::-1]

print(f"reverse_string('Python'): {reverse_string('Python')}")

# Exercise 11: List Sum
print("\nExercise 11: Sum of List")
print("-" * 30)

def sum_list(numbers):
    return sum(numbers)

# Alternative without using sum()
def sum_list_alt(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
print(f"sum_list({numbers}): {sum_list(numbers)}")

# Exercise 12: Factorial
print("\nExercise 12: Calculate Factorial")
print("-" * 30)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"factorial(5): {factorial(5)}")
print(f"factorial(7): {factorial(7)}")

# Exercise 13: Prime Checker
print("\nExercise 13: Check Prime Number")
print("-" * 30)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(f"is_prime(7): {is_prime(7)}")
print(f"is_prime(10): {is_prime(10)}")
print(f"is_prime(13): {is_prime(13)}")

# Exercise 14: Lambda Function
print("\nExercise 14: Lambda for Cube")
print("-" * 30)

cube = lambda x: x ** 3

print(f"cube(3): {cube(3)}")
print(f"cube(5): {cube(5)}")

# Exercise 15: Filter with Lambda
print("\nExercise 15: Filter Multiples")
print("-" * 30)

numbers = [5, 12, 15, 20, 23, 30]
multiples_of_5 = list(filter(lambda x: x % 5 == 0, numbers))
print(f"Multiples of 5: {multiples_of_5}")

# Exercise 16: Sort with Lambda
print("\nExercise 16: Sort by Length")
print("-" * 30)

words = ['Python', 'is', 'awesome', 'language']
sorted_words = sorted(words, key=lambda x: len(x))
print(f"Sorted by length: {sorted_words}")

# Exercise 17: Count Vowels
print("\nExercise 17: Vowel Counter")
print("-" * 30)

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Alternative using sum
def count_vowels_alt(text):
    return sum(1 for char in text if char.lower() in "aeiou")

print(f"count_vowels('Education'): {count_vowels('Education')}")

# Exercise 18: Palindrome Checker
print("\nExercise 18: Check Palindrome")
print("-" * 30)

def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

print(f"is_palindrome('radar'): {is_palindrome('radar')}")
print(f"is_palindrome('python'): {is_palindrome('python')}")

# Exercise 19: FizzBuzz Function
print("\nExercise 19: FizzBuzz Function")
print("-" * 30)

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

print(f"fizzbuzz(3): {fizzbuzz(3)}")
print(f"fizzbuzz(5): {fizzbuzz(5)}")
print(f"fizzbuzz(15): {fizzbuzz(15)}")
print(f"fizzbuzz(7): {fizzbuzz(7)}")

# Exercise 20: Bonus - Calculator
print("\nExercise 20: Bonus - Calculator Function")
print("-" * 30)

def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Error: Invalid operation"

print(f"calculator(10, 5, '+'): {calculator(10, 5, '+')}")
print(f"calculator(10, 5, '*'): {calculator(10, 5, '*')}")
print(f"calculator(10, 0, '/'): {calculator(10, 0, '/')}")

print("\n" + "=" * 50)
print("All solutions completed!")
print("=" * 50)

print("\nKey Concepts Demonstrated:")
print("- Function definition and calling")
print("- Parameters and arguments (positional and keyword)")
print("- Return values (single and multiple)")
print("- Default parameters for flexibility")
print("- Lambda functions for simple operations")
print("- Using functions with map(), filter(), sorted()")
print("- Common algorithms: factorial, prime checking, palindromes")
print("- Error handling in functions (division by zero)")
