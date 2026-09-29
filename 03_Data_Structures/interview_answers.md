# Data Structures - Interview Answers

## Level: Normal (1-5)

### Answer 1: List vs Tuple

| Feature | List | Tuple |
|---------|------|-------|
| Mutability | Mutable (can modify) | Immutable (cannot modify) |
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Performance | Slower | Faster (less memory) |
| Use case | Dynamic data | Fixed data, dict keys |
| Methods | append, remove, etc. | Limited (count, index) |

**When to use:**
```python
# List: Dynamic, mutable data
shopping_cart = ['apple', 'banana']
shopping_cart.append('orange')  # OK

# Tuple: Fixed data, constants, dict keys
coordinates = (10.5, 20.3)
coordinates[0] = 15  # TypeError

# Tuple as dict key
locations = {
    (0, 0): "origin",
    (10, 20): "point A"
}

# Tuple for multiple return values
def get_user():
    return ("Alice", 25, "alice@email.com")

name, age, email = get_user()
```

### Answer 2: List Slicing
```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lst[2:8:2])   # [2, 4, 6] - start at 2, end before 8, step 2
print(lst[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - reverse
print(lst[-3:])     # [7, 8, 9] - last 3 elements
```

**Slicing syntax:** `lst[start:stop:step]`
```python
# Common patterns
lst[:]      # Copy entire list
lst[::2]    # Every other element
lst[1::2]   # Every other, starting at index 1
lst[-1]     # Last element
lst[-2:]    # Last 2 elements
lst[:-1]    # All except last
lst[::-1]   # Reverse
```

### Answer 3: Dictionary Key Requirements
**Keys must be hashable (immutable):**

```python
key1 = [1, 2, 3]      # ❌ INVALID - lists are mutable
key2 = (1, 2, 3)      # ✅ VALID - tuples are immutable
key3 = {1, 2, 3}      # ❌ INVALID - sets are mutable
key4 = "hello"        # ✅ VALID - strings are immutable
key5 = 42             # ✅ VALID - ints are immutable

# Valid keys
d = {
    42: "number",
    "hello": "string",
    (1, 2): "tuple",
    frozenset([1, 2]): "frozenset",
}

# Invalid - will raise TypeError
try:
    d[[1, 2]] = "list"  # TypeError: unhashable type: 'list'
except TypeError as e:
    print(e)
```

**Requirements:**
1. Must be hashable (`__hash__` method)
2. Must be immutable
3. Must implement `__eq__` for equality

### Answer 4: Set Operations
```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union: all elements from both sets
union = a | b
# or: a.union(b)
print(union)  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection: common elements
intersection = a & b
# or: a.intersection(b)
print(intersection)  # {4, 5}

# Difference: in a but not in b
difference = a - b
# or: a.difference(b)
print(difference)  # {1, 2, 3}

# Symmetric difference: in either but not both
sym_diff = a ^ b
# or: a.symmetric_difference(b)
print(sym_diff)  # {1, 2, 3, 6, 7, 8}

# Subset/Superset
print(a.issubset(b))    # False
print(a.issuperset(b))  # False
print({1, 2}.issubset(a))  # True
```

### Answer 5: List Comprehension
```python
# Original loop
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i ** 2)

# List comprehension
result = [i ** 2 for i in range(10) if i % 2 == 0]

# Output: [0, 4, 16, 36, 64]
```

**More examples:**
```python
# Nested loop
result = [(x, y) for x in range(3) for y in range(3)]

# With multiple conditions
result = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]

# With if-else (ternary)
result = [x if x % 2 == 0 else -x for x in range(10)]
```

## Level: Medium (6-10)

### Answer 6: Shallow vs Deep Copy
**Output:**
```python
original: [[999, 2, 3], [4, 5, 6]]
shallow:  [[999, 2, 3], [4, 5, 6]]  # Inner list is shared!
deep:     [[1, 2, 3], [4, 5, 6]]    # Completely independent
```

**Explanation:**
```python
import copy

original = [[1, 2, 3], [4, 5, 6]]

# Shallow copy: copies outer container, not nested objects
shallow = original.copy()  # or list(original) or original[:]
# Both point to same inner lists
print(id(original[0]) == id(shallow[0]))  # True

# Deep copy: recursively copies everything
deep = copy.deepcopy(original)
# Inner lists are different objects
print(id(original[0]) == id(deep[0]))  # False

# Modification test
original[0][0] = 999
print(f"Original: {original}")  # [[999, 2, 3], [4, 5, 6]]
print(f"Shallow: {shallow}")    # [[999, 2, 3], [4, 5, 6]] - affected!
print(f"Deep: {deep}")          # [[1, 2, 3], [4, 5, 6]] - unaffected
```

