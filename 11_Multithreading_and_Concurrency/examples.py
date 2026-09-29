"""
Multithreading and Concurrency Examples
This file demonstrates practical examples of concurrent programming in Python.
"""

import threading
import time
import random
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing


# Example 1: Basic Threading
print("=" * 60)
print("Example 1: Basic Threading")
print("=" * 60)

def print_numbers(thread_name, delay):
    """Print numbers with a delay"""
    for i in range(5):
        time.sleep(delay)
        print(f"{thread_name}: {i}")

# Create and start threads
thread1 = threading.Thread(target=print_numbers, args=("Thread-1", 0.5))
thread2 = threading.Thread(target=print_numbers, args=("Thread-2", 0.3))

thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Both threads finished!\n")


# Example 2: Thread Synchronization with Lock
print("=" * 60)
print("Example 2: Thread Synchronization (Lock)")
print("=" * 60)

counter = 0
lock = threading.Lock()

def increment_counter(name, iterations):
    """Safely increment a shared counter"""
    global counter
    for _ in range(iterations):
        with lock:  # Acquire lock
            current = counter
            time.sleep(0.0001)  # Simulate some work
            counter = current + 1
    print(f"{name} finished incrementing")

threads = []
for i in range(5):
    t = threading.Thread(target=increment_counter, args=(f"Thread-{i}", 100))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final counter value: {counter}")
print(f"Expected: {5 * 100}\n")


# Example 3: Producer-Consumer Pattern with Queue
print("=" * 60)
print("Example 3: Producer-Consumer Pattern")
print("=" * 60)

def producer(queue, num_items):
    """Produce items and put them in queue"""
    for i in range(num_items):
        item = f"Item-{i}"
        time.sleep(random.uniform(0.1, 0.3))
        queue.put(item)
        print(f"Producer: Created {item}")
    queue.put(None)  # Signal completion

def consumer(queue, consumer_id):
    """Consume items from queue"""
    while True:
        item = queue.get()
        if item is None:
            queue.put(None)  # Pass signal to other consumers
            break
        time.sleep(random.uniform(0.1, 0.5))
        print(f"Consumer-{consumer_id}: Processed {item}")
        queue.task_done()

task_queue = Queue()

# Start producer and consumers
producer_thread = threading.Thread(target=producer, args=(task_queue, 10))
consumer_threads = [
    threading.Thread(target=consumer, args=(task_queue, i))
    for i in range(3)
]

producer_thread.start()
for ct in consumer_threads:
    ct.start()

producer_thread.join()
for ct in consumer_threads:
    ct.join()

print("Producer-Consumer example completed!\n")


# Example 4: Thread Pool with concurrent.futures
print("=" * 60)
print("Example 4: ThreadPoolExecutor")
print("=" * 60)

def download_file(url):
    """Simulate downloading a file"""
    print(f"Starting download: {url}")
    time.sleep(random.uniform(1, 2))
    print(f"Completed download: {url}")
    return f"Content from {url}"

urls = [
    "http://example.com/file1",
    "http://example.com/file2",
    "http://example.com/file3",
    "http://example.com/file4",
]

# Using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(download_file, urls)

print(f"All downloads completed!\n")


# Example 5: Event for Thread Communication
print("=" * 60)
print("Example 5: Event Signaling")
print("=" * 60)

event = threading.Event()

def wait_for_event(name):
    """Wait for event to be set"""
    print(f"{name}: Waiting for event...")
    event.wait()
    print(f"{name}: Event received, continuing!")

def trigger_event():
    """Trigger event after delay"""
    print("Trigger: Sleeping for 2 seconds...")
    time.sleep(2)
    print("Trigger: Setting event!")
    event.set()

# Start waiting threads
waiters = [
    threading.Thread(target=wait_for_event, args=(f"Waiter-{i}",))
    for i in range(3)
]
for w in waiters:
    w.start()

# Trigger the event
trigger_thread = threading.Thread(target=trigger_event)
trigger_thread.start()

for w in waiters:
    w.join()
trigger_thread.join()

print("Event example completed!\n")


# Example 6: Semaphore (Limiting Concurrent Access)
print("=" * 60)
print("Example 6: Semaphore (Resource Limiting)")
print("=" * 60)

# Only allow 2 threads to access resource at once
semaphore = threading.Semaphore(2)

