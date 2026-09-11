# Module 09: Advanced Topics

Explore powerful Python features that make your code more elegant and efficient!

## Topics to Cover

1. **Decorators**
   - What are decorators?
   - Function decorators
   - Creating custom decorators
   - Common use cases (@property, @staticmethod)

2. **Generators**
   - Understanding generators
   - `yield` keyword
   - Generator expressions
   - Memory efficiency
   - Infinite generators

3. **List/Dict/Set Comprehensions (Advanced)**
   - Nested comprehensions
   - Conditional comprehensions
   - Performance considerations

4. **Context Managers**
   - The `with` statement
   - `__enter__` and `__exit__`
   - Creating custom context managers
   - `contextlib` module

5. **Iterators**
   - Iterator protocol
   - `__iter__` and `__next__`
   - Creating custom iterators

6. **Regular Expressions**
   - Pattern matching
   - `re` module
   - Common patterns
   - Validation use cases

7. **Additional Topics**
   - `*args` and `**kwargs`
   - Map, Filter, Reduce
   - Enumerate and Zip
   - Collections module

## Key Concepts

```python
# Decorator example
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        print("Starting function...")
        result = func(*args, **kwargs)
        print("Function complete!")
        return result
    return wrapper

@timing_decorator
def greet(name):
    return f"Hello, {name}"

# Generator example
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)

# Context manager
class FileManager:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager('data.txt') as f:
    content = f.read()

# *args and **kwargs
def flexible_function(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")
```

## Practice Ideas

1. Create a decorator that times function execution
2. Build a generator for Fibonacci sequence
3. Write a custom context manager for database connections
4. Use regex to validate email addresses
5. Create an iterator for a custom collection

## When to Use These Features

- **Decorators**: Add functionality to existing functions (logging, timing, validation)
- **Generators**: Process large data efficiently without loading everything into memory
- **Context Managers**: Ensure resources are properly cleaned up
- **Comprehensions**: Create collections concisely and efficiently

## Coming Soon

Detailed examples and exercises. For now:
- Explore these concepts gradually
- Don't feel pressured to use advanced features everywhere
- Understand when each feature adds value

## Next Module

Apply your knowledge in [Module 10: Projects](../10_Projects/) with real-world applications!
