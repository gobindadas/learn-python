# Functions - Interview Answers

## Level: Normal (1-5)

### Answer 1: Function Arguments
```python
def func(a, b, c=10):
    """
    a, b: positional required arguments
    c: optional argument with default value 10
    """
    print(f"a={a}, b={b}, c={c}")

func(1, 2)        # a=1, b=2, c=10 (default)
func(1, 2, 3)     # a=1, b=2, c=3 (overrides default)
func(a=1, b=2, c=3)  # a=1, b=2, c=3 (keyword arguments)
func(1, b=2)      # a=1, b=2, c=10 (mixed)
func(b=2, a=1)    # a=1, b=2, c=10 (keyword order doesn't matter)
```

**Argument types:**
```python
def example(pos_only, /, pos_or_kw, *, kw_only):
    """
    pos_only: Positional-only (before /)
    pos_or_kw: Can be positional or keyword
    kw_only: Keyword-only (after *)
    """
    pass

# Python 3.8+ syntax
example(1, 2, kw_only=3)  # Valid
example(1, pos_or_kw=2, kw_only=3)  # Valid
# example(pos_only=1, pos_or_kw=2, kw_only=3)  # Error
```

### Answer 2: Return Values
**Output:** `None`

**Explanation:**
- Functions without explicit `return` statement return `None`
- `None` is Python's null value

```python
def mystery():
    x = 10
    y = 20
    # Implicitly returns None

result = mystery()
print(result)  # None
print(type(result))  # <class 'NoneType'>

# Equivalent to:
def mystery():
    x = 10
    y = 20
    return None
```

### Answer 3: Variable Scope
**Output:**
```
inner
outer
global
```

**Explanation: LEGB Rule**
- **L**ocal: Inside current function
- **E**nclosing: In outer functions
- **G**lobal: Module level
- **B**uilt-in: Python built-ins

```python
x = "global"  # Global scope

def outer():
    x = "outer"  # Enclosing scope for inner()
    
    def inner():
        x = "inner"  # Local scope
        print(x)  # "inner" (local)
    
    inner()
    print(x)  # "outer" (local to outer)

outer()
print(x)  # "global" (global scope)

# Modifying enclosing/global scope
def outer():
    x = "outer"
    
    def inner():
        nonlocal x  # Modify enclosing scope
        x = "modified"
    
    inner()
    print(x)  # "modified"

x = "global"
def modify_global():
    global x  # Modify global scope
    x = "modified"

modify_global()
print(x)  # "modified"
```

### Answer 4: Mutable Default Arguments
**Problem:** Default arguments are evaluated once at function definition, not each call.

```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - WRONG! Same list
print(add_item(3))  # [1, 2, 3] - WRONG!

# The default [] is created once and reused
```

**Solution:**
```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [2] - Correct!
print(add_item(3))  # [3] - Correct!

# Or using factory function
from typing import List

def add_item(item, items=None):
    items = items if items is not None else []
    items.append(item)
    return items
```

### Answer 5: *args and **kwargs
**\*args:** Captures variable positional arguments as tuple
**\*\*kwargs:** Captures variable keyword arguments as dict

```python
def example(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

example(1, 2, 3, name="Alice", age=25)
# args: (1, 2, 3)
# kwargs: {'name': 'Alice', 'age': 25}

# Complete signature
def func(pos1, pos2, *args, kw1=None, **kwargs):
    pass

func(1, 2, 3, 4, kw1="value", extra="data")

# Unpacking
def add(a, b, c):
    return a + b + c

values = [1, 2, 3]
print(add(*values))  # Unpacks to add(1, 2, 3)

params = {'a': 1, 'b': 2, 'c': 3}
print(add(**params))  # Unpacks to add(a=1, b=2, c=3)
```

## Level: Medium (6-10)

### Answer 6: Closures
**Problem:** Late binding - all lambdas capture same variable

