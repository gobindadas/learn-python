# Error Handling - Interview Questions

## Level: Normal (1-5)

### Question 1: Try-Except Basics
Explain try, except, else, and finally blocks. When does each execute?

### Question 2: Exception Hierarchy
What is the Python exception hierarchy? Why shouldn't you catch bare Exception?

### Question 3: Multiple Except Blocks
How do you handle multiple exception types? Show examples.

### Question 4: Raising Exceptions
When and how should you raise exceptions?

### Question 5: Custom Exceptions
How do you create custom exception classes?

## Level: Medium (6-10)

### Question 6: Exception Chaining
What is exception chaining? Use `raise ... from ...`.

### Question 7: Context Managers and Exceptions
How do context managers handle exceptions in `__exit__`?

### Question 8: EAFP vs LBYL
Explain "Easier to Ask Forgiveness than Permission" vs "Look Before You Leap".

### Question 9: Logging vs Printing Exceptions
What's the proper way to log exceptions?

### Question 10: Suppressing Exceptions
When is it appropriate to suppress exceptions? Use `contextlib.suppress`.

## Level: Hard (11-15)

### Question 11: Exception Groups (Python 3.11+)
What are exception groups? When would you use ExceptionGroup?

### Question 12: Custom Exception Handler
Implement a global exception handler using sys.excepthook.

### Question 13: Retry Decorator
Implement a decorator that retries on specific exceptions with exponential backoff.

### Question 14: Error Recovery Patterns
Implement circuit breaker pattern for handling failures.

### Question 15: Graceful Degradation
Design a system that degrades gracefully when dependencies fail.
