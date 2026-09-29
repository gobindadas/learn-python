# Python Basics - Interview Answers

## Level: Normal (1-5)

### Answer 1: Variable Assignment and Memory
**Output:** `10`

**Explanation:**
- In Python, integers are immutable objects
- When `b = a`, both variables point to the same integer object (10)
- When `a = 20`, a new integer object is created and `a` points to it
- `b` still points to the original object (10)
- This is different from languages where `b` would be a reference to `a`

```python
a = 10
b = a  # b points to the same object as a (10)
a = 20  # a now points to a new object (20)
print(b)  # b still points to 10
```

### Answer 2: Type Conversion Edge Cases
**Output:**
```python
3          # int(3.9) - truncates, doesn't round
100        # int("100") - valid string to int
ValueError # int("10.5") - can't convert float string directly
True       # bool("False") - any non-empty string is True
False      # bool("") - empty string is False
```

**Key Points:**
- `int()` truncates floats, doesn't round
- `int()` can't parse float strings directly - use `int(float("10.5"))`
- `bool()` returns False only for: `False`, `None`, `0`, `""`, `[]`, `{}`, `()`

### Answer 3: String Immutability
**Error:** `TypeError: 'str' object does not support item assignment`

**Explanation:**
Strings in Python are immutable - they cannot be changed after creation.

**Correct approaches:**
```python
# Method 1: String concatenation
s = "H" + s[1:]

# Method 2: String methods
s = s.capitalize()

# Method 3: String replace
s = s.replace(s[0], s[0].upper(), 1)

# Method 4: List conversion
s = ''.join(['H'] + list(s[1:]))
```

### Answer 4: Operator Precedence
**Output:**
```python
20    # 10 + (5 * 2) - multiplication before addition
30    # (10 + 5) * 2 - parentheses override precedence
512   # 2 ** (3 ** 2) = 2 ** 9 - exponentiation is right-associative
```

**Precedence order (high to low):**
1. `()` - Parentheses
2. `**` - Exponentiation (right-associative)
3. `*, /, //, %` - Multiplication, division, floor division, modulo
4. `+, -` - Addition, subtraction

### Answer 5: String Formatting Methods
**Three main methods:**

```python
name = "Alice"
age = 30

# 1. Old-style % formatting (legacy)
result = "Name: %s, Age: %d" % (name, age)

# 2. str.format() method (Python 2.6+)
result = "Name: {}, Age: {}".format(name, age)
result = "Name: {n}, Age: {a}".format(n=name, a=age)

# 3. f-strings (Python 3.6+) - PREFERRED
result = f"Name: {name}, Age: {age}"
result = f"Name: {name}, Age: {age}, Next year: {age + 1}"
```

## Level: Medium (6-10)

### Answer 6: Multiple Assignment Gotcha
**Output:**
```python
[1, 2, 3, 4]
[1, 2, 3, 4]
```

**Explanation:**
- All three variables (`x`, `y`, `z`) point to the **same list object**
- When you modify the list through `x`, you're modifying the shared object
- Both `y` and `z` see the change because they reference the same object

**How to avoid:**
```python
# Create separate copies
x = [1, 2, 3]
y = [1, 2, 3]  # New list
z = x.copy()   # Creates a shallow copy

# Or using list()
y = list(x)

# Or using slicing
z = x[:]
```

### Answer 7: Integer Division and Modulo
```python
def seconds_to_hms(seconds):
    """
    Convert seconds to HH:MM:SS format
    
    Args:
        seconds: Total number of seconds (int)
    
    Returns:
        String in format HH:MM:SS
    """
    hours = seconds // 3600
    remaining = seconds % 3600
    minutes = remaining // 60
    secs = remaining % 60
    
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

# Test cases
print(seconds_to_hms(3665))   # 01:01:05
print(seconds_to_hms(7200))   # 02:00:00
print(seconds_to_hms(90))     # 00:01:30
```