```python
# Wrong
functions = []
for i in range(3):
    functions.append(lambda: i)  # Captures reference to i

for f in functions:
    print(f())  # All print 2, 2, 2

# Fix 1: Default argument (early binding)
functions = []
for i in range(3):
    functions.append(lambda x=i: x)

for f in functions:
    print(f())  # 0, 1, 2

# Fix 2: Factory function
def make_func(x):
    return lambda: x

functions = [make_func(i) for i in range(3)]
for f in functions:
    print(f())  # 0, 1, 2

# Fix 3: functools.partial
from functools import partial

def print_value(x):
    return x

functions = [partial(print_value, i) for i in range(3)]
```

**Closure example:**
```python
def make_multiplier(n):
    """Closure captures n from enclosing scope"""
    def multiplier(x):
        return x * n  # n is from outer scope
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15

# Inspect closure
print(double.__closure__)  # Contains cell with n=2
print(double.__closure__[0].cell_contents)  # 2
```

### Answer 7: Decorators
```python
import time
import functools

def timer(func):
    """Decorator to measure execution time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        
        result = func(*args, **kwargs)
        
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        
        return result
    
    return wrapper

# Usage
@timer
def slow_function(n):
    """Simulates slow operation"""
    time.sleep(n)
    return n * 2

result = slow_function(1)
# Output:
# Calling slow_function with args=(1,), kwargs={}
# slow_function took 1.0001s

# Multiple decorators
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"LOG: Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
@timer
def my_func():
    time.sleep(0.5)

# Executes logger(timer(my_func))
```

### Answer 8: Generator vs Regular Function
```python
def regular_range(n):
    """Stores all values in memory"""
    result = []
    for i in range(n):
        result.append(i)
    return result  # Returns list

def generator_range(n):
    """Yields values one at a time"""
    for i in range(n):
        yield i  # Returns generator

# Memory usage
import sys

n = 1000000

# Regular function
reg = regular_range(n)
print(f"List size: {sys.getsizeof(reg):,} bytes")  # ~8MB

# Generator
gen = generator_range(n)
print(f"Generator size: {sys.getsizeof(gen):,} bytes")  # ~200 bytes

# When to use each:
# Regular: Need all values, multiple iterations, small dataset
for x in regular_range(10):
    print(x)

# Generator: Large dataset, single iteration, lazy evaluation
for x in generator_range(10):
    print(x)

# Generator is consumed after iteration
gen = generator_range(3)
print(list(gen))  # [0, 1, 2]
print(list(gen))  # [] - exhausted!

# Generator expressions
gen_expr = (x**2 for x in range(10))  # Generator
list_comp = [x**2 for x in range(10)]  # List
```

### Answer 9: Function as First-Class Objects
```python
# 1. Assign to variable
def greet():
    return "Hello!"

say_hello = greet
print(say_hello())  # "Hello!"

# 2. Pass as argument
def apply_func(func, value):
    return func(value)

def square(x):
    return x ** 2

print(apply_func(square, 5))  # 25

# 3. Return from function
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add_5 = make_adder(5)
print(add_5(10))  # 15

# 4. Store in data structure
operations = {
    'add': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mul': lambda a, b: a * b,
}

print(operations['add'](3, 4))  # 7

# Function attributes
def my_func():
    """A documented function"""
    pass

my_func.version = "1.0"
my_func.author = "Alice"

print(my_func.__name__)    # my_func
print(my_func.__doc__)     # A documented function
print(my_func.version)     # 1.0
```

### Answer 10: Partial Functions
```python
from functools import partial

# Using functools.partial
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(5))    # 125

# Custom implementation
def my_partial(func, *partial_args, **partial_kwargs):
    """Custom partial function implementation"""
    def wrapper(*args, **kwargs):
        # Combine partial args with call-time args
        full_args = partial_args + args
        full_kwargs = {**partial_kwargs, **kwargs}
        return func(*full_args, **full_kwargs)
    
    return wrapper

# Test custom partial
def greet(greeting, name, punctuation="!"):
    return f"{greeting} {name}{punctuation}"

say_hello = my_partial(greet, "Hello")
print(say_hello("Alice"))  # Hello Alice!
print(say_hello("Bob", punctuation="?"))  # Hello Bob?
```

## Level: Hard (11-15)