**Visual representation:**
```
Shallow:
original ─┬─> [ref1, ref2]
shallow ──┤    ↓     ↓
          └──> [1,2,3] [4,5,6]  (shared!)

Deep:
original ──> [ref1, ref2]
              ↓     ↓
            [1,2,3] [4,5,6]

deep ──────> [ref3, ref4]
              ↓     ↓
            [1,2,3] [4,5,6]  (independent!)
```

### Answer 7: Dictionary Methods
```python
d = {'a': 1, 'b': 2}

# Method 1: Direct access - raises KeyError if missing
try:
    value = d['c']  # KeyError: 'c'
except KeyError:
    value = None

# Method 2: get() - returns None if missing
value = d.get('c')  # None

# Method 3: get() with default - returns default if missing
value = d.get('c', 0)  # 0 (doesn't modify dict)

# Method 4: setdefault() - returns value, ADDS if missing
value = d.setdefault('c', 0)  # 0 (adds 'c': 0 to dict!)
print(d)  # {'a': 1, 'b': 2, 'c': 0}
```

**Comparison:**

| Method | Missing Key | Modifies Dict | Use Case |
|--------|-------------|---------------|----------|
| `d['k']` | Raises KeyError | No | When key must exist |
| `d.get('k')` | Returns None | No | Safe access |
| `d.get('k', default)` | Returns default | No | With default value |
| `d.setdefault('k', default)` | Returns & adds default | Yes | Initialize if missing |

**Use cases:**
```python
# Counting with setdefault
counts = {}
for word in ["a", "b", "a", "c", "b"]:
    counts.setdefault(word, 0)
    counts[word] += 1

# Better: use get
counts = {}
for word in ["a", "b", "a", "c", "b"]:
    counts[word] = counts.get(word, 0) + 1

# Best: use defaultdict or Counter
from collections import defaultdict, Counter
counts = defaultdict(int)
for word in ["a", "b", "a", "c", "b"]:
    counts[word] += 1
```

### Answer 8: List Performance

| Operation | Time Complexity | Explanation |
|-----------|----------------|-------------|
| `lst.append(item)` | O(1) amortized | Adds to end |
| `lst.insert(0, item)` | O(n) | Shifts all elements |
| `item in lst` | O(n) | Linear search |
| `lst[100]` | O(1) | Direct indexing |
| `lst.pop()` | O(1) | Remove from end |
| `lst.pop(0)` | O(n) | Shifts all elements |
| `lst.sort()` | O(n log n) | Timsort algorithm |

**Benchmarks:**
```python
import timeit

# Append: O(1) - very fast
timeit.timeit('lst.append(1)', setup='lst = []', number=100000)

# Insert at beginning: O(n) - slow
timeit.timeit('lst.insert(0, 1)', setup='lst = list(range(1000))', number=1000)

# Membership test: O(n) - slow for lists, O(1) for sets
timeit.timeit('500 in lst', setup='lst = list(range(1000))', number=10000)
timeit.timeit('500 in s', setup='s = set(range(1000))', number=10000)
```

**Better alternatives:**
```python
# Instead of: lst.insert(0, item) repeatedly
# Use: collections.deque
from collections import deque
dq = deque()
dq.appendleft(item)  # O(1)

# Instead of: item in lst
# Use: set for membership testing
s = set(lst)
if item in s:  # O(1)
    pass
```

### Answer 9: Dictionary Merge
```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

# Method 1: Unpacking (**) - creates new dict
result1 = {**d1, **d2}  # {'a': 1, 'b': 3, 'c': 4}
# d1 and d2 unchanged

# Method 2: Union operator (|) - Python 3.9+
result2 = d1 | d2  # {'a': 1, 'b': 3, 'c': 4}
# d1 and d2 unchanged
# Also: d1 |= d2 for in-place update

# Method 3: update() - modifies original
result3 = d1.copy()  # Must copy to avoid modifying d1
result3.update(d2)   # {'a': 1, 'b': 3, 'c': 4}
```

**All three produce same result** when d2 values override d1.