### Answer 8: String Methods Chain
```python
s = "  Hello World  "

# One-liner solution
result = s.strip().lower().replace("world", "python")

# Output: "hello python"
```

**Method breakdown:**
- `strip()` - removes leading/trailing whitespace
- `lower()` - converts to lowercase
- `replace(old, new)` - replaces substring

### Answer 9: Input Validation
```python
def get_validated_input(prompt, min_val=None, max_val=None):
    """
    Get and validate positive integer input within range
    
    Args:
        prompt: Message to display
        min_val: Minimum acceptable value (inclusive)
        max_val: Maximum acceptable value (inclusive)
    
    Returns:
        Valid integer input
    """
    while True:
        try:
            user_input = input(prompt)
            
            # Convert to integer
            value = int(user_input)
            
            # Check if positive
            if value < 0:
                print("Error: Number must be positive")
                continue
            
            # Check range if specified
            if min_val is not None and value < min_val:
                print(f"Error: Number must be at least {min_val}")
                continue
            
            if max_val is not None and value > max_val:
                print(f"Error: Number must be at most {max_val}")
                continue
            
            return value
            
        except ValueError:
            print("Error: Please enter a valid integer")
        except KeyboardInterrupt:
            print("\nInput cancelled by user")
            return None
        except EOFError:
            print("\nEnd of input")
            return None

# Usage
age = get_validated_input("Enter your age (0-150): ", 0, 150)
```

### Answer 10: Memory Efficiency (Integer Caching)
**Output (typically):**
```python
True   # a is b for 256
False  # c is d for 257 (may vary)
```

**Explanation:**
- Python caches small integers (typically -5 to 256) for memory efficiency
- When you create an integer in this range, Python reuses the same object
- For integers outside this range, new objects are created
- This is an implementation detail (CPython specific)

```python
a = 256
b = 256
print(a is b)  # True - same cached object
print(id(a) == id(b))  # True - same memory address

c = 257
d = 257
print(c is d)  # May be False - different objects
print(c == d)  # True - same value

# Force same object
e = f = 257
print(e is f)  # True - assigned simultaneously
```

**Best Practice:** Always use `==` for value comparison, use `is` only for identity checks (None, True, False).

## Level: Hard (11-15)

### Answer 11: Dynamic Type System
**Issues with the design:**
1. Violates Open/Closed Principle - must modify function for new types
2. Doesn't handle type variations (list vs tuple)
3. No polymorphism - defeats duck typing
4. Type checking is anti-Pythonic

**Improved approaches:**

```python
# Approach 1: Duck typing with protocols
def process(data):
    """Process data using duck typing"""
    try:
        # Try numeric operation
        return data * 2
    except TypeError:
        # Try string operation
        try:
            return data.upper()
        except AttributeError:
            # Try iterable operation
            try:
                return len(data)
            except TypeError:
                return None

# Approach 2: Using __mul__ and other magic methods
def process(data):
    """Use magic methods for polymorphism"""
    if hasattr(data, '__mul__'):
        return data * 2
    elif hasattr(data, 'upper'):
        return data.upper()
    elif hasattr(data, '__len__'):
        return len(data)
    return None

# Approach 3: Protocol classes (Python 3.8+)
from typing import Protocol

class Processable(Protocol):
    def process(self) -> any:
        ...

class MyInt:
    def __init__(self, value):
        self.value = value
    
    def process(self):
        return self.value * 2

# Approach 4: Single dispatch (Python 3.4+)
from functools import singledispatch

@singledispatch
def process(data):
    return None

@process.register(int)
def _(data):
    return data * 2

@process.register(str)
def _(data):
    return data.upper()

@process.register(list)
def _(data):
    return len(data)
```

### Answer 12: String Interning
**Output:**
```python
True   # a is b
False  # a is c (typically)
True   # a == c
```

