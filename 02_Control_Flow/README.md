# Module 02: Control Flow

Now that you understand Python basics, let's learn how to make your programs make decisions and repeat actions!

## Topics Covered

1. If Statements (Conditional Logic)
2. If-Elif-Else Chains
3. While Loops
4. For Loops
5. Break and Continue
6. Nested Loops

## 1. If Statements

If statements let your program make decisions based on conditions.

```python
age = 18

if age >= 18:
    print("You are an adult")
```

### With Else
```python
age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

## 2. If-Elif-Else Chains

When you have multiple conditions to check:

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

### Multiple Conditions
```python
age = 20
has_license = True

if age >= 18 and has_license:
    print("You can drive")
elif age >= 18 and not has_license:
    print("You need to get a license")
else:
    print("You're too young to drive")
```

## 3. While Loops

While loops repeat code as long as a condition is True.

```python
count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1  # Same as count = count + 1
```

**Warning**: Be careful not to create infinite loops!
```python
# BAD - Infinite loop!
# count = 1
# while count <= 5:
#     print(count)
#     # Forgot to increment count!
```

## 4. For Loops

For loops iterate over sequences (ranges, lists, strings, etc.).

### Looping with range()
```python
# Print numbers 0 to 4
for i in range(5):
    print(i)

# Print numbers 1 to 5
for i in range(1, 6):
    print(i)

# Print numbers 0, 2, 4, 6, 8 (step by 2)
for i in range(0, 10, 2):
    print(i)
```

### Looping through strings
```python
name = "Python"

for letter in name:
    print(letter)
```

## 5. Break and Continue

### Break - Exit the loop entirely
```python
for i in range(10):
    if i == 5:
        break  # Stop when i equals 5
    print(i)
# Output: 0, 1, 2, 3, 4
```

### Continue - Skip to next iteration
```python
for i in range(5):
    if i == 2:
        continue  # Skip when i equals 2
    print(i)
# Output: 0, 1, 3, 4
```

## 6. Nested Loops

Loops inside loops!

```python
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
```

### Practical Example: Multiplication Table
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
```

## Common Patterns

### Counting Pattern
```python
count = 0
for i in range(10):
    if i % 2 == 0:  # Even numbers
        count += 1
print(f"Even numbers: {count}")
```

### Sum Pattern
```python
total = 0
for i in range(1, 11):
    total += i
print(f"Sum of 1-10: {total}")
```

### Search Pattern
```python
numbers = [10, 20, 30, 40, 50]
target = 30
found = False

for num in numbers:
    if num == target:
        found = True
        break

if found:
    print(f"{target} was found!")
else:
    print(f"{target} was not found")
```

## Best Practices

1. **Use meaningful variable names**: `for student in students:` not `for s in students:`
2. **Avoid deeply nested loops**: More than 2-3 levels gets hard to read
3. **Use `range()` when you need the index**: `for i in range(len(items)):`
4. **Use `for` when you know iterations**: Use `while` when the number is unknown
5. **Always have a way to exit**: Prevent infinite loops

## Key Takeaways

- `if/elif/else` - Make decisions in your code
- `while` - Repeat while condition is True
- `for` - Iterate over sequences
- `break` - Exit loop early
- `continue` - Skip current iteration
- Loops can be nested for complex patterns

## Practice

Check `examples.py` to see control flow in action, then complete `exercises.py`!

## Next Module

Master these control structures, then move to [Module 03: Data Structures](../03_Data_Structures/) to learn about lists, dictionaries, and more!
