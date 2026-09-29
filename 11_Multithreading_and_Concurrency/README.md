# Multithreading and Concurrency in Python

## Overview

Concurrency and parallelism are essential concepts for writing efficient programs that can handle multiple tasks simultaneously. Python provides several approaches to achieve concurrency, each suited for different use cases.

## Key Concepts

### Concurrency vs Parallelism

- **Concurrency**: Multiple tasks making progress by switching between them (not necessarily simultaneous)
- **Parallelism**: Multiple tasks executing simultaneously on different CPU cores

### The Global Interpreter Lock (GIL)

**Critical to understand**: Python has a Global Interpreter Lock (GIL) that allows only one thread to execute Python bytecode at a time, even on multi-core systems.

**Impact**:
- **CPU-bound tasks**: Multithreading doesn't help (use `multiprocessing` instead)
- **I/O-bound tasks**: Multithreading works great (network, file operations, database queries)

## Python Concurrency Options

| Approach | Best For | Pros | Cons |
|----------|----------|------|------|
| `threading` | I/O-bound tasks | Simple, shares memory | GIL limits CPU tasks |
| `multiprocessing` | CPU-bound tasks | True parallelism, bypasses GIL | Higher memory usage, IPC overhead |
| `asyncio` | I/O-bound with many connections | Very efficient for I/O | Requires async/await, learning curve |
| `concurrent.futures` | Simplified threading/processing | Clean API, easy to use | Less control than direct threading |

## Threading Module

### Basic Thread Creation

```python
import threading
import time

def worker(name):
    print(f"Thread {name} starting")
    time.sleep(2)
    print(f"Thread {name} finished")

# Method 1: Using Thread class
thread = threading.Thread(target=worker, args=("A",))
thread.start()
thread.join()  # Wait for thread to finish

# Method 2: Subclassing Thread
class WorkerThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def run(self):
        print(f"Thread {self.name} starting")
        time.sleep(2)
        print(f"Thread {self.name} finished")

thread = WorkerThread("B")
thread.start()
thread.join()
```

### Thread Synchronization

#### Lock (Mutex)
Prevents multiple threads from accessing shared resources simultaneously.

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:  # Acquire and release lock automatically
        temp = counter
        temp += 1
        counter = temp
```

#### RLock (Reentrant Lock)
A lock that can be acquired multiple times by the same thread.

```python
rlock = threading.RLock()

def recursive_function(n):
    with rlock:
        if n > 0:
            recursive_function(n - 1)
```

#### Semaphore
Limits the number of threads accessing a resource.

```python
# Allow max 3 threads to access resource
semaphore = threading.Semaphore(3)

def access_resource():
    with semaphore:
        # Only 3 threads can be here at once
        print(f"Accessing resource: {threading.current_thread().name}")
        time.sleep(2)
```

#### Event
Used for thread communication and signaling.

```python
event = threading.Event()

def waiter():
    print("Waiting for event...")
    event.wait()  # Block until event is set
    print("Event received!")

def setter():
    time.sleep(2)
    print("Setting event")
    event.set()  # Signal all waiting threads
```

#### Condition
Advanced synchronization with wait/notify pattern.

```python
condition = threading.Condition()
items = []

def consumer():
    with condition:
        while not items:
            condition.wait()  # Wait for notification
        item = items.pop(0)
        print(f"Consumed: {item}")

def producer():
    with condition:
        items.append("item")
        condition.notify()  # Wake up one waiting thread
```

#### Barrier
Synchronizes multiple threads at a specific point.

```python
barrier = threading.Barrier(3)  # Wait for 3 threads

def worker(n):
    print(f"Thread {n} working...")
    time.sleep(n)
    barrier.wait()  # All threads wait here until 3 arrive
    print(f"Thread {n} continuing...")
```

### Thread-Safe Data Structures

```python
from queue import Queue, LifoQueue, PriorityQueue

# Thread-safe FIFO queue
q = Queue()
q.put(item)
item = q.get()

# Thread-safe LIFO (stack)
stack = LifoQueue()

# Thread-safe priority queue
pq = PriorityQueue()
pq.put((priority, item))
```

## Multiprocessing Module

Bypass GIL by using separate processes.

```python
from multiprocessing import Process, Pool, Queue, Lock

def worker(name):
    print(f"Process {name} starting")

# Basic process
p = Process(target=worker, args=("A",))
p.start()
p.join()

# Process Pool for parallel execution
def square(n):
    return n * n

with Pool(processes=4) as pool:
    results = pool.map(square, [1, 2, 3, 4, 5])
    print(results)  # [1, 4, 9, 16, 25]

# Inter-process communication
queue = Queue()
queue.put("message")
message = queue.get()
```

## Concurrent.futures Module

High-level interface for threading and multiprocessing.

### ThreadPoolExecutor

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def task(n):
    time.sleep(1)
    return n * n

# Submit individual tasks
with ThreadPoolExecutor(max_workers=3) as executor:
    future = executor.submit(task, 5)
    result = future.result()  # Wait for result
    
# Map multiple tasks
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, [1, 2, 3, 4, 5])
    print(list(results))

# Handle results as they complete
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, i) for i in range(5)]
    for future in as_completed(futures):
        print(future.result())
```