**Explanation:**
- **String Interning**: Python automatically interns (caches) some strings to save memory
- String literals that look like identifiers are automatically interned
- Dynamically created strings (like join) may not be interned
- `is` checks object identity (same object in memory)
- `==` checks value equality

```python
# Interned strings
a = "hello"
b = "hello"
print(a is b)  # True - same interned object

# Dynamically created - not interned
c = "".join(['h', 'e', 'l', 'l', 'o'])
print(a is c)  # False - different objects
print(a == c)  # True - same value

# Force interning
import sys
c = sys.intern(c)
print(a is c)  # True - now interned

# Strings with special characters may not be interned
x = "hello world"  # Has space
y = "hello world"
print(x is y)  # May be False
```

### Answer 13: Numeric Edge Cases
```python
def safe_numeric_operation(a, b, operation):
    """
    Safely perform numeric operations with edge case handling
    
    Args:
        a, b: Numeric values
        operation: 'add', 'subtract', 'multiply', 'divide'
    
    Returns:
        Result or None if error
    """
    from decimal import Decimal, InvalidOperation
    
    try:
        # Handle division by zero
        if operation == 'divide':
            if b == 0:
                raise ValueError("Division by zero")
            return a / b
        
        # Handle floating point precision
        if isinstance(a, float) or isinstance(b, float):
            # Use Decimal for precise calculations
            a_decimal = Decimal(str(a))
            b_decimal = Decimal(str(b))
            
            if operation == 'add':
                return float(a_decimal + b_decimal)
            elif operation == 'subtract':
                return float(a_decimal - b_decimal)
            elif operation == 'multiply':
                return float(a_decimal * b_decimal)
        
        # Regular integer operations
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiply':
            return a * b
            
    except (TypeError, ValueError, InvalidOperation) as e:
        print(f"Error: {e}")
        return None

# Python handles integer overflow automatically (arbitrary precision)
big_num = 10 ** 100
print(big_num * big_num)  # Works fine!

# Floating point precision issues
print(0.1 + 0.2)  # 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # False

# Better approach
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))  # 0.3
```

### Answer 14: Advanced String Operations
```python
def is_valid_identifier(s):
    """
    Check if string is a valid Python identifier
    
    Rules:
    - Must start with letter or underscore
    - Can contain letters, digits, underscores
    - Cannot be a Python keyword
    - Cannot be empty
    
    Args:
        s: String to check
    
    Returns:
        Boolean
    """
    import keyword
    
    # Check empty string
    if not s or len(s) == 0:
        return False
    
    # Check first character (must be letter or underscore)
    first_char = s[0]
    if not (first_char.isalpha() or first_char == '_'):
        return False
    
    # Check remaining characters
    for char in s[1:]:
        if not (char.isalnum() or char == '_'):
            return False
    
    # Check if it's a keyword
    if keyword.iskeyword(s):
        return False
    
    return True

# Test cases
print(is_valid_identifier("variable"))      # True
print(is_valid_identifier("_private"))      # True
print(is_valid_identifier("var123"))        # True
print(is_valid_identifier("123var"))        # False (starts with digit)
print(is_valid_identifier("my-var"))        # False (has hyphen)
print(is_valid_identifier("class"))         # False (keyword)
print(is_valid_identifier(""))              # False (empty)
```

### Answer 15: Type Coercion and Comparison
**Output:**
```python
True   # 1 == True (value equality after coercion)
False  # 1 is True (different objects)
True   # 0 == False (value equality after coercion)
False  # [] == False (list is not equal to bool)
False  # bool([]) (empty list is falsy)
```

**Detailed Explanation:**

