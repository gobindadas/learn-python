# Advanced Topics - Interview Answers

## Level: Normal (1-5)

### Answer 1: Comprehensions
```python
# List comprehension
squares = [x**2 for x in range(10)]

# Dict comprehension
square_dict = {x: x**2 for x in range(10)}

# Set comprehension
unique_squares = {x**2 for x in range(-5, 5)}

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
```

### Answer 3: Map, Filter, Reduce
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map()
squared = list(map(lambda x: x**2, numbers))
# vs comprehension
squared = [x**2 for x in numbers]

# filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
# vs comprehension
evens = [x for x in numbers if x % 2 == 0]

# reduce()
total = reduce(lambda x, y: x + y, numbers)
# vs sum()
total = sum(numbers)
```

## Level: Medium (6-10)

### Answer 6: Iterators and Iterables
```python
class CountDown:
    """Custom iterator"""
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

# Usage
for num in CountDown(5):
    print(num)  # 5, 4, 3, 2, 1
```

### Answer 9: Type Hints
```python
from typing import List, Dict, Optional, Union, Callable

def process_data(
    items: List[int],
    mapping: Dict[str, int],
    callback: Optional[Callable[[int], int]] = None
) -> Union[List[int], None]:
    if not items:
        return None
    
    result = [callback(x) if callback else x for x in items]
    return result
```

## Level: Hard (11-15)

### Answer 11: Async/Await
```python
import asyncio

async def fetch_data(n):
    await asyncio.sleep(1)
    return n * 2

async def main():
    # Concurrent execution
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    print(results)

asyncio.run(main())
```
