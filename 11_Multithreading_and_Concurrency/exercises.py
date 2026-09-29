"""
Multithreading and Concurrency Exercises

Complete these exercises to practice concurrent programming in Python.
Solutions are available in solutions.py
"""

import threading
import time
import random
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


# Exercise 1: Basic Thread Creation
# Create a function that downloads multiple URLs concurrently
# Simulate download with time.sleep()
print("=" * 60)
print("Exercise 1: Concurrent URL Downloader")
print("=" * 60)
print("Task: Create 5 threads to download URLs concurrently")
print("Each download should take 1-2 seconds (simulate with sleep)")
print("Print when each download starts and completes")
print()

def download_url(url):
    """
    TODO: Implement this function
    - Print when download starts
    - Sleep for random time between 1-2 seconds
    - Print when download completes
    - Return the URL with 'Downloaded: ' prefix
    """
    pass

# TODO: Create and start 5 threads to download these URLs
urls = [
    "http://example.com/file1.pdf",
    "http://example.com/file2.pdf",
    "http://example.com/file3.pdf",
    "http://example.com/file4.pdf",
    "http://example.com/file5.pdf",
]

# Your code here


# Exercise 2: Thread-Safe Bank Account
# Implement a thread-safe bank account class
print("\n" + "=" * 60)
print("Exercise 2: Thread-Safe Bank Account")
print("=" * 60)
print("Task: Implement a BankAccount class with thread-safe deposit/withdraw")
print()

class BankAccount:
    """
    TODO: Implement a thread-safe bank account
    - Initialize with starting balance
    - Implement deposit(amount) method
    - Implement withdraw(amount) method (prevent overdraft)
    - Implement get_balance() method
    - Use locks to ensure thread safety
    """

    def __init__(self, initial_balance=0):
        pass

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def get_balance(self):
        pass


# TODO: Test with multiple threads doing deposits and withdrawals
# Create 5 threads depositing and 5 threads withdrawing
# Verify final balance is correct


# Exercise 3: Producer-Consumer with Priority
# Implement a priority-based task queue
print("\n" + "=" * 60)
print("Exercise 3: Priority Task Queue")
print("=" * 60)
print("Task: Create a producer-consumer system with task priorities")
print()

"""
TODO: Implement the following:
1. Create a PriorityQueue
2. Producer creates tasks with different priorities (1=high, 5=low)
3. Consumer processes higher priority tasks first
4. Print which task is being processed and its priority
"""

# Your code here


# Exercise 4: Thread Pool for Image Processing
# Simulate image processing with ThreadPoolExecutor
print("\n" + "=" * 60)
print("Exercise 4: Concurrent Image Processor")
print("=" * 60)
print("Task: Process multiple images concurrently using ThreadPoolExecutor")
print()

def process_image(image_name):
    """
    TODO: Simulate image processing
    - Print processing start
    - Sleep for random time (0.5-1.5 seconds)
    - Print processing complete
    - Return processed image info (dict with name, size, etc.)
    """
    pass

# TODO: Process these images using ThreadPoolExecutor (max 3 workers)
images = [f"image_{i}.jpg" for i in range(10)]

# Your code here


# Exercise 5: Rate Limiter with Semaphore
# Implement an API rate limiter
print("\n" + "=" * 60)
print("Exercise 5: API Rate Limiter")
print("=" * 60)
print("Task: Limit concurrent API calls to 3 using Semaphore")
print()

"""
TODO: Implement a rate limiter that:
- Allows max 3 concurrent API calls
- Uses Semaphore for limiting
- Simulates API call with 1 second sleep
- Prints when API call starts/ends
- Test with 10 threads trying to make API calls
"""

# Your code here


# Exercise 6: Deadlock Detection and Prevention
# Fix the deadlock in this code
print("\n" + "=" * 60)
print("Exercise 6: Fix Deadlock")
print("=" * 60)
print("Task: Fix the deadlock issue in the following code")
print()

lock_a = threading.Lock()
lock_b = threading.Lock()

def task_one():
    """This can cause deadlock"""
    with lock_a:
        print("Task 1: Acquired lock A")
        time.sleep(0.1)
        with lock_b:
            print("Task 1: Acquired lock B")

def task_two():
    """This can cause deadlock"""
    with lock_b:
        print("Task 2: Acquired lock B")
        time.sleep(0.1)
        with lock_a:
            print("Task 2: Acquired lock A")

# TODO: Fix the deadlock issue
# Hint: Ensure locks are always acquired in the same order


# Exercise 7: Event-Driven File Watcher
# Implement a simple file watcher using Events
print("\n" + "=" * 60)
print("Exercise 7: Event-Driven File Watcher")
print("=" * 60)
print("Task: Implement a file watcher that notifies when file is ready")
print()

"""
TODO: Implement file watcher pattern:
1. One thread simulates file creation (sleep 2 seconds, then signal)
2. Multiple threads wait for file to be ready
3. Use threading.Event for signaling
4. When file is ready, all waiting threads process it
"""

# Your code here


# Exercise 8: Concurrent Web Scraper
# Scrape multiple pages concurrently
print("\n" + "=" * 60)
print("Exercise 8: Concurrent Web Scraper")
print("=" * 60)
print("Task: Scrape multiple pages concurrently and collect results")
print()

