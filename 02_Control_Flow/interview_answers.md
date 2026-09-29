# Control Flow - Interview Answers

## Level: Normal (1-5)

### Answer 1: Loop Output Prediction
**Output:** `0 1 2 4 `

**Explanation:**
- Loop iterates from 0 to 4
- When `i == 3`, `continue` skips the rest of the iteration
- Numbers 0, 1, 2, 4 are printed (3 is skipped)

### Answer 2: While Loop with Else
The `else` clause in a while loop executes when the loop completes normally (condition becomes False), but NOT when the loop is terminated by a `break` statement.

```python
# Executes else
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Loop completed normally")  # This runs

# Does NOT execute else
i = 0
while i < 10:
    if i == 3:
        break
    i += 1
else:
    print("This won't print")  # Skipped due to break
```

**Use case:** Searching in a loop
```python
def find_item(items, target):
    for item in items:
        if item == target:
            print("Found!")
            break
    else:
        print("Not found")  # Only if loop completes without break
```

### Answer 3: Nested Loop Break
`break` only breaks out of the **innermost loop** containing it.

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # Only breaks inner loop
        print(f"i={i}, j={j}")

# Output:
# i=0, j=0
# i=1, j=0
# i=2, j=0

# To break outer loop, use a flag or exception
found = False
for i in range(3):
    for j in range(3):
        if some_condition:
            found = True
            break
    if found:
        break
```

### Answer 4: Ternary Operator
```python
result = "Pass" if score >= 60 else "Fail"
```

**General syntax:** `value_if_true if condition else value_if_false`

**More examples:**
```python
max_val = a if a > b else b
message = "Even" if num % 2 == 0 else "Odd"
status = "Adult" if age >= 18 else "Minor"
```

### Answer 5: Match Statement (Python 3.10+)
The `match` statement is structural pattern matching, more powerful than `if-elif-else`.

```python
# if-elif-else
def describe_number(n):
    if n == 0:
        return "zero"
    elif n == 1:
        return "one"
    elif n > 1:
        return "positive"
    else:
        return "negative"

# match statement
def describe_number(n):
    match n:
        case 0:
            return "zero"
        case 1:
            return "one"
        case n if n > 1:
            return "positive"
        case _:
            return "negative"

# Advanced pattern matching
def process_command(command):
    match command:
        case ["quit"]:
            return "Exiting"
        case ["load", filename]:
            return f"Loading {filename}"
        case ["save", filename, format]:
            return f"Saving {filename} as {format}"
        case _:
            return "Unknown command"
```

**Differences:**
- Match supports destructuring
- Can match sequences, mappings, objects
- More readable for complex patterns
- Guards with `if` conditions

## Level: Medium (6-10)

### Answer 6: Loop Optimization Challenge
```python
# Original
result = []
for i in range(1000):
    if i % 2 == 0:
        result.append(i * 2)

# List comprehension
result = [i * 2 for i in range(1000) if i % 2 == 0]

# Even more efficient (avoid modulo)
result = [i * 2 for i in range(0, 1000, 2)]
```

**Why it's faster:**
1. **C-level optimization**: List comprehensions run at C speed
2. **Pre-allocation**: Python pre-allocates memory
3. **Fewer function calls**: No repeated `.append()` calls
4. **Better bytecode**: More efficient bytecode generation

**Benchmark:**
```python
import timeit

# Loop
time1 = timeit.timeit('''
result = []
for i in range(1000):
    if i % 2 == 0:
        result.append(i * 2)
''', number=10000)

# List comprehension
time2 = timeit.timeit('''
result = [i * 2 for i in range(0, 1000, 2)]
''', number=10000)

print(f"Loop: {time1:.4f}s")
print(f"Comprehension: {time2:.4f}s")
# Comprehension is typically 30-40% faster
```

### Answer 7: Finding Loop Patterns
```python
items = ['a', 'b', 'c']

# Loop 1: Index-based (AVOID unless necessary)
for i in range(len(items)):
    print(items[i])
# Use when: Need to modify list in place, or working with multiple lists

# Loop 2: Direct iteration (PREFERRED)
for item in items:
    print(item)
# Use when: Only need values, most Pythonic

# Loop 3: With enumerate (BEST for index + value)
for index, item in enumerate(items):
    print(index, item)
# Use when: Need both index and value
```

**When to use each:**
```python
# Index-based: Modifying in place
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

# Direct: Simple iteration
for name in names:
    print(f"Hello, {name}")

