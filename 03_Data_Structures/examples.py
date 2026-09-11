"""
Module 03: Data Structures - Examples
Explore lists, tuples, dictionaries, and sets!
"""

print("=" * 50)
print("DATA STRUCTURES - EXAMPLES")
print("=" * 50)

# 1. LISTS - Creation and Access
print("\n1. Lists - Creation and Access")
print("-" * 30)

fruits = ["apple", "banana", "cherry", "date"]
print(f"Fruits list: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"First two fruits: {fruits[0:2]}")

# 2. LISTS - Modification
print("\n2. Lists - Modification")
print("-" * 30)

numbers = [1, 2, 3]
print(f"Original: {numbers}")

numbers.append(4)
print(f"After append(4): {numbers}")

numbers.insert(0, 0)
print(f"After insert(0, 0): {numbers}")

numbers.remove(2)
print(f"After remove(2): {numbers}")

popped = numbers.pop()
print(f"After pop(): {numbers}, popped value: {popped}")

# 3. LIST METHODS
print("\n3. List Methods")
print("-" * 30)

values = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original list: {values}")

values.sort()
print(f"After sort(): {values}")

values.reverse()
print(f"After reverse(): {values}")

count_1 = values.count(1)
print(f"Count of 1: {count_1}")

index_5 = values.index(5)
print(f"Index of 5: {index_5}")

# 4. TUPLES
print("\n4. Tuples")
print("-" * 30)

coordinates = (10, 20)
person = ("Alice", 25, "Engineer")

print(f"Coordinates: {coordinates}")
print(f"Person: {person}")
print(f"Name: {person[0]}, Age: {person[1]}")

# Tuple unpacking
x, y = coordinates
name, age, job = person
print(f"Unpacked coordinates: x={x}, y={y}")
print(f"Unpacked person: {name}, {age}, {job}")

# 5. DICTIONARIES - Creation and Access
print("\n5. Dictionaries - Creation and Access")
print("-" * 30)

student = {
    "name": "Bob",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics"]
}

print(f"Student dict: {student}")
print(f"Name: {student['name']}")
print(f"Age: {student.get('age')}")
print(f"Email: {student.get('email', 'Not provided')}")

# 6. DICTIONARIES - Modification
print("\n6. Dictionaries - Modification")
print("-" * 30)

inventory = {"apples": 10, "bananas": 5}
print(f"Original inventory: {inventory}")

inventory["oranges"] = 8
print(f"After adding oranges: {inventory}")

inventory["apples"] = 15
print(f"After updating apples: {inventory}")

removed = inventory.pop("bananas")
print(f"After removing bananas: {inventory}, removed: {removed}")

# 7. DICTIONARIES - Looping
print("\n7. Dictionaries - Looping")
print("-" * 30)

prices = {"apple": 0.5, "banana": 0.3, "orange": 0.6}

print("Keys:")
for key in prices.keys():
    print(f"  {key}")

print("Values:")
for value in prices.values():
    print(f"  ${value}")

print("Key-Value pairs:")
for fruit, price in prices.items():
    print(f"  {fruit}: ${price}")

# 8. SETS - Creation and Operations
print("\n8. Sets - Creation and Operations")
print("-" * 30)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

print(f"Union (|): {set1 | set2}")
print(f"Intersection (&): {set1 & set2}")
print(f"Difference (-): {set1 - set2}")
print(f"Symmetric Diff (^): {set1 ^ set2}")

# 9. SETS - Removing Duplicates
print("\n9. Sets - Removing Duplicates")
print("-" * 30)

numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
print(f"List with duplicates: {numbers_with_duplicates}")

unique_numbers = list(set(numbers_with_duplicates))
print(f"After removing duplicates: {unique_numbers}")

# 10. LIST COMPREHENSIONS
print("\n10. List Comprehensions")
print("-" * 30)

# Squares
squares = [x**2 for x in range(6)]
print(f"Squares: {squares}")

# Even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(f"Evens: {evens}")

# Transform strings
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print(f"Uppercase names: {upper_names}")

# 11. DICTIONARY COMPREHENSION
print("\n11. Dictionary Comprehension")
print("-" * 30)

# Create dict of squares
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares dict: {squares_dict}")

# Transform existing dict
prices = {"apple": 1.0, "banana": 0.5}
discounted = {item: price * 0.9 for item, price in prices.items()}
print(f"Discounted prices: {discounted}")

# 12. NESTED STRUCTURES
print("\n12. Nested Structures")
print("-" * 30)

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

print("Students:")
for student in students:
    print(f"  {student['name']}: {student['grade']}")

# 13. PRACTICAL EXAMPLE: Grade Book
print("\n13. Practical Example: Grade Book")
print("-" * 30)

gradebook = {
    "Alice": [85, 90, 92],
    "Bob": [78, 82, 88],
    "Charlie": [92, 95, 98]
}

for student, grades in gradebook.items():
    average = sum(grades) / len(grades)
    print(f"{student}: grades={grades}, average={average:.2f}")

# 14. PRACTICAL EXAMPLE: Shopping Cart
print("\n14. Practical Example: Shopping Cart")
print("-" * 30)

cart = {
    "apple": {"price": 0.5, "quantity": 5},
    "banana": {"price": 0.3, "quantity": 10},
    "orange": {"price": 0.6, "quantity": 3}
}

total = 0
print("Shopping Cart:")
for item, details in cart.items():
    subtotal = details["price"] * details["quantity"]
    total += subtotal
    print(f"  {item}: ${details['price']} x {details['quantity']} = ${subtotal:.2f}")

print(f"Total: ${total:.2f}")

# 15. PRACTICAL EXAMPLE: Word Frequency
print("\n15. Practical Example: Word Frequency")
print("-" * 30)

text = "hello world hello python python python"
words = text.split()

frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequency:")
for word, count in frequency.items():
    print(f"  {word}: {count}")

print("\n" + "=" * 50)
print("Examples completed! Now try the exercises.")
print("=" * 50)