**Performance:**
```python
# Fastest for small dicts: ** unpacking
result = {**d1, **d2}

# Cleanest (Python 3.9+): |
result = d1 | d2

# Most flexible: update (allows multiple sources)
result = {}
result.update(d1)
result.update(d2)
result.update(d3)
```

### Answer 10: Nested Data Structures
```python
def flatten_list(nested_list):
    """Flatten nested list of arbitrary depth"""
    result = []
    
    for item in nested_list:
        if isinstance(item, list):
            # Recursive call for nested lists
            result.extend(flatten_list(item))
        else:
            result.append(item)
    
    return result

# Test
nested = [1, [2, 3, [4, 5]], 6, [7, [8, [9]]]]
print(flatten_list(nested))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Alternative: using generator
def flatten_generator(nested_list):
    """Generator version"""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_generator(item)
        else:
            yield item

result = list(flatten_generator(nested))

# One-liner using recursion
flatten = lambda lst: [item for sublist in lst for item in (
    flatten(sublist) if isinstance(sublist, list) else [sublist]
)]
```

## Level: Hard (11-15)

### Answer 11: Custom Hash for Dictionary Keys
```python
class Point:
    """Point that can be used as dictionary key"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __hash__(self):
        """
        Combine hashes of components
        Must be consistent with __eq__
        """
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        """
        Define equality
        Required for dictionary key lookup
        """
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Usage
p1 = Point(10, 20)
p2 = Point(10, 20)
p3 = Point(30, 40)

print(p1 == p2)  # True
print(hash(p1) == hash(p2))  # True

# Use as dictionary key
locations = {
    p1: "Location A",
    p3: "Location B"
}

print(locations[p2])  # "Location A" - p2 equals p1

# Important rules:
# 1. If a == b, then hash(a) == hash(b)
# 2. Immutable objects only (or fake immutability)
# 3. Hash should not change during object lifetime

# Wrong example (mutable):
class BadPoint:
    def __init__(self, x, y):
        self.x = x  # Mutable!
        self.y = y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

bp = BadPoint(10, 20)
d = {bp: "value"}
bp.x = 30  # Changed hash!
print(bp in d)  # False - can't find it anymore!
```

### Answer 12: LRU Cache Implementation
```python
from collections import OrderedDict

class LRUCache:
    """
    LRU Cache with O(1) get and put
    Uses OrderedDict for O(1) operations
    """
    
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        """
        Get value and mark as recently used
        O(1) time complexity
        """
        if key not in self.cache:
            return -1
        
        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        """
        Put value and evict LRU if needed
        O(1) time complexity
        """
        if key in self.cache:
            # Update and move to end
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        # Evict least recently used (first item)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
    
    def __repr__(self):
        return f"LRUCache({dict(self.cache)})"

# Manual implementation with doubly linked list
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCacheManual:
    """LRU Cache with manual doubly linked list"""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> node
        # Dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        """Remove node from linked list"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_end(self, node):
        """Add node before tail (most recent)"""
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node
    
    def get(self, key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # Move to end (most recent)
        self._remove(node)
        self._add_to_end(node)
        return node.value
    
    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        
        node = Node(key, value)
        self._add_to_end(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            # Remove least recent (after head)
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

# Test
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))    # 1
cache.put(3, 3)        # Evicts key 2
print(cache.get(2))    # -1 (not found)
cache.put(4, 4)        # Evicts key 1
print(cache.get(1))    # -1
print(cache.get(3))    # 3
print(cache.get(4))    # 4
```

### Answer 13: Deque vs List
**Deque advantages:**
- O(1) append/pop from both ends
- Thread-safe
- Memory efficient for queue operations

**List advantages:**
- O(1) random access
- Less memory overhead per element
- Simpler

```python
from collections import deque
import timeit

# Scenario: Queue operations (FIFO)
# List: O(n) for pop(0)
def list_queue():
    q = []
    for i in range(1000):
        q.append(i)
    for i in range(1000):
        q.pop(0)  # O(n) - slow!

# Deque: O(1) for popleft()
def deque_queue():
    q = deque()
    for i in range(1000):
        q.append(i)
    for i in range(1000):
        q.popleft()  # O(1) - fast!

# Benchmark
list_time = timeit.timeit(list_queue, number=100)
deque_time = timeit.timeit(deque_queue, number=100)

print(f"List: {list_time:.4f}s")
print(f"Deque: {deque_time:.4f}s")
print(f"Deque is {list_time/deque_time:.1f}x faster")

# Use cases for deque
# 1. Queue (FIFO)
from collections import deque
queue = deque()
queue.append('a')  # Enqueue
item = queue.popleft()  # Dequeue

# 2. Stack (LIFO) - though list is fine here
stack = deque()
stack.append('a')  # Push
item = stack.pop()  # Pop

# 3. Sliding window
def sliding_window_max(nums, k):
    """Max in sliding window of size k"""
    dq = deque()
    result = []
    
    for i, num in enumerate(nums):
        # Remove elements outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# 4. Fixed-size buffer
buffer = deque(maxlen=5)  # Auto-evicts oldest
for i in range(10):
    buffer.append(i)
print(buffer)  # deque([5, 6, 7, 8, 9])
```

