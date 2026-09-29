# Error Handling - Interview Answers

## Level: Normal (1-5)

### Answer 1: Try-Except Basics
```python
try:
    # Code that might raise exception
    result = 10 / 0
except ZeroDivisionError:
    # Handles specific exception
    print("Cannot divide by zero")
except Exception as e:
    # Handles other exceptions
    print(f"Error: {e}")
else:
    # Executes if NO exception
    print("Success!")
finally:
    # ALWAYS executes
    print("Cleanup")
```

### Answer 2: Exception Hierarchy
```python
# Don't do this (catches everything, including KeyboardInterrupt)
try:
    code()
except:  # BAD - catches BaseException
    pass

# Better
try:
    code()
except Exception as e:  # GOOD - specific
    handle(e)

# Hierarchy:
# BaseException
#  ├── SystemExit
#  ├── KeyboardInterrupt
#  └── Exception
#       ├── ValueError
#       ├── TypeError
#       └── ...
```

### Answer 3: Multiple Except Blocks
```python
# Multiple exceptions
try:
    value = int(input())
    result = 10 / value
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, KeyError) as e:
    print(f"Multiple types: {e}")
```

### Answer 5: Custom Exceptions
```python
class ValidationError(Exception):
    """Custom validation exception"""
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

try:
    raise ValidationError("email", "Invalid format")
except ValidationError as e:
    print(f"Field '{e.field}' error: {e.message}")
```

## Level: Medium (6-10)

### Answer 6: Exception Chaining
```python
# Implicit chaining
try:
    value = int("invalid")
except ValueError:
    raise RuntimeError("Processing failed")  # Shows both exceptions

# Explicit chaining
try:
    value = int("invalid")
except ValueError as e:
    raise RuntimeError("Processing failed") from e

# Suppress chaining
try:
    value = int("invalid")
except ValueError:
    raise RuntimeError("Processing failed") from None
```

### Answer 8: EAFP vs LBYL
```python
# LBYL (Look Before You Leap)
if key in dictionary:
    value = dictionary[key]
else:
    value = default

# EAFP (Easier to Ask Forgiveness than Permission) - Pythonic
try:
    value = dictionary[key]
except KeyError:
    value = default

# EAFP is preferred in Python
```

### Answer 9: Logging vs Printing Exceptions
```python
import logging
import traceback

logging.basicConfig(level=logging.ERROR)

try:
    risky_operation()
except Exception as e:
    # BAD - loses stack trace
    print(f"Error: {e}")
    
    # GOOD - full stack trace
    logging.exception("Operation failed")
    
    # Or manually
    logging.error("Error occurred", exc_info=True)
    
    # Get traceback as string
    tb_str = traceback.format_exc()
```

## Level: Hard (11-15)

### Answer 13: Retry Decorator
```python
import time
import functools

def retry(max_attempts=3, delay=1, backoff=2, exceptions=(Exception,)):
    """Retry decorator with exponential backoff"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
                    print(f"Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry(max_attempts=3, delay=1, backoff=2, exceptions=(ValueError,))
def unstable_api_call():
    import random
    if random.random() < 0.7:
        raise ValueError("API error")
    return "Success"
```

### Answer 14: Circuit Breaker Pattern
```python
import time
from enum import Enum

class CircuitState(Enum):
    CLOSED = "closed"  # Normal operation
    OPEN = "open"      # Failing, reject requests
    HALF_OPEN = "half_open"  # Testing if recovered

class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED
    
    def call(self, func, *args, **kwargs):
        if self.state == CircuitState.OPEN:
            if time.time() - self.last_failure_time > self.timeout:
                self.state = CircuitState.HALF_OPEN
            else:
                raise Exception("Circuit breaker is OPEN")
        
        try:
            result = func(*args, **kwargs)
            if self.state == CircuitState.HALF_OPEN:
                self.state = CircuitState.CLOSED
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()
            
            if self.failure_count >= self.failure_threshold:
                self.state = CircuitState.OPEN
            
            raise
```