def scrape_page(url):
    """
    TODO: Simulate web scraping
    - Print scraping start
    - Sleep for random time (1-3 seconds)
    - Return dict with url and simulated data (word count, title, etc.)
    """
    pass

# TODO: Scrape these URLs concurrently and print results
urls_to_scrape = [
    "http://example.com/page1",
    "http://example.com/page2",
    "http://example.com/page3",
    "http://example.com/page4",
    "http://example.com/page5",
]

# Your code here


# Exercise 9: Thread-Safe Cache
# Implement a thread-safe LRU cache
print("\n" + "=" * 60)
print("Exercise 9: Thread-Safe Cache")
print("=" * 60)
print("Task: Implement a simple thread-safe cache with get/set operations")
print()

class ThreadSafeCache:
    """
    TODO: Implement a thread-safe cache
    - Initialize with max size
    - Implement get(key) method
    - Implement set(key, value) method
    - Use RLock for thread safety
    - Optional: Implement basic LRU eviction
    """

    def __init__(self, max_size=100):
        pass

    def get(self, key):
        pass

    def set(self, key, value):
        pass

    def size(self):
        pass


# TODO: Test cache with multiple threads reading and writing


# Exercise 10: Parallel Number Crunching
# Use multiprocessing for CPU-intensive task
print("\n" + "=" * 60)
print("Exercise 10: Parallel Prime Number Finder")
print("=" * 60)
print("Task: Find prime numbers in ranges using multiprocessing")
print()

def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """
    TODO: Find all prime numbers in given range
    - Return list of prime numbers
    - Print progress
    """
    pass

# TODO: Find primes in these ranges using ProcessPoolExecutor
ranges = [
    (1, 10000),
    (10001, 20000),
    (20001, 30000),
    (30001, 40000),
]

# Your code here


# Exercise 11: Barrier Synchronization Pattern
# Synchronize multiple workers at checkpoints
print("\n" + "=" * 60)
print("Exercise 11: Multi-Phase Data Processing")
print("=" * 60)
print("Task: Process data in 3 phases with barrier synchronization")
print()

"""
TODO: Implement 3-phase processing:
- Phase 1: Load data (simulate with sleep)
- Barrier: Wait for all workers to finish loading
- Phase 2: Process data
- Barrier: Wait for all workers to finish processing
- Phase 3: Save results
- Use threading.Barrier for synchronization
- Create 4 worker threads
"""

# Your code here


# Exercise 12: Condition Variable Pattern
# Implement bounded buffer with Condition
print("\n" + "=" * 60)
print("Exercise 12: Bounded Buffer")
print("=" * 60)
print("Task: Implement a bounded buffer using Condition variable")
print()

class BoundedBuffer:
    """
    TODO: Implement bounded buffer with Condition
    - Fixed size buffer (e.g., 5 items)
    - put(item): Add item (wait if full)
    - get(): Remove item (wait if empty)
    - Use threading.Condition for synchronization
    """

    def __init__(self, max_size=5):
        pass

    def put(self, item):
        pass

    def get(self):
        pass


# TODO: Test with producer and consumer threads


# Exercise 13: Thread Pool with Results
# Get results from thread pool in order
print("\n" + "=" * 60)
print("Exercise 13: Ordered Results from Thread Pool")
print("=" * 60)
print("Task: Process tasks concurrently but return results in order")
print()

def calculate_square(n):
    """
    TODO: Calculate square of number
    - Sleep for random time
    - Return square of n
    """
    pass

# TODO: Calculate squares of numbers 1-10
# Return results in original order (not completion order)
# Hint: Use executor.map() or submit() with futures

# Your code here


# Exercise 14: Graceful Shutdown
# Implement graceful thread pool shutdown
print("\n" + "=" * 60)
print("Exercise 14: Graceful Shutdown Pattern")
print("=" * 60)
print("Task: Implement worker threads that can be gracefully stopped")
print()

"""
TODO: Create worker threads that:
1. Process items from a queue
2. Can be stopped gracefully with a stop signal
3. Complete current work before exiting
4. Use Event or sentinel value for stopping
"""

# Your code here


# Exercise 15: Race Condition Bug Fix
# Find and fix the race condition
print("\n" + "=" * 60)
print("Exercise 15: Fix Race Condition")
print("=" * 60)
print("Task: Fix the race condition in this shopping cart")
print()

class ShoppingCart:
    """This class has a race condition bug"""

    def __init__(self):
        self.items = []
        self.total = 0.0

    def add_item(self, item, price):
        """Add item to cart - HAS RACE CONDITION"""
        self.items.append(item)
        # Race condition: total might be incorrect with multiple threads
        current_total = self.total
        time.sleep(0.001)  # Simulate processing delay
        self.total = current_total + price

    def get_total(self):
        return self.total

# TODO: Fix the race condition in ShoppingCart
# Test with multiple threads adding items simultaneously


print("\n" + "=" * 60)
print("All exercises defined!")
print("Implement the solutions and compare with solutions.py")
print("=" * 60)