### Answer 11: Advanced Decorators with Parameters
```python
import time
import functools
import asyncio

def retry(times=3, delay=1):
    """
    Decorator with parameters
    Retries function on exception
    """
    def decorator(func):
        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == times - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
        
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    if attempt == times - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
                    await asyncio.sleep(delay)
        
        # Return appropriate wrapper
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper
    
    return decorator

# Usage
@retry(times=3, delay=0.5)
def unstable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success!"

@retry(times=3, delay=0.5)
async def async_unstable():
    import random
    if random.random() < 0.7:
        raise ValueError("Async failure")
    return "Async success!"
```

### Answer 12: Generator Send and Throw
```python
def counter_generator():
    """Generator that can receive values"""
    count = 0
    while True:
        # Receive value from send()
        increment = yield count
        if increment is not None:
            count += increment
        else:
            count += 1

# Using send()
gen = counter_generator()
print(next(gen))        # 0 (must prime generator)
print(gen.send(5))      # 5 (send increment)
print(gen.send(3))      # 8 (5+3)
print(next(gen))        # 9 (8+1)

# Using throw()
def safe_divide():
    while True:
        try:
            x = yield
            yield x / 2
        except ZeroDivisionError:
            yield "Cannot divide by zero"

gen = safe_divide()
next(gen)
print(gen.send(10))  # 5.0

# Throw exception
next(gen)
print(gen.throw(ZeroDivisionError))  # "Cannot divide by zero"

# Using close()
def infinite_gen():
    try:
        count = 0
        while True:
            yield count
            count += 1
    finally:
        print("Generator closed, cleanup done")

gen = infinite_gen()
print(next(gen))  # 0
print(next(gen))  # 1
gen.close()  # "Generator closed, cleanup done"
# next(gen)  # StopIteration

# Practical example: Coroutine
def grep_coroutine(pattern):
    """Coroutine that filters lines"""
    print(f"Looking for {pattern}")
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("Coroutine closing")

g = grep_coroutine("python")
next(g)  # Prime
g.send("I love python")  # Prints: I love python
g.send("Java is ok")     # No output
g.send("python rocks")   # Prints: python rocks
g.close()
```

### Answer 13: Function Introspection
```python
import inspect
from typing import get_type_hints

def introspect_function(func):
    """
    Inspect function and return metadata
    """
    sig = inspect.signature(func)
    
    info = {
        'name': func.__name__,
        'module': func.__module__,
        'docstring': inspect.getdoc(func),
        'parameters': {},
        'return_annotation': sig.return_annotation,
        'is_coroutine': inspect.iscoroutinefunction(func),
        'source_file': inspect.getsourcefile(func),
    }
    
    # Get parameter details
    for param_name, param in sig.parameters.items():
        info['parameters'][param_name] = {
            'annotation': param.annotation,
            'default': param.default if param.default != inspect.Parameter.empty else None,
            'kind': str(param.kind)
        }
    
    # Get type hints
    try:
        hints = get_type_hints(func)
        info['type_hints'] = hints
    except:
        info['type_hints'] = {}
    
    return info

# Test function
def example(a: int, b: str = "default", *args, **kwargs) -> dict:
    """
    Example function for introspection
    
    Args:
        a: An integer
        b: A string with default
    
    Returns:
        A dictionary
    """
    return {'a': a, 'b': b}

# Introspect
info = introspect_function(example)
print(f"Name: {info['name']}")
print(f"Parameters: {info['parameters']}")
print(f"Return type: {info['return_annotation']}")
print(f"Docstring: {info['docstring']}")
```

### Answer 14: Recursive Memoization
```python
def memoize(func):
    """Memoization decorator for recursive functions"""
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    # Expose cache for inspection
    wrapper.cache = cache
    return wrapper

# Usage
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))  # Fast!
print(len(fibonacci.cache))  # 101 cached values

# Without memoization: O(2^n) - extremely slow
# With memoization: O(n) - fast

# Using lru_cache (built-in)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(100))
print(fib.cache_info())  # Cache statistics
```