# Enumerate: Need position
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")
```

### Answer 8: Walrus Operator in Loops
The walrus operator (`:=`) assigns and returns a value in one expression.

```python
# Without walrus operator
line = input("Enter text: ")
while line != "quit":
    process(line)
    line = input("Enter text: ")

# With walrus operator
while (line := input("Enter text: ")) != "quit":
    process(line)

# Reading file chunks
while (chunk := file.read(1024)):
    process(chunk)

# List comprehension with walrus
# Get lengths > 5
data = ["a", "hello", "world", "hi", "python"]
result = [length for item in data if (length := len(item)) > 5]
# result = [5, 6] (lengths of "hello" and "python")

# Avoiding repeated computation
if (match := pattern.search(text)):
    print(match.group(1))
```

### Answer 9: Multiple Loop Variables
```python
def iterate_simultaneously(list1, list2):
    """Iterate over two lists simultaneously"""
    for item1, item2 in zip(list1, list2):
        print(f"List1: {item1}, List2: {item2}")

# Example
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# With more than two lists
scores = [85, 90, 88]
for name, age, score in zip(names, ages, scores):
    print(f"{name}, {age}, scored {score}")

# If lists have different lengths
list1 = [1, 2, 3]
list2 = ['a', 'b']

# zip stops at shortest
for x, y in zip(list1, list2):
    print(x, y)
# Output: 1 a, 2 b

# Use zip_longest for longest
from itertools import zip_longest
for x, y in zip_longest(list1, list2, fillvalue=None):
    print(x, y)
# Output: 1 a, 2 b, 3 None
```

### Answer 10: Control Flow Bug
**Bug:** The `else` clause is attached to the `for` loop, not the `if` statement.

```python
# BUGGY CODE
def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
    else:  # This belongs to 'for', not 'if'
        return None

# The bug: 'else' after 'for' executes if loop completes without break
# Since we use 'return', the else never executes
# The indentation is misleading

# FIXED CODE - Option 1
def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
    return None  # After loop completes

# FIXED CODE - Option 2 (using for-else correctly)
def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
            break  # Unreachable but shows intent
    else:
        return None  # Only if loop completes without break
```

## Level: Hard (11-15)

### Answer 11: Custom Iterator with Control Flow
```python
def my_range(start, stop=None, step=1):
    """
    Custom range implementation
    
    Args:
        start: Starting value (or stop if only one arg)
        stop: Ending value (exclusive)
        step: Step size (can be negative)
    
    Yields:
        Values in range
    """
    # Handle single argument case
    if stop is None:
        start, stop = 0, start
    
    # Validate step
    if step == 0:
        raise ValueError("step cannot be zero")
    
    # Generate values
    current = start
    
    if step > 0:
        while current < stop:
            yield current
            current += step
    else:
        while current > stop:
            yield current
            current += step

# Usage
print(list(my_range(5)))           # [0, 1, 2, 3, 4]
print(list(my_range(2, 8)))        # [2, 3, 4, 5, 6, 7]
print(list(my_range(0, 10, 2)))    # [0, 2, 4, 6, 8]
print(list(my_range(10, 0, -1)))   # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Class-based iterator
class MyRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        
        if step == 0:
            raise ValueError("step cannot be zero")
        self.step = step
        self.current = self.start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.step > 0:
            if self.current >= self.stop:
                raise StopIteration
        else:
            if self.current <= self.stop:
                raise StopIteration
        
        value = self.current
        self.current += self.step
        return value
```

### Answer 12: State Machine Implementation
```python
class TrafficLight:
    """Traffic light state machine"""
    
    STATES = ['Red', 'Green', 'Yellow']
    TRANSITIONS = {
        'Red': 'Green',
        'Green': 'Yellow',
        'Yellow': 'Red'
    }
    
    def __init__(self):
        self.current_state = 'Red'
        self.history = ['Red']
    
    def next(self):
        """Transition to next state"""
        self.current_state = self.TRANSITIONS[self.current_state]
        self.history.append(self.current_state)
        return self.current_state
    
    def reset(self):
        """Reset to initial state"""
        self.current_state = 'Red'
        self.history = ['Red']
        return self.current_state
    
    def status(self):
        """Get current status"""
        return {
            'current': self.current_state,
            'history': self.history.copy(),
            'count': len(self.history)
        }
    
    def process_command(self, command):
        """Process a command"""
        command = command.lower().strip()
        
        if command == 'next':
            return f"Switched to {self.next()}"
        elif command == 'reset':
            self.reset()
            return "Reset to Red"
        elif command == 'status':
            status = self.status()
            return f"Current: {status['current']}, " \
                   f"Changes: {status['count']}"
        else:
            return f"Invalid command: {command}"