def access_limited_resource(thread_id):
    """Access a resource with limited concurrent access"""
    print(f"Thread-{thread_id}: Requesting access...")
    with semaphore:
        print(f"Thread-{thread_id}: Access granted! Using resource...")
        time.sleep(1)
        print(f"Thread-{thread_id}: Releasing resource...")
    print(f"Thread-{thread_id}: Done")

resource_threads = [
    threading.Thread(target=access_limited_resource, args=(i,))
    for i in range(5)
]

for rt in resource_threads:
    rt.start()

for rt in resource_threads:
    rt.join()

print("Semaphore example completed!\n")


# Example 7: Multiprocessing for CPU-bound tasks
print("=" * 60)
print("Example 7: Multiprocessing (CPU-bound)")
print("=" * 60)

def cpu_intensive_task(n):
    """CPU intensive calculation"""
    result = sum(i * i for i in range(n))
    print(f"Process {multiprocessing.current_process().name}: Calculated sum of squares up to {n}")
    return result

if __name__ == '__main__':
    # Use ProcessPoolExecutor for CPU-bound tasks
    numbers = [1000000, 2000000, 3000000, 4000000]

    print("Starting CPU-intensive tasks...")
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(cpu_intensive_task, numbers))

    print(f"Results: {results[:2]}...")  # Print first 2 results
    print("Multiprocessing example completed!\n")


# Example 8: Thread-safe Counter with RLock
print("=" * 60)
print("Example 8: RLock (Reentrant Lock)")
print("=" * 60)

class ThreadSafeCounter:
    """A thread-safe counter using RLock"""

    def __init__(self):
        self._value = 0
        self._lock = threading.RLock()

    def increment(self):
        with self._lock:
            self._value += 1

    def decrement(self):
        with self._lock:
            self._value -= 1

    def get_value(self):
        with self._lock:
            return self._value

    def increment_by(self, amount):
        """Demonstrates reentrant locking"""
        with self._lock:
            for _ in range(amount):
                self.increment()  # Can acquire lock again (reentrant)

safe_counter = ThreadSafeCounter()

def modify_counter(counter_obj, thread_id):
    for i in range(10):
        if i % 2 == 0:
            counter_obj.increment()
        else:
            counter_obj.increment_by(2)
    print(f"Thread-{thread_id} finished modifying counter")

counter_threads = [
    threading.Thread(target=modify_counter, args=(safe_counter, i))
    for i in range(3)
]

for t in counter_threads:
    t.start()

for t in counter_threads:
    t.join()

print(f"Final counter value: {safe_counter.get_value()}")
print("RLock example completed!\n")


# Example 9: Barrier Synchronization
print("=" * 60)
print("Example 9: Barrier Synchronization")
print("=" * 60)

barrier = threading.Barrier(3)

def worker_with_barrier(worker_id):
    """Worker that synchronizes at a barrier"""
    print(f"Worker-{worker_id}: Phase 1 - Doing initial work...")
    time.sleep(random.uniform(0.5, 1.5))
    print(f"Worker-{worker_id}: Phase 1 complete, waiting at barrier...")

    barrier.wait()  # All threads wait here

    print(f"Worker-{worker_id}: Phase 2 - All workers synchronized, continuing...")
    time.sleep(random.uniform(0.5, 1.0))
    print(f"Worker-{worker_id}: Phase 2 complete!")

barrier_threads = [
    threading.Thread(target=worker_with_barrier, args=(i,))
    for i in range(3)
]

for t in barrier_threads:
    t.start()

for t in barrier_threads:
    t.join()

print("Barrier example completed!\n")


# Example 10: Daemon Threads
print("=" * 60)
print("Example 10: Daemon Threads")
print("=" * 60)

def daemon_worker():
    """A daemon thread that runs in background"""
    print("Daemon: Starting background work...")
    for i in range(10):
        time.sleep(0.5)
        print(f"Daemon: Still working... {i}")
    print("Daemon: Work complete (you won't see this)")

# Create daemon thread
daemon = threading.Thread(target=daemon_worker, daemon=True)
daemon.start()

print("Main: Daemon started, sleeping for 2 seconds...")
time.sleep(2)
print("Main: Exiting (daemon will be terminated)")
# Daemon thread terminates when main program exits

print("\n" + "=" * 60)
print("All examples completed!")
print("=" * 60)
