# Data Structures - Interview Questions

## Level: Normal (1-5)

### Question 1: List, Tuple, Set, and Dict - Complete Comparison
Explain the key differences between Python's four main built-in data structures: List, Tuple, Set, and Dict. Compare them in terms of:
- Mutability
- Ordering
- Duplicates
- Indexing/Access methods
- Performance characteristics
- Use cases for each

Provide practical examples showing when to use each data structure.

### Question 2: List Slicing
What will be the output?
```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[2:8:2])
print(lst[::-1])
print(lst[-3:])
```

### Question 3: Dictionary Key Requirements
Which of these can be used as dictionary keys and why?
```python
key1 = [1, 2, 3]
key2 = (1, 2, 3)
key3 = {1, 2, 3}
key4 = "hello"
key5 = 42
```

### Question 4: Set Operations
Given two sets:
```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
```
Find: union, intersection, difference, and symmetric difference.

### Question 5: List Comprehension
Convert this loop to a list comprehension:
```python
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i ** 2)
```

## Level: Medium (6-10)

### Question 6: Shallow vs Deep Copy
Explain the output:
```python
import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow = original.copy()
deep = copy.deepcopy(original)

original[0][0] = 999

print(original)
print(shallow)
print(deep)
```

### Question 7: Dictionary Methods
What's the difference between:
```python
d = {'a': 1, 'b': 2}

# Method 1
value = d['c']

# Method 2
value = d.get('c')

# Method 3
value = d.get('c', 0)

# Method 4
value = d.setdefault('c', 0)
```

### Question 8: List Performance
Compare the time complexity of these operations:
```python
# Operation 1: Append
lst.append(item)

# Operation 2: Insert at beginning
lst.insert(0, item)

# Operation 3: Check membership
item in lst

# Operation 4: Access by index
lst[100]
```

### Question 9: Dictionary Merge
Given two dictionaries, what's the difference between these merge operations?
```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

# Method 1
result1 = {**d1, **d2}

# Method 2
result2 = d1 | d2  # Python 3.9+

# Method 3
result3 = d1.copy()
result3.update(d2)
```

### Question 10: Nested Data Structures
Write a function to flatten a nested list of arbitrary depth:
```python
nested = [1, [2, 3, [4, 5]], 6, [7, [8, [9]]]]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Level: Hard (11-15)

### Question 11: Custom Hash for Dictionary Keys
Create a custom class that can be used as a dictionary key. Implement `__hash__` and `__eq__` properly.

### Question 12: LRU Cache Implementation
Implement an LRU (Least Recently Used) cache with O(1) get and put operations using:
- Dictionary for fast lookup
- Doubly linked list for maintaining order

### Question 13: Deque vs List
When would you use `collections.deque` instead of a list? Provide a scenario where deque significantly outperforms list.

### Question 14: Counter and Defaultdict
Compare these approaches for counting word frequency:
```python
# Method 1: Regular dict
# Method 2: dict.get()
# Method 3: defaultdict
# Method 4: Counter
```
Implement each and discuss trade-offs.

### Question 15: Memory-Efficient Data Structures
You need to store 1 million boolean flags. Compare:
```python
# Method 1: List of booleans
# Method 2: Set of indices (sparse)
# Method 3: Bitarray/bytes
```
Which is most memory-efficient and when?

## Bonus Challenge

### Question 16: Implement a Trie
Implement a Trie (prefix tree) data structure for efficient string searching with:
- insert(word)
- search(word)
- startsWith(prefix)
- delete(word)

### Question 17: Design a Time-Based Key-Value Store
Design a data structure that:
- Stores values with timestamps
- get(key, timestamp) returns value at that time
- set(key, value, timestamp) stores value
- Uses efficient data structures (hint: dict + sorted list)

### Question 18: Ring Buffer
Implement a circular/ring buffer with fixed size that:
- Overwrites oldest data when full
- Supports O(1) append and read operations
- Useful for streaming data or logging
