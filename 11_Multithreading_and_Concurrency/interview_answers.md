# Multithreading and Concurrency - Interview Answers

## Level: Normal (1-5)

### Answer 1: Threading vs Multiprocessing
```python
# Threading: I/O-bound tasks (GIL allows I/O to release)
import threading
import time

def io_task():
    time.sleep(1)  # I/O operation
    return "done"

threads = [threading.Thread(target=io_task) for _ in range(5)]
# Runs concurrently

# Multiprocessing: CPU-bound tasks (bypasses GIL)
from multiprocessing import Process

def cpu_task():
    return sum(i**2 for i in range(1000000))

processes = [Process(target=cpu_task) for _ in range(5)]
# Runs in parallel
```

### Answer 3: Thread Synchronization
```python
import threading

# Lock: Mutual exclusion
lock = threading.Lock()
with lock:
    # Critical section
    pass

# RLock: Reentrant lock (same thread can acquire multiple times)
rlock = threading.RLock()
with rlock:
    with rlock:  # OK - same thread
        pass

# Semaphore: Limit concurrent access
sem = threading.Semaphore(3)  # Max 3 threads
with sem:
    # Max 3 threads here
    pass
```

### Answer 4: Race Conditions
```python
# Race condition (BAD)
counter = 0
def increment():
    global counter
    temp = counter
    temp += 1
    counter = temp

# Fix with Lock (GOOD)
counter = 0
lock = threading.Lock()
def increment():
    global counter
    with lock:
        counter += 1
```

## Level: Medium (6-10)

### Answer 6: Producer-Consumer Pattern
```python
from queue import Queue
import threading
import time

def producer(queue, items):
    for item in items:
        print(f"Producing {item}")
        queue.put(item)
        time.sleep(0.5)
    queue.put(None)  # Sentinel

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consuming {item}")
        time.sleep(1)
        queue.task_done()

q = Queue()
threading.Thread(target=producer, args=(q, range(5))).start()
threading.Thread(target=consumer, args=(q,)).start()
```

### Answer 8: Deadlock
```python
# Deadlock (BAD)
lock1, lock2 = threading.Lock(), threading.Lock()

def task1():
    with lock1:
        with lock2:  # Different order
            pass

def task2():
    with lock2:  # Different order
        with lock1:
            pass

# Fix: Always acquire in same order (GOOD)
def task1():
    with lock1:
        with lock2:
            pass

def task2():
    with lock1:  # Same order
        with lock2:
            pass
```

## Level: Hard (11-15)

### Answer 11: Thread-Safe Singleton
```python
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                # Double-checked locking
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
```