# Usage
light = TrafficLight()
print(light.process_command('status'))   # Current: Red, Changes: 1
print(light.process_command('next'))     # Switched to Green
print(light.process_command('next'))     # Switched to Yellow
print(light.process_command('next'))     # Switched to Red
print(light.process_command('invalid'))  # Invalid command
```

### Answer 13: Loop Performance Analysis
```python
import timeit
import numpy as np

# Method 1: List + append
def method1():
    result = []
    for i in range(10000):
        result.append(i ** 2)
    return result

# Method 2: List comprehension
def method2():
    return [i ** 2 for i in range(10000)]

# Method 3: map + lambda
def method3():
    return list(map(lambda x: x ** 2, range(10000)))

# Method 4: NumPy
def method4():
    return np.arange(10000) ** 2

# Benchmark
t1 = timeit.timeit(method1, number=1000)
t2 = timeit.timeit(method2, number=1000)
t3 = timeit.timeit(method3, number=1000)
t4 = timeit.timeit(method4, number=1000)

print(f"Method 1 (append): {t1:.4f}s")
print(f"Method 2 (comprehension): {t2:.4f}s")
print(f"Method 3 (map): {t3:.4f}s")
print(f"Method 4 (numpy): {t4:.4f}s")
```

**When to use each:**

1. **List + append**: Dynamic size unknown, conditional logic
2. **List comprehension**: Best for pure Python, readable, fast
3. **map + lambda**: Functional style, existing function
4. **NumPy**: Large datasets, numerical computing, fastest for arrays

**Typical performance order:**
NumPy > List comprehension ≈ map > append loop

### Answer 14: Complex Conditional Logic
```python
# Original nested version
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

# Simplified Version 1: Guard clauses (Early returns)
def process_user(user):
    if user is None:
        return "Invalid user"
    
    if not user.is_active:
        return "Account inactive"
    
    if not user.has_permission('admin'):
        return "Insufficient permissions"
    
    if not user.email_verified:
        return "Verify email"
    
    return "Full access granted"

# Simplified Version 2: Combined conditions
def process_user(user):
    if user is None:
        return "Invalid user"
    
    if not user.is_active:
        return "Account inactive"
    
    if not user.has_permission('admin'):
        return "Insufficient permissions"
    
    return "Full access granted" if user.email_verified else "Verify email"

# Simplified Version 3: Match statement (Python 3.10+)
def process_user(user):
    match user:
        case None:
            return "Invalid user"
        case user if not user.is_active:
            return "Account inactive"
        case user if not user.has_permission('admin'):
            return "Insufficient permissions"
        case user if not user.email_verified:
            return "Verify email"
        case _:
            return "Full access granted"
```

### Answer 15: Generator with Control Flow
```python
def fibonacci_generator(max_value=None, count=None):
    """
    Generate Fibonacci numbers
    
    Args:
        max_value: Maximum value (exclusive)
        count: Maximum count of numbers
    
    Yields:
        Fibonacci numbers
    
    Raises:
        ValueError: If both or neither parameter is provided
        TypeError: If parameters are not integers
    """
    # Validation
    if max_value is None and count is None:
        raise ValueError("Must provide either max_value or count")
    
    if max_value is not None and count is not None:
        raise ValueError("Provide only one of max_value or count")
    
    if max_value is not None:
        if not isinstance(max_value, int) or max_value < 0:
            raise TypeError("max_value must be a non-negative integer")
    
    if count is not None:
        if not isinstance(count, int) or count < 0:
            raise TypeError("count must be a non-negative integer")
    
    # Generate Fibonacci numbers
    a, b = 0, 1
    generated = 0
    
    try:
        if max_value is not None:
            while a < max_value:
                yield a
                a, b = b, a + b
        else:  # count is not None
            while generated < count:
                yield a
                a, b = b, a + b
                generated += 1
    except GeneratorExit:
        # Clean up if generator is closed early
        print("Generator closed")
        return

# Usage
print("Fibonacci up to 100:")
for num in fibonacci_generator(max_value=100):
    print(num, end=" ")

print("\n\nFirst 10 Fibonacci:")
for num in fibonacci_generator(count=10):
    print(num, end=" ")

# Error handling
try:
    gen = fibonacci_generator()  # Missing parameters