### ProcessPoolExecutor

Same API as ThreadPoolExecutor, but uses processes.

```python
from concurrent.futures import ProcessPoolExecutor

def cpu_intensive(n):
    return sum(i * i for i in range(n))

with ProcessPoolExecutor(max_workers=4) as executor:
    results = executor.map(cpu_intensive, [10**6, 10**6, 10**6])
    print(list(results))
```

## Asyncio (Asynchronous I/O)

Event loop-based concurrency for I/O-bound tasks.

```python
import asyncio

async def fetch_data(n):
    print(f"Fetching {n}...")
    await asyncio.sleep(1)  # Non-blocking sleep
    print(f"Done {n}")
    return n * n

async def main():
    # Run tasks concurrently
    tasks = [fetch_data(i) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print(results)

# Run the async function
asyncio.run(main())
```

### Async with HTTP requests

```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['http://example.com', 'http://example.org']
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

asyncio.run(main())
```

## Common Patterns

### Producer-Consumer Pattern

```python
from queue import Queue
import threading

def producer(queue, items):
    for item in items:
        print(f"Producing {item}")
        queue.put(item)
    queue.put(None)  # Sentinel value to signal completion

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consuming {item}")
        queue.task_done()

q = Queue()
producer_thread = threading.Thread(target=producer, args=(q, range(5)))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
```

### Thread Pool Pattern

```python
from concurrent.futures import ThreadPoolExecutor

def process_item(item):
    # Process item
    return item * 2

items = range(10)
with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(process_item, items))
```

## Best Practices

1. **Choose the right tool**:
   - I/O-bound + simple: `threading` or `concurrent.futures.ThreadPoolExecutor`
   - I/O-bound + many connections: `asyncio`
   - CPU-bound: `multiprocessing` or `concurrent.futures.ProcessPoolExecutor`

2. **Avoid shared state**: Minimize shared mutable data between threads/processes

3. **Use synchronization primitives**: Always protect shared resources with locks

4. **Prefer `with` statements**: Ensures proper lock acquisition/release

5. **Use thread-safe data structures**: `queue.Queue` instead of regular lists

6. **Handle exceptions**: Exceptions in threads don't propagate to the main thread

7. **Join threads/processes**: Always wait for completion with `.join()`

8. **Use daemon threads carefully**: Daemon threads terminate when main program exits

9. **Avoid deadlocks**:
   - Always acquire locks in the same order
   - Use timeouts: `lock.acquire(timeout=5)`
   - Use context managers

10. **Profile first**: Measure performance before and after adding concurrency

## Common Pitfalls

### Race Conditions
```python
# WRONG - Race condition
counter = 0

def increment():
    global counter
    counter += 1  # Not atomic!

# RIGHT - Using lock
counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        counter += 1
```

### Deadlock
```python
# WRONG - Can cause deadlock
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    with lock1:
        with lock2:
            pass

def thread2():
    with lock2:  # Different order!
        with lock1:
            pass

# RIGHT - Same order in all threads
def thread2():
    with lock1:
        with lock2:
            pass
```

### Memory Sharing Issues
```python
# WRONG - Lists are not thread-safe
results = []

def worker():
    results.append(data)  # Race condition!

# RIGHT - Use Queue
from queue import Queue
results = Queue()

def worker():
    results.put(data)
```

## Performance Comparison

```python
import time
from threading import Thread
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def cpu_bound(n):
    return sum(i * i for i in range(n))

def io_bound():
    time.sleep(1)

# Compare different approaches
# For CPU-bound: multiprocessing wins
# For I/O-bound: threading or asyncio wins
```

## Debugging Concurrent Code

```python
import threading

# Get all active threads
print(threading.enumerate())

# Get current thread
print(threading.current_thread().name)

# Check if thread is alive
print(thread.is_alive())

# Use logging instead of print (thread-safe)
import logging
logging.basicConfig(level=logging.DEBUG, 
                   format='%(threadName)s: %(message)s')
```

## Resources

- Python Threading Documentation: https://docs.python.org/3/library/threading.html
- Python Multiprocessing: https://docs.python.org/3/library/multiprocessing.html
- Python Asyncio: https://docs.python.org/3/library/asyncio.html
- PEP 3156: Asynchronous IO Support

## Summary

- **Threading**: Good for I/O-bound tasks, limited by GIL for CPU tasks
- **Multiprocessing**: True parallelism for CPU-bound tasks
- **Asyncio**: Efficient for I/O-bound with many concurrent connections
- **Concurrent.futures**: High-level, clean API for both threading and multiprocessing
- Always use proper synchronization to avoid race conditions and deadlocks
