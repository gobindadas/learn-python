# Control Flow - Interview Questions

## Level: Normal (1-5)

### Question 1: Loop Output Prediction
What will be the output?
```python
for i in range(5):
    if i == 3:
        continue
    print(i, end=" ")
```

### Question 2: While Loop with Else
Explain the purpose of the `else` clause in a while loop. When does it execute?
```python
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Loop completed normally")
```

### Question 3: Nested Loop Break
What happens when you use `break` in a nested loop? Does it break out of all loops or just the innermost one?

### Question 4: Ternary Operator
Rewrite this code using a ternary operator:
```python
if score >= 60:
    result = "Pass"
else:
    result = "Fail"
```

### Question 5: Match Statement (Python 3.10+)
What is the Python `match` statement? How is it different from a series of `if-elif-else`?

## Level: Medium (6-10)

### Question 6: Loop Optimization Challenge
You have this code:
```python
result = []
for i in range(1000):
    if i % 2 == 0:
        result.append(i * 2)
```
Convert it to a list comprehension and explain why it might be faster.

### Question 7: Finding Loop Patterns
What's the difference between these three loops?
```python
# Loop 1
for i in range(len(items)):
    print(items[i])

# Loop 2
for item in items:
    print(item)

# Loop 3
for index, item in enumerate(items):
    print(index, item)
```
When would you use each?

### Question 8: Walrus Operator in Loops
Explain the walrus operator (`:=`) and how it can be used in loops. Provide an example.

### Question 9: Multiple Loop Variables
Write a program that iterates over two lists simultaneously and stops when the shorter list ends. Use `zip()`.

### Question 10: Control Flow Bug
Find and fix the bug:
```python
def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
    else:
        return None
```

## Level: Hard (11-15)

### Question 11: Custom Iterator with Control Flow
Implement a custom range-like function that supports:
- Start, stop, step parameters
- Both positive and negative steps
- Proper StopIteration handling
```python
def my_range(start, stop=None, step=1):
    # Your implementation
    pass
```

### Question 12: State Machine Implementation
Implement a simple state machine for a traffic light (Red → Green → Yellow → Red) using control flow. The system should:
- Accept commands: "next", "reset", "status"
- Validate state transitions
- Handle invalid commands

### Question 13: Loop Performance Analysis
Compare the performance implications:
```python
# Method 1
result = []
for i in range(10000):
    result.append(i ** 2)

# Method 2
result = [i ** 2 for i in range(10000)]

# Method 3
result = list(map(lambda x: x ** 2, range(10000)))

# Method 4
import numpy as np
result = np.arange(10000) ** 2
```
When would you choose each approach?

### Question 14: Complex Conditional Logic
Simplify this nested conditional:
```python
def process_user(user):
    if user is not None:
        if user.is_active:
            if user.has_permission('admin'):
                if user.email_verified:
                    return "Full access granted"
                else:
                    return "Verify email"
            else:
                return "Insufficient permissions"
        else:
            return "Account inactive"
    else:
        return "Invalid user"
```

### Question 15: Generator with Control Flow
Implement a generator function that yields Fibonacci numbers up to a maximum value. Include error handling for invalid inputs.

## Bonus Challenge

### Question 16: Async Control Flow
How does control flow work in asynchronous Python? Explain the difference between:
```python
# Synchronous
for item in items:
    process(item)

# Asynchronous
async for item in items:
    await process(item)
```

### Question 17: Context Managers and Control Flow
Implement a custom context manager that measures execution time. Show how control flow affects the timing measurement.

### Question 18: Recursive vs Iterative
Convert this recursive function to an iterative one:
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```
Discuss the pros and cons of each approach.
