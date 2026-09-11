"""
Module 02: Control Flow - Examples
Run this file to see conditional logic and loops in action.
"""

print("=" * 50)
print("CONTROL FLOW - EXAMPLES")
print("=" * 50)

# 1. IF STATEMENTS
print("\n1. If Statements")
print("-" * 30)

temperature = 75

if temperature > 80:
    print("It's hot outside!")

if temperature <= 80:
    print("The weather is pleasant")

# If-else
age = 20
if age >= 18:
    print(f"Age {age}: You can vote")
else:
    print(f"Age {age}: You cannot vote yet")

# 2. IF-ELIF-ELSE CHAINS
print("\n2. If-Elif-Else Chains")
print("-" * 30)

score = 87

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Multiple conditions
age = 25
has_license = True

if age >= 18 and has_license:
    print("Status: Can drive legally")
elif age >= 18:
    print("Status: Need to get license first")
else:
    print("Status: Too young to drive")

# 3. WHILE LOOPS
print("\n3. While Loops")
print("-" * 30)

# Simple countdown
count = 5
print("Countdown:")
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

# Accumulator pattern
total = 0
number = 1
while number <= 5:
    total += number
    number += 1
print(f"Sum of 1-5: {total}")

# 4. FOR LOOPS WITH RANGE
print("\n4. For Loops with Range")
print("-" * 30)

# Basic range
print("Numbers 0-4:")
for i in range(5):
    print(i, end=" ")
print()

# Range with start and end
print("Numbers 1-5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# Range with step
print("Even numbers 0-10:")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# 5. FOR LOOPS WITH STRINGS
print("\n5. For Loops with Strings")
print("-" * 30)

word = "Python"
print(f"Letters in '{word}':")
for letter in word:
    print(letter, end=" ")
print()

# Count vowels
vowels = 0
for letter in word:
    if letter.lower() in "aeiou":
        vowels += 1
print(f"Number of vowels: {vowels}")

# 6. BREAK STATEMENT
print("\n6. Break Statement")
print("-" * 30)

print("Finding first number divisible by 7:")
for num in range(1, 100):
    if num % 7 == 0:
        print(f"Found: {num}")
        break

# Search pattern
numbers = [3, 7, 12, 18, 24, 30]
target = 18
print(f"\nSearching for {target} in {numbers}:")
for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found")

# 7. CONTINUE STATEMENT
print("\n7. Continue Statement")
print("-" * 30)

print("Odd numbers from 1-10:")
for i in range(1, 11):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(i, end=" ")
print()

# 8. NESTED LOOPS
print("\n8. Nested Loops")
print("-" * 30)

print("Multiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i}x{j}={result:2}", end="  ")
    print()  # New line after each row

# 9. PRACTICAL EXAMPLE: Pattern Printing
print("\n9. Practical Example: Pattern Printing")
print("-" * 30)

print("Triangle pattern:")
for i in range(1, 6):
    print("*" * i)

print("\nReverse triangle:")
for i in range(5, 0, -1):
    print("*" * i)

# 10. PRACTICAL EXAMPLE: Number Guessing Game
print("\n10. Practical Example: Number Guessing Game")
print("-" * 30)

secret_number = 42
max_attempts = 5
print("(Pre-set guesses to demonstrate logic)")

guesses = [30, 50, 45, 42]  # Simulated guesses
for attempt in range(1, max_attempts + 1):
    if attempt - 1 >= len(guesses):
        break

    guess = guesses[attempt - 1]
    print(f"Attempt {attempt}: Guessed {guess}")

    if guess == secret_number:
        print(f"Correct! You found it in {attempt} attempts!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Out of attempts! The number was {secret_number}")

# 11. PRACTICAL EXAMPLE: FizzBuzz
print("\n11. Practical Example: FizzBuzz")
print("-" * 30)

print("FizzBuzz (1-20):")
for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz", end=" ")
    elif num % 3 == 0:
        print("Fizz", end=" ")
    elif num % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(num, end=" ")
print()

# 12. PRACTICAL EXAMPLE: Sum of Even Numbers
print("\n12. Practical Example: Sum of Even Numbers")
print("-" * 30)

total_even = 0
for num in range(1, 21):
    if num % 2 == 0:
        total_even += num

print(f"Sum of even numbers 1-20: {total_even}")

print("\n" + "=" * 50)
print("Examples completed! Now try the exercises.")
print("=" * 50)