except ValueError as e:
    print(f"\nError: {e}")
```

## Bonus Challenge

### Answer 16: Async Control Flow
```python
import asyncio
import time

# Synchronous version
def sync_process(item):
    time.sleep(1)  # Blocking
    return item * 2

def sync_main():
    items = [1, 2, 3, 4, 5]
    results = []
    for item in items:
        result = sync_process(item)  # Blocks here
        results.append(result)
    return results

# Asynchronous version
async def async_process(item):
    await asyncio.sleep(1)  # Non-blocking
    return item * 2

async def async_main():
    items = [1, 2, 3, 4, 5]
    results = []
    for item in items:
        result = await async_process(item)  # Awaits but allows switching
        results.append(result)
    return results

# Better async version (parallel)
async def async_main_parallel():
    items = [1, 2, 3, 4, 5]
    tasks = [async_process(item) for item in items]
    results = await asyncio.gather(*tasks)  # Run concurrently
    return results

# Async iteration
async def async_generator():
    for i in range(5):
        await asyncio.sleep(0.5)
        yield i

async def consume_async_generator():
    async for item in async_generator():
        print(item)

# Timing comparison
start = time.time()
sync_main()
print(f"Sync time: {time.time() - start:.2f}s")  # ~5 seconds

start = time.time()
asyncio.run(async_main())
print(f"Async sequential: {time.time() - start:.2f}s")  # ~5 seconds

start = time.time()
asyncio.run(async_main_parallel())
print(f"Async parallel: {time.time() - start:.2f}s")  # ~1 second
```

**Key Differences:**
- `for` is blocking, `async for` is non-blocking
- `await` allows other tasks to run during waiting
- Async is beneficial for I/O-bound operations
- CPU-bound tasks should use multiprocessing

### Answer 17: Context Managers and Control Flow
```python
import time
from contextlib import contextmanager

class Timer:
    """Context manager for timing code execution"""
    
    def __init__(self, name="Operation"):
        self.name = name
        self.start_time = None
        self.end_time = None
        self.elapsed = None
    
    def __enter__(self):
        self.start_time = time.time()
        print(f"{self.name} started...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.elapsed = self.end_time - self.start_time
        
        if exc_type is not None:
            print(f"{self.name} failed after {self.elapsed:.4f}s")
            print(f"Error: {exc_val}")
            return False  # Re-raise exception
        
        print(f"{self.name} completed in {self.elapsed:.4f}s")
        return True

# Usage
with Timer("Data processing") as t:
    time.sleep(1)
    result = [i ** 2 for i in range(1000)]

print(f"Elapsed: {t.elapsed:.4f}s")

# Using decorator/generator syntax
@contextmanager
def timer(name="Operation"):
    start = time.time()
    print(f"{name} started...")
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{name} completed in {elapsed:.4f}s")

# Usage
with timer("Database query"):
    time.sleep(0.5)

# Handling exceptions
with Timer("Risky operation"):
    raise ValueError("Something went wrong")
```

### Answer 18: Recursive vs Iterative
```python
# Recursive version
def factorial_recursive(n):
    """Recursive factorial"""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Iterative version
def factorial_iterative(n):
    """Iterative factorial"""
    if n < 0:
        raise ValueError("n must be non-negative")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Tail-recursive version (Python doesn't optimize this)
def factorial_tail(n, accumulator=1):
    """Tail-recursive factorial"""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)

# Test
print(factorial_recursive(5))   # 120
print(factorial_iterative(5))   # 120
print(factorial_tail(5))        # 120
```

**Pros and Cons:**

| Aspect | Recursive | Iterative |
|--------|-----------|-----------|
| Readability | Often clearer for tree/graph problems | Can be more verbose |
| Memory | O(n) stack space | O(1) stack space |
| Speed | Function call overhead | Faster |
| Stack limit | Limited by recursion depth (~1000) | No limit |
| Best for | Tree traversal, divide-and-conquer | Simple loops, large n |

**Performance comparison:**
```python
import sys
sys.setrecursionlimit(10000)

# Recursive fails for large n
try:
    factorial_recursive(2000)
except RecursionError:
    print("Recursive version failed")

# Iterative handles large n
result = factorial_iterative(2000)
print(f"Iterative succeeded: {len(str(result))} digits")
```

**When to use each:**
- **Recursive**: Tree/graph traversal, divide-and-conquer, naturally recursive problems
- **Iterative**: Performance-critical code, large inputs, simple loops