### Answer 14: Counter and Defaultdict
```python
from collections import defaultdict, Counter

text = "hello world hello python world"
words = text.split()

# Method 1: Regular dict with if-else
counts1 = {}
for word in words:
    if word in counts1:
        counts1[word] += 1
    else:
        counts1[word] = 1

# Method 2: dict.get()
counts2 = {}
for word in words:
    counts2[word] = counts2.get(word, 0) + 1

# Method 3: defaultdict
counts3 = defaultdict(int)
for word in words:
    counts3[word] += 1

# Method 4: Counter
counts4 = Counter(words)

print(counts4)  # Counter({'hello': 2, 'world': 2, 'python': 1})

# Counter bonus methods
print(counts4.most_common(2))  # [('hello', 2), ('world', 2)]
print(counts4['missing'])  # 0 (not KeyError)

# Combine counters
c1 = Counter(['a', 'b', 'c'])
c2 = Counter(['b', 'c', 'd'])
print(c1 + c2)  # Counter({'b': 2, 'c': 2, 'a': 1, 'd': 1})
print(c1 - c2)  # Counter({'a': 1})

# Trade-offs:
# Regular dict: Most control, verbose
# dict.get(): Clean, explicit
# defaultdict: Clean, fast, need to know default type
# Counter: Most features, overhead for simple counting
```

### Answer 15: Memory-Efficient Data Structures
```python
import sys

n = 1_000_000

# Method 1: List of booleans
list_bools = [False] * n
print(f"List of bools: {sys.getsizeof(list_bools):,} bytes")
# ~8MB (each bool is a PyObject)

# Method 2: Set of indices (sparse - only True indices)
set_indices = {i for i in range(0, n, 100)}  # Every 100th
print(f"Set (sparse): {sys.getsizeof(set_indices):,} bytes")
# Depends on number of True values

# Method 3: Bitarray (most efficient)
try:
    from bitarray import bitarray
    bits = bitarray(n)
    bits.setall(0)
    print(f"Bitarray: {sys.getsizeof(bits):,} bytes")
    # ~125KB (1 bit per boolean)
except ImportError:
    print("bitarray not installed")

# Method 4: bytes/bytearray (8 bools per byte)
byte_array = bytearray((n + 7) // 8)
print(f"Bytearray: {sys.getsizeof(byte_array):,} bytes")
# ~125KB

# When to use each:
# List: Need individual access, modifications
# Set: Sparse data (few True values), need set operations
# Bitarray: Dense data, memory critical
# Bytearray: Dense data, no external dependency

# Bitarray operations
def set_bit(byte_array, index):
    byte_array[index // 8] |= 1 << (index % 8)

def get_bit(byte_array, index):
    return bool(byte_array[index // 8] & (1 << (index % 8)))

def clear_bit(byte_array, index):
    byte_array[index // 8] &= ~(1 << (index % 8))
```

## Bonus Challenge