```python
# == checks VALUE equality (uses __eq__ method)
# is checks IDENTITY (same object in memory)

# 1 == True
print(1 == True)    # True - bool is subclass of int, True has value 1
print(isinstance(True, int))  # True
print(True + True)  # 2

# 1 is True
print(1 is True)    # False - different objects
print(id(1), id(True))  # Different memory addresses

# 0 == False
print(0 == False)   # True - False has value 0
print(False + 1)    # 1

# [] == False
print([] == False)  # False - no coercion happens with ==
print([] is False)  # False

# bool([])
print(bool([]))     # False - empty containers are falsy

# Implications for type checking
x = 1
if x == True:      # BAD - may have unintended matches
    print("This runs!")

if x is True:      # GOOD for boolean check
    print("This doesn't run")

if x:              # BEST - Pythonic truthy check
    print("This runs!")

# Falsy values in Python
falsy_values = [False, None, 0, 0.0, '', [], {}, (), set()]
for val in falsy_values:
    print(f"{repr(val):10} -> {bool(val)}")
```

## Bonus Challenge

### Answer 16: Build a Type Validator
```python
from typing import get_origin, get_args, Union
import types

def validate_type(value, expected_type, raise_error=True):
    """
    Validate if value matches expected type
    
    Args:
        value: Value to check
        expected_type: Expected type or type hint
        raise_error: Whether to raise TypeError or return bool
    
    Returns:
        Boolean if raise_error=False, else raises TypeError
    """
    # Handle None/Optional
    if value is None:
        origin = get_origin(expected_type)
        if origin is Union:
            args = get_args(expected_type)
            if type(None) in args:
                return True
        if raise_error:
            raise TypeError(f"Expected {expected_type}, got None")
        return False
    
    # Get origin for generic types (List, Dict, etc.)
    origin = get_origin(expected_type)
    
    # Handle Union types (e.g., Union[int, str])
    if origin is Union:
        args = get_args(expected_type)
        for arg in args:
            if arg is type(None) and value is None:
                return True
            try:
                if validate_type(value, arg, raise_error=False):
                    return True
            except TypeError:
                continue
        if raise_error:
            raise TypeError(
                f"Expected one of {args}, got {type(value).__name__}: {value}"
            )
        return False
    
    # Handle generic types (List, Dict, etc.)
    if origin is not None:
        # Check container type
        if not isinstance(value, origin):
            if raise_error:
                raise TypeError(
                    f"Expected {origin.__name__}, got {type(value).__name__}"
                )
            return False
        
        # Check nested types
        args = get_args(expected_type)
        if args:
            if origin in (list, set, tuple):
                for item in value:
                    if not validate_type(item, args[0], raise_error):
                        return False
            elif origin is dict:
                key_type, val_type = args
                for k, v in value.items():
                    if not validate_type(k, key_type, raise_error):
                        return False
                    if not validate_type(v, val_type, raise_error):
                        return False
        return True
    
    # Simple type check
    if not isinstance(value, expected_type):
        if raise_error:
            raise TypeError(
                f"Expected {expected_type.__name__}, "
                f"got {type(value).__name__}: {value}"
            )
        return False
    
    return True

# Test cases
from typing import List, Dict, Optional

# Simple types
print(validate_type(42, int, raise_error=False))          # True
print(validate_type("hello", int, raise_error=False))     # False

# Union types
print(validate_type(42, Union[int, str], raise_error=False))      # True
print(validate_type("hi", Union[int, str], raise_error=False))    # True

# Optional (Union with None)
print(validate_type(None, Optional[int], raise_error=False))      # True
print(validate_type(42, Optional[int], raise_error=False))        # True

# Generic types
print(validate_type([1, 2, 3], List[int], raise_error=False))     # True
print(validate_type([1, "2"], List[int], raise_error=False))      # False

# Nested types
data = {"name": "Alice", "age": "30"}
print(validate_type(data, Dict[str, str], raise_error=False))     # True
print(validate_type(data, Dict[str, int], raise_error=False))     # False

# With error raising
try:
    validate_type("hello", int, raise_error=True)
except TypeError as e:
    print(f"Caught error: {e}")
```

This type validator handles:
- Simple types (int, str, etc.)
- Union types (int | str)
- Optional types (None allowed)
- Generic types (List[int], Dict[str, int])
- Nested validation
- Meaningful error messages
