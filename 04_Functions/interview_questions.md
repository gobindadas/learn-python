# Functions - Interview Questions

## Level: Normal (1-5)

### Question 1: Function Arguments
What's the difference between:
```python
def func(a, b, c=10):
    pass

func(1, 2)
func(1, 2, 3)
func(a=1, b=2, c=3)
```

### Question 2: Return Values
What does this function return?
```python
def mystery():
    x = 10
    y = 20
    # No return statement

result = mystery()
print(result)
```

### Question 3: Variable Scope
What will be printed?
```python
x = "global"

def outer():
    x = "outer"
    
    def inner():
        x = "inner"
        print(x)
    
    inner()
    print(x)

outer()
print(x)
```

### Question 4: Mutable Default Arguments
What's wrong with this code?
```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))
print(add_item(2))
print(add_item(3))
```

### Question 5: *args and **kwargs
Explain the difference and provide examples of when to use each.

## Level: Medium (6-10)

### Question 6: Closures
Explain closures and fix this code to work correctly:
```python
functions = []
for i in range(3):
    functions.append(lambda: i)

for f in functions:
    print(f())  # What gets printed?
```

### Question 7: Decorators
Implement a decorator that:
- Measures function execution time
- Prints function name and arguments
- Can work with any function

### Question 8: Generator vs Regular Function
Compare these two implementations:
```python
def regular_range(n):
    result = []
    for i in range(n):
        result.append(i)
    return result

def generator_range(n):
    for i in range(n):
        yield i
```
When would you use each?

### Question 9: Function as First-Class Objects
Demonstrate that functions are first-class objects by:
- Assigning function to variable
- Passing function as argument
- Returning function from function
- Storing function in data structure

### Question 10: Partial Functions
What are partial functions? Implement a custom `partial` function without using `functools.partial`.

## Level: Hard (11-15)

### Question 11: Advanced Decorators
Implement a decorator with parameters that:
- Can retry a function n times on failure
- Has configurable delay between retries
- Works with both sync and async functions

### Question 12: Generator Send and Throw
Explain generator methods:
- `.send()`
- `.throw()`
- `.close()`
Provide practical examples.

### Question 13: Function Introspection
Write a function that inspects another function and returns:
- Function name
- Number of arguments
- Argument names and defaults
- Return type annotation
- Docstring

### Question 14: Recursive Memoization
Implement a memoization decorator that works with recursive functions (like Fibonacci).

### Question 15: Context Manager as Function
Implement a function that acts as a context manager without using classes. Use `@contextmanager` decorator.

## Bonus Challenge

### Question 16: Function Composition
Implement a `compose` function that takes multiple functions and returns their composition:
```python
def add_one(x): return x + 1
def double(x): return x * 2
def square(x): return x ** 2

f = compose(square, double, add_one)
print(f(3))  # square(double(add_one(3))) = square(double(4)) = square(8) = 64
```

### Question 17: Currying
Implement a decorator that curries a function (converts f(a,b,c) to f(a)(b)(c)).

### Question 18: Method Dispatch
Implement a function dispatcher that:
- Calls different implementations based on argument types
- Supports single and multiple dispatch
- Similar to `@singledispatch` from functools