### Answer 15: Context Manager as Function
```python
from contextlib import contextmanager
import time

@contextmanager
def timer(name="Operation"):
    """Context manager for timing"""
    start = time.time()
    print(f"{name} started...")
    
    try:
        yield  # Code block executes here
    finally:
        elapsed = time.time() - start
        print(f"{name} took {elapsed:.4f}s")

# Usage
with timer("Database query"):
    time.sleep(1)

# More complex example
@contextmanager
def temporary_value(obj, attr, value):
    """Temporarily change object attribute"""
    original = getattr(obj, attr)
    setattr(obj, attr, value)
    
    try:
        yield original
    finally:
        setattr(obj, attr, original)

class Config:
    debug = False

config = Config()
print(config.debug)  # False

with temporary_value(config, 'debug', True):
    print(config.debug)  # True

print(config.debug)  # False (restored)
```

## Bonus Challenge

### Answer 16: Function Composition
```python
from functools import reduce

def compose(*functions):
    """
    Compose functions right to left
    compose(f, g, h)(x) = f(g(h(x)))
    """
    def inner(arg):
        return reduce(lambda acc, func: func(acc), reversed(functions), arg)
    return inner

# Alternative implementation
def compose2(*functions):
    """Cleaner version"""
    return lambda x: reduce(lambda acc, f: f(acc), reversed(functions), x)

# Test
def add_one(x):
    return x + 1

def double(x):
    return x * 2

def square(x):
    return x ** 2

# compose(square, double, add_one)(3)
# = square(double(add_one(3)))
# = square(double(4))
# = square(8)
# = 64

f = compose(square, double, add_one)
print(f(3))  # 64

# Pipe (left to right)
def pipe(*functions):
    """Compose left to right"""
    return lambda x: reduce(lambda acc, f: f(acc), functions, x)

g = pipe(add_one, double, square)
print(g(3))  # (3+1)*2^2 = 16
```

### Answer 17: Currying
```python
import functools

def curry(func):
    """Convert function to curried form"""
    @functools.wraps(func)
    def curried(*args, **kwargs):
        # Check if we have all arguments
        sig = inspect.signature(func)
        try:
            sig.bind(*args, **kwargs)
            # All arguments provided
            return func(*args, **kwargs)
        except TypeError:
            # Not enough arguments, return partial
            return curry(functools.partial(func, *args, **kwargs))
    
    return curried

# Manual currying
def manual_curry(func):
    """Simpler manual curry"""
    def curried(*args):
        if len(args) >= func.__code__.co_argcount:
            return func(*args)
        return lambda *more_args: curried(*(args + more_args))
    return curried

# Test
@curry
def add_three(a, b, c):
    return a + b + c

# All these work:
print(add_three(1, 2, 3))      # 6
print(add_three(1)(2)(3))      # 6
print(add_three(1, 2)(3))      # 6
print(add_three(1)(2, 3))      # 6

# Practical use
add_5 = add_three(2)(3)
print(add_5(10))  # 15
```

### Answer 18: Method Dispatch
```python
from functools import singledispatch

# Single dispatch (one argument)
@singledispatch
def process(arg):
    """Default implementation"""
    print(f"Default: {arg}")

@process.register(int)
def _(arg):
    print(f"Integer: {arg * 2}")

@process.register(str)
def _(arg):
    print(f"String: {arg.upper()}")

@process.register(list)
def _(arg):
    print(f"List length: {len(arg)}")

# Usage
process(42)         # Integer: 84
process("hello")    # String: HELLO
process([1,2,3])    # List length: 3

# Custom multiple dispatch
class MultiDispatch:
    """Custom multiple dispatch"""
    def __init__(self):
        self.registry = {}
    
    def register(self, *types):
        def decorator(func):
            self.registry[types] = func
            return func
        return decorator
    
    def __call__(self, *args):
        types = tuple(type(arg) for arg in args)
        func = self.registry.get(types)
        
        if func is None:
            raise TypeError(f"No implementation for {types}")
        
        return func(*args)

# Usage
add = MultiDispatch()

@add.register(int, int)
def _(a, b):
    return a + b

@add.register(str, str)
def _(a, b):
    return a + " " + b

@add.register(list, list)
def _(a, b):
    return a + b

print(add(1, 2))           # 3
print(add("hello", "world"))  # hello world
print(add([1], [2]))       # [1, 2]
```