### Answer 16: Implement a Trie
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """Prefix tree for efficient string operations"""
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert word into trie - O(m) where m = len(word)"""
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
    
    def search(self, word):
        """Search exact word - O(m)"""
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_end_of_word
    
    def startsWith(self, prefix):
        """Check if any word starts with prefix - O(m)"""
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True
    
    def delete(self, word):
        """Delete word from trie"""
        def _delete(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            
            char = word[index]
            if char not in node.children:
                return False
            
            should_delete = _delete(node.children[char], word, index + 1)
            
            if should_delete:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word
            
            return False
        
        _delete(self.root, word, 0)
    
    def autocomplete(self, prefix):
        """Get all words with given prefix"""
        node = self.root
        
        # Navigate to prefix
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # Collect all words from this node
        words = []
        
        def dfs(node, current_word):
            if node.is_end_of_word:
                words.append(prefix + current_word)
            
            for char, child in node.children.items():
                dfs(child, current_word + char)
        
        dfs(node, "")
        return words

# Test
trie = Trie()
words = ["apple", "app", "apricot", "banana", "band"]

for word in words:
    trie.insert(word)

print(trie.search("app"))        # True
print(trie.search("appl"))       # False
print(trie.startsWith("app"))    # True
print(trie.autocomplete("app"))  # ['app', 'apple', 'apricot']

trie.delete("app")
print(trie.search("app"))        # False
print(trie.search("apple"))      # True (not deleted)
```

### Answer 17: Design a Time-Based Key-Value Store
```python
from collections import defaultdict
import bisect

class TimeBasedKV:
    """
    Time-based key-value store
    - set(key, value, timestamp): O(1)
    - get(key, timestamp): O(log n) binary search
    """
    
    def __init__(self):
        # key -> list of (timestamp, value) tuples
        self.store = defaultdict(list)
    
    def set(self, key, value, timestamp):
        """
        Store value with timestamp
        Assumes timestamps are in increasing order
        """
        self.store[key].append((timestamp, value))
    
    def get(self, key, timestamp):
        """
        Get value at or before timestamp
        Returns None if no value exists
        """
        if key not in self.store:
            return None
        
        values = self.store[key]
        
        # Binary search for largest timestamp <= query timestamp
        # Find rightmost position where timestamp <= query
        left, right = 0, len(values) - 1
        result = None
        
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    # Alternative using bisect
    def get_bisect(self, key, timestamp):
        """Using bisect for cleaner code"""
        if key not in self.store:
            return None
        
        values = self.store[key]
        timestamps = [t for t, v in values]
        
        # Find insertion point
        idx = bisect.bisect_right(timestamps, timestamp)
        
        if idx == 0:
            return None
        
        return values[idx - 1][1]

# Test
kv = TimeBasedKV()
kv.set("foo", "bar", 1)
kv.set("foo", "baz", 3)
kv.set("foo", "qux", 5)

print(kv.get("foo", 0))  # None
print(kv.get("foo", 1))  # "bar"
print(kv.get("foo", 2))  # "bar" (uses value from t=1)
print(kv.get("foo", 3))  # "baz"
print(kv.get("foo", 4))  # "baz" (uses value from t=3)
print(kv.get("foo", 10)) # "qux"
```

### Answer 18: Ring Buffer
```python
class RingBuffer:
    """
    Circular/Ring buffer with fixed size
    Overwrites oldest data when full
    """
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0  # Next write position
        self.size = 0  # Current size
    
    def append(self, item):
        """Add item, overwrite oldest if full - O(1)"""
        self.buffer[self.head] = item
        self.head = (self.head + 1) % self.capacity
        
        if self.size < self.capacity:
            self.size += 1
    
    def get(self, index):
        """Get item at logical index - O(1)"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        # Calculate actual position
        if self.size < self.capacity:
            return self.buffer[index]
        else:
            # Buffer is full, oldest is at head
            actual_index = (self.head + index) % self.capacity
            return self.buffer[actual_index]
    
    def to_list(self):
        """Convert to list in correct order"""
        if self.size < self.capacity:
            return self.buffer[:self.size]
        else:
            # Reorder from head
            return self.buffer[self.head:] + self.buffer[:self.head]
    
    def __len__(self):
        return self.size
    
    def __repr__(self):
        return f"RingBuffer({self.to_list()})"

# Using deque (simpler)
from collections import deque

class RingBufferSimple:
    """Ring buffer using deque"""
    
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)
    
    def append(self, item):
        self.buffer.append(item)  # Auto-evicts oldest
    
    def get(self, index):
        return self.buffer[index]
    
    def to_list(self):
        return list(self.buffer)

# Test
rb = RingBuffer(5)
for i in range(8):
    rb.append(i)
    print(f"After {i}: {rb}")

# Output:
# After 0: RingBuffer([0])
# After 1: RingBuffer([0, 1])
# After 2: RingBuffer([0, 1, 2])
# After 3: RingBuffer([0, 1, 2, 3])
# After 4: RingBuffer([0, 1, 2, 3, 4])
# After 5: RingBuffer([1, 2, 3, 4, 5])  # Overwrote 0
# After 6: RingBuffer([2, 3, 4, 5, 6])  # Overwrote 1
# After 7: RingBuffer([3, 4, 5, 6, 7])  # Overwrote 2
```
