"""
Module 03: Data Structures - Solutions
Compare your answers with these solutions!
"""

print("DATA STRUCTURES - SOLUTIONS")
print("=" * 50)

# Exercise 1: List Basics
print("\nExercise 1: Create and Modify a List")
print("-" * 30)

movies = ["Inception", "Matrix", "Interstellar", "Shawshank", "Dark Knight"]
print(f"First movie: {movies[0]}")
print(f"Last movie: {movies[-1]}")

movies.append("Gladiator")
print(f"After adding movie: {movies}")

movies.remove(movies[1])
print(f"After removing second movie: {movies}")

# Exercise 2: List Slicing
print("\nExercise 2: List Slicing")
print("-" * 30)

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"First 3: {numbers[0:3]}")
print(f"Last 3: {numbers[-3:]}")
print(f"Every second: {numbers[::2]}")

# Exercise 3: List Methods
print("\nExercise 3: List Methods")
print("-" * 30)

scores = [78, 92, 85, 92, 67, 88, 92]
print(f"Original: {scores}")

scores.sort()
print(f"Sorted: {scores}")

count_92 = scores.count(92)
print(f"Count of 92: {count_92}")

index_67 = scores.index(67)
print(f"Index of 67: {index_67}")

scores.reverse()
print(f"Reversed: {scores}")

# Exercise 4: Tuples
print("\nExercise 4: Tuple Unpacking")
print("-" * 30)

location = ('Tokyo', 'Japan', 14000000)
city, country, population = location

print(f"City: {city}")
print(f"Country: {country}")
print(f"Population: {population:,}")

# Exercise 5: Dictionary Basics
print("\nExercise 5: Create a Dictionary")
print("-" * 30)

book = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
    "pages": 328
}

print("Book information:")
for key, value in book.items():
    print(f"  {key}: {value}")

book["genre"] = "Dystopian"
book["year"] = 1950

print(f"\nUpdated book: {book}")

# Exercise 6: Dictionary Access
print("\nExercise 6: Safe Dictionary Access")
print("-" * 30)

user = {'name': 'Alice', 'age': 25}

name = user['name']
print(f"Name: {name}")

email = user.get('email', 'No email')
print(f"Email: {email}")

if 'age' in user:
    print("Age exists in dictionary")

# Exercise 7: Dictionary Looping
print("\nExercise 7: Loop Through Dictionary")
print("-" * 30)

prices = {
    "apple": 0.5,
    "banana": 0.3,
    "orange": 0.6
}

total = 0
for item, price in prices.items():
    print(f"{item}: ${price}")
    total += price

print(f"Total: ${total:.2f}")

# Exercise 8: Sets
print("\nExercise 8: Set Operations")
print("-" * 30)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Union: {set_a | set_b}")
print(f"Intersection: {set_a & set_b}")
print(f"Difference (a-b): {set_a - set_b}")

# Exercise 9: Remove Duplicates
print("\nExercise 9: Remove Duplicates with Sets")
print("-" * 30)

tags = ['python', 'java', 'python', 'c++', 'java', 'ruby']
print(f"Original: {tags}")

unique_tags = sorted(list(set(tags)))
print(f"Unique and sorted: {unique_tags}")

# Exercise 10: List Comprehension - Basic
print("\nExercise 10: List Comprehension - Squares")
print("-" * 30)

cubes = [x**3 for x in range(1, 11)]
print(f"Cubes: {cubes}")

# Exercise 11: List Comprehension - Filter
print("\nExercise 11: List Comprehension with Condition")
print("-" * 30)

multiples_of_3 = [x for x in range(1, 21) if x % 3 == 0]
print(f"Multiples of 3: {multiples_of_3}")

# Exercise 12: Dictionary Comprehension
print("\nExercise 12: Dictionary Comprehension")
print("-" * 30)

squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dictionary: {squares_dict}")

# Exercise 13: Nested Structures
print("\nExercise 13: List of Dictionaries")
print("-" * 30)

students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 21, "grade": "B"},
    {"name": "Charlie", "age": 19, "grade": "A"}
]

print("Students:")
for student in students:
    print(f"  {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

# Exercise 14: Practical - Contact Book
print("\nExercise 14: Contact Book")
print("-" * 30)

contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}

# Look up one contact
print(f"Alice's number: {contacts.get('Alice', 'Not found')}")

# Print all contacts
print("\nAll contacts:")
for name, phone in contacts.items():
    print(f"  {name}: {phone}")

# Exercise 15: Practical - Inventory Manager
print("\nExercise 15: Inventory Manager")
print("-" * 30)

inventory = {
    "apples": 50,
    "bananas": 15,
    "oranges": 8
}

print(f"Initial inventory: {inventory}")

# Add units
inventory["apples"] += 5
print(f"After adding apples: {inventory}")

# Remove out of stock
inventory["grapes"] = 0
del inventory["grapes"]

# Print items with quantity > 10
print("Items with quantity > 10:")
for item, qty in inventory.items():
    if qty > 10:
        print(f"  {item}: {qty}")

# Exercise 16: Bonus - Word Counter
print("\nExercise 16: Bonus - Word Counter")
print("-" * 30)

sentence = 'the quick brown fox jumps over the lazy dog'
words = sentence.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequencies:")
for word, count in word_count.items():
    print(f"  {word}: {count}")

# Alternative using get()
word_count_alt = {}
for word in words:
    word_count_alt[word] = word_count_alt.get(word, 0) + 1

# Exercise 17: Bonus - Two Lists to Dictionary
print("\nExercise 17: Bonus - Combine Lists")
print("-" * 30)

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'NYC']

# Method 1: Using zip()
person_dict = dict(zip(keys, values))
print(f"Using zip(): {person_dict}")

# Method 2: Using loop
person_dict2 = {}
for i in range(len(keys)):
    person_dict2[keys[i]] = values[i]
print(f"Using loop: {person_dict2}")

# Method 3: Dictionary comprehension
person_dict3 = {keys[i]: values[i] for i in range(len(keys))}
print(f"Using comprehension: {person_dict3}")

print("\n" + "=" * 50)
print("All solutions completed!")
print("=" * 50)

print("\nKey Concepts Demonstrated:")
print("- List operations: slicing, methods, modification")
print("- Tuple unpacking for multiple assignment")
print("- Dictionary access, modification, and iteration")
print("- Set operations for mathematical operations")
print("- Removing duplicates efficiently with sets")
print("- List and dictionary comprehensions")
print("- Nested data structures")
print("- Practical applications: contacts, inventory, word counting")
