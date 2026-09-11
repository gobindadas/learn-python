"""
Module 02: Control Flow - Solutions
Compare your solutions with these!
"""

print("CONTROL FLOW - SOLUTIONS")
print("=" * 50)

# Exercise 1: Simple If Statement
print("\nExercise 1: Age Checker")
print("-" * 30)

user_age = 15

if user_age >= 13:
    print("You can create a social media account")
else:
    print("You are too young for social media")

# Exercise 2: If-Elif-Else Chain
print("\nExercise 2: Grade Calculator")
print("-" * 30)

test_score = 76

if test_score >= 90:
    print("Grade: A")
elif test_score >= 80:
    print("Grade: B")
elif test_score >= 70:
    print("Grade: C")
elif test_score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Exercise 3: Multiple Conditions
print("\nExercise 3: Ticket Price Calculator")
print("-" * 30)

age = 25
is_student = True

if age < 12:
    price = 5
    print(f"Child ticket: ${price}")
elif is_student:
    price = 7
    print(f"Student ticket: ${price}")
elif age >= 65:
    price = 6
    print(f"Senior ticket: ${price}")
else:
    price = 10
    print(f"Adult ticket: ${price}")

# Exercise 4: While Loop
print("\nExercise 4: Countdown Timer")
print("-" * 30)

count = 10
while count > 0:
    print(count)
    count -= 1
print("Happy New Year!")

# Exercise 5: While Loop with Accumulator
print("\nExercise 5: Sum Calculator")
print("-" * 30)

total = 0
num = 1
while num <= 100:
    total += num
    num += 1
print(f"Sum of 1 to 100: {total}")

# Exercise 6: For Loop with Range
print("\nExercise 6: Multiplication Table")
print("-" * 30)

for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# Exercise 7: For Loop with String
print("\nExercise 7: Vowel Counter")
print("-" * 30)

word = "Education"
vowel_count = 0

for letter in word:
    if letter.lower() in "aeiou":
        vowel_count += 1

print(f"The word '{word}' has {vowel_count} vowels")

# Exercise 8: Break Statement
print("\nExercise 8: Find First Multiple")
print("-" * 30)

for num in range(1, 101):
    if num % 6 == 0 and num % 7 == 0:
        print(f"First number divisible by both 6 and 7: {num}")
        break

# Exercise 9: Continue Statement
print("\nExercise 9: Skip Multiples")
print("-" * 30)

for num in range(1, 21):
    if num % 3 == 0:
        continue
    print(num, end=" ")
print()

# Exercise 10: Nested Loops - Pattern
print("\nExercise 10: Number Triangle")
print("-" * 30)

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Exercise 11: Nested Loops - Grid
print("\nExercise 11: Multiplication Grid")
print("-" * 30)

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")
    print()

# Exercise 12: FizzBuzz
print("\nExercise 12: FizzBuzz Challenge")
print("-" * 30)

for num in range(1, 31):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz", end=" ")
    elif num % 3 == 0:
        print("Fizz", end=" ")
    elif num % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(num, end=" ")
print()

# Exercise 13: Prime Number Checker
print("\nExercise 13: Prime Number Checker")
print("-" * 30)

number = 17
is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")

# Exercise 14: Factorial Calculator
print("\nExercise 14: Factorial Calculator")
print("-" * 30)

num = 6
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"{num}! = {factorial}")

# Exercise 15: Bonus Challenge - Password Validator
print("\nExercise 15: Password Validator")
print("-" * 30)

password = "Python123"
is_valid = True

# Check length
if len(password) < 8:
    is_valid = False
    print("Password too short")

# Check for digit
has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True
        break

if not has_digit:
    is_valid = False
    print("Password needs a digit")

# Check for uppercase
has_upper = False
for char in password:
    if char.isupper():
        has_upper = True
        break

if not has_upper:
    is_valid = False
    print("Password needs an uppercase letter")

if is_valid:
    print("Valid password")
else:
    print("Invalid password")

print("\n" + "=" * 50)
print("All solutions completed!")
print("=" * 50)

print("\nKey Concepts Demonstrated:")
print("- If/elif/else for decision making")
print("- While loops for condition-based iteration")
print("- For loops for definite iteration")
print("- Break to exit loops early")
print("- Continue to skip iterations")
print("- Nested loops for multi-dimensional patterns")
print("- Common algorithms: FizzBuzz, prime checking, factorial")
