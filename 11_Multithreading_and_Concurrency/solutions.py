"""
Solutions to Multithreading and Concurrency Exercises

This file contains complete solutions to all exercises.
Study these after attempting the exercises yourself.
"""

import threading
import time
import random
from queue import Queue, PriorityQueue
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed


# Solution 1: Concurrent URL Downloader
print("=" * 60)
print("Solution 1: Concurrent URL Downloader")
print("=" * 60)

def download_url(url):
    """Download URL simulation"""
    print(f"Starting download: {url}")
    time.sleep(random.uniform(1, 2))
    print(f"Completed download: {url}")
    return f"Downloaded: {url}"

urls = [
    "http://example.com/file1.pdf",
    "http://example.com/file2.pdf",
    "http://example.com/file3.pdf",
    "http://example.com/file4.pdf",
    "http://example.com/file5.pdf",
]

threads = []
for url in urls:
    thread = threading.Thread(target=download_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All downloads completed!\n")


# Solution 2: Thread-Safe Bank Account
print("=" * 60)
print("Solution 2: Thread-Safe Bank Account")
print("=" * 60)

class BankAccount:
    """Thread-safe bank account implementation"""

    def __init__(self, initial_balance=0):
        self._balance = initial_balance
        self._lock = threading.Lock()

    def deposit(self, amount):
        """Deposit money into account"""
        with self._lock:
            print(f"Depositing {amount}")
            self._balance += amount
            print(f"New balance after deposit: {self._balance}")

    def withdraw(self, amount):
        """Withdraw money from account (prevent overdraft)"""
        with self._lock:
            if self._balance >= amount:
                print(f"Withdrawing {amount}")
                self._balance -= amount
                print(f"New balance after withdrawal: {self._balance}")
                return True
            else:
                print(f"Insufficient funds for withdrawal of {amount}")
                return False

    def get_balance(self):
        """Get current balance"""
        with self._lock:
            return self._balance


# Test the bank account
account = BankAccount(1000)

def make_deposits(account, num_deposits):
    for _ in range(num_deposits):
        account.deposit(50)
        time.sleep(0.01)

def make_withdrawals(account, num_withdrawals):
    for _ in range(num_withdrawals):
        account.withdraw(30)
        time.sleep(0.01)

deposit_threads = [
    threading.Thread(target=make_deposits, args=(account, 5))
    for _ in range(3)
]

withdraw_threads = [
    threading.Thread(target=make_withdrawals, args=(account, 5))
    for _ in range(3)
]

for t in deposit_threads + withdraw_threads:
    t.start()

for t in deposit_threads + withdraw_threads:
    t.join()

print(f"Final balance: {account.get_balance()}")
print(f"Expected: 1000 + (3*5*50) - (3*5*30) = {1000 + (3*5*50) - (3*5*30)}\n")


# Solution 3: Priority Task Queue
print("=" * 60)
print("Solution 3: Priority Task Queue")
print("=" * 60)

def producer_with_priority(queue, num_tasks):
    """Produce tasks with different priorities"""
    for i in range(num_tasks):
        priority = random.randint(1, 5)
        task = f"Task-{i}"
        queue.put((priority, task))
        print(f"Producer: Created {task} with priority {priority}")
        time.sleep(0.1)
    queue.put((0, None))  # Sentinel with highest priority

def consumer_with_priority(queue, consumer_id):
    """Consume tasks based on priority"""
    while True:
        priority, task = queue.get()
        if task is None:
            queue.put((0, None))  # Pass sentinel to other consumers
            break
        print(f"Consumer-{consumer_id}: Processing {task} (priority {priority})")
        time.sleep(0.3)
        queue.task_done()

priority_queue = PriorityQueue()

producer = threading.Thread(target=producer_with_priority, args=(priority_queue, 10))
consumers = [
    threading.Thread(target=consumer_with_priority, args=(priority_queue, i))
    for i in range(2)
]

producer.start()
for c in consumers:
    c.start()

producer.join()
for c in consumers:
    c.join()

print("Priority queue example completed!\n")


# Solution 4: Concurrent Image Processor
print("=" * 60)
print("Solution 4: Concurrent Image Processor")
print("=" * 60)

def process_image(image_name):
    """Simulate image processing"""
    print(f"Processing {image_name}...")
    time.sleep(random.uniform(0.5, 1.5))
    result = {
        'name': image_name,
        'size': random.randint(1000, 5000),
        'status': 'processed'
    }
    print(f"Completed {image_name}")
    return result

images = [f"image_{i}.jpg" for i in range(10)]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(process_image, images))

print(f"Processed {len(results)} images")
print(f"Sample results: {results[:2]}\n")


# Solution 5: API Rate Limiter
print("=" * 60)
print("Solution 5: API Rate Limiter")
print("=" * 60)

api_semaphore = threading.Semaphore(3)  # Max 3 concurrent calls

def make_api_call(call_id):
    """Make API call with rate limiting"""
    print(f"API Call {call_id}: Requesting access...")
    with api_semaphore:
        print(f"API Call {call_id}: Access granted, making call...")
        time.sleep(1)  # Simulate API call
        print(f"API Call {call_id}: Call completed")
    print(f"API Call {call_id}: Released")

api_threads = [
    threading.Thread(target=make_api_call, args=(i,))
    for i in range(10)
]

for t in api_threads:
    t.start()

for t in api_threads:
    t.join()

print("API rate limiting completed!\n")


# Solution 6: Fix Deadlock
print("=" * 60)
print("Solution 6: Fix Deadlock")
print("=" * 60)

lock_a = threading.Lock()
lock_b = threading.Lock()

def task_one_fixed():
    """Fixed: Always acquire locks in same order"""
    with lock_a:
        print("Task 1: Acquired lock A")
        time.sleep(0.1)
        with lock_b:
            print("Task 1: Acquired lock B")
            print("Task 1: Both locks acquired!")

def task_two_fixed():
    """Fixed: Same lock order as task_one"""
    with lock_a:  # Changed from lock_b
        print("Task 2: Acquired lock A")
        time.sleep(0.1)
        with lock_b:  # Changed from lock_a
            print("Task 2: Acquired lock B")
            print("Task 2: Both locks acquired!")

t1 = threading.Thread(target=task_one_fixed)
t2 = threading.Thread(target=task_two_fixed)

t1.start()
t2.start()

t1.join()
t2.join()

print("Deadlock fixed! Both tasks completed.\n")


# Solution 7: Event-Driven File Watcher
print("=" * 60)
print("Solution 7: Event-Driven File Watcher")
print("=" * 60)

file_ready_event = threading.Event()

def create_file():
    """Simulate file creation"""
    print("File creator: Creating file...")
    time.sleep(2)
    print("File creator: File ready!")
    file_ready_event.set()

def wait_for_file(worker_id):
    """Wait for file to be ready"""
    print(f"Worker-{worker_id}: Waiting for file...")
    file_ready_event.wait()
    print(f"Worker-{worker_id}: File is ready, processing...")
    time.sleep(0.5)
    print(f"Worker-{worker_id}: Processing complete")

creator = threading.Thread(target=create_file)
waiters = [
    threading.Thread(target=wait_for_file, args=(i,))
    for i in range(3)
]

for w in waiters:
    w.start()

creator.start()

creator.join()
for w in waiters:
    w.join()

print("File watcher pattern completed!\n")


# Solution 8: Concurrent Web Scraper
print("=" * 60)
print("Solution 8: Concurrent Web Scraper")
print("=" * 60)

def scrape_page(url):
    """Simulate web scraping"""
    print(f"Scraping {url}...")
    time.sleep(random.uniform(1, 3))
    return {
        'url': url,
        'word_count': random.randint(100, 1000),
        'title': f"Title from {url}",
        'status': 'success'
    }

urls_to_scrape = [
    "http://example.com/page1",
    "http://example.com/page2",
    "http://example.com/page3",
    "http://example.com/page4",
    "http://example.com/page5",
]

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(scrape_page, url) for url in urls_to_scrape]
    results = []
    for future in as_completed(futures):
        result = future.result()
        results.append(result)
        print(f"Scraped: {result['url']} - {result['word_count']} words")

print(f"Total pages scraped: {len(results)}\n")


# Solution 9: Thread-Safe Cache
print("=" * 60)
print("Solution 9: Thread-Safe Cache")
print("=" * 60)

class ThreadSafeCache:
    """Thread-safe cache implementation"""

    def __init__(self, max_size=100):
        self._cache = {}
        self._max_size = max_size
        self._lock = threading.RLock()

    def get(self, key):
        """Get value from cache"""
        with self._lock:
            value = self._cache.get(key)
            if value is not None:
                print(f"Cache HIT: {key}")
            else:
                print(f"Cache MISS: {key}")
            return value

    def set(self, key, value):
        """Set value in cache"""
        with self._lock:
            if len(self._cache) >= self._max_size and key not in self._cache:
                # Simple eviction: remove first item
                first_key = next(iter(self._cache))
                del self._cache[first_key]
                print(f"Cache EVICT: {first_key}")
            self._cache[key] = value
            print(f"Cache SET: {key} = {value}")

    def size(self):
        """Get cache size"""
        with self._lock:
            return len(self._cache)


cache = ThreadSafeCache(max_size=5)

def cache_worker(worker_id):
    """Worker that uses cache"""
    for i in range(5):
        key = f"key_{random.randint(0, 7)}"
        value = cache.get(key)
        if value is None:
            cache.set(key, f"value_{worker_id}_{i}")
        time.sleep(0.1)

cache_threads = [
    threading.Thread(target=cache_worker, args=(i,))
    for i in range(3)
]

for t in cache_threads:
    t.start()

for t in cache_threads:
    t.join()

print(f"Final cache size: {cache.size()}\n")


# Solution 10: Parallel Prime Number Finder
print("=" * 60)
print("Solution 10: Parallel Prime Number Finder")
print("=" * 60)

def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Find all prime numbers in given range"""
    print(f"Finding primes in range {start}-{end}...")
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    print(f"Found {len(primes)} primes in range {start}-{end}")
    return primes

ranges = [
    (1, 1000),
    (1001, 2000),
    (2001, 3000),
    (3001, 4000),
]

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(lambda r: find_primes_in_range(r[0], r[1]), ranges)
        all_primes = [prime for sublist in results for prime in sublist]
        print(f"Total primes found: {len(all_primes)}\n")


# Solution 11: Multi-Phase Data Processing
print("=" * 60)
print("Solution 11: Multi-Phase Data Processing")
print("=" * 60)

barrier = threading.Barrier(4)

def process_data_worker(worker_id):
    """Process data in 3 phases with barriers"""
    # Phase 1: Load data
    print(f"Worker-{worker_id}: Phase 1 - Loading data...")
    time.sleep(random.uniform(0.5, 1.5))
    print(f"Worker-{worker_id}: Phase 1 complete, waiting at barrier...")
    barrier.wait()

    # Phase 2: Process data
    print(f"Worker-{worker_id}: Phase 2 - Processing data...")
    time.sleep(random.uniform(0.5, 1.5))
    print(f"Worker-{worker_id}: Phase 2 complete, waiting at barrier...")
    barrier.wait()

    # Phase 3: Save results
    print(f"Worker-{worker_id}: Phase 3 - Saving results...")
    time.sleep(random.uniform(0.5, 1.0))
    print(f"Worker-{worker_id}: Phase 3 complete!")

workers = [
    threading.Thread(target=process_data_worker, args=(i,))
    for i in range(4)
]

for w in workers:
    w.start()

for w in workers:
    w.join()

print("Multi-phase processing completed!\n")


# Solution 12: Bounded Buffer
print("=" * 60)
print("Solution 12: Bounded Buffer")
print("=" * 60)

class BoundedBuffer:
    """Bounded buffer with Condition variable"""

    def __init__(self, max_size=5):
        self._buffer = []
        self._max_size = max_size
        self._condition = threading.Condition()

    def put(self, item):
        """Add item to buffer (wait if full)"""
        with self._condition:
            while len(self._buffer) >= self._max_size:
                print("Buffer FULL, producer waiting...")
                self._condition.wait()
            self._buffer.append(item)
            print(f"PUT: {item} (buffer size: {len(self._buffer)})")
            self._condition.notify()

    def get(self):
        """Remove item from buffer (wait if empty)"""
        with self._condition:
            while len(self._buffer) == 0:
                print("Buffer EMPTY, consumer waiting...")
                self._condition.wait()
            item = self._buffer.pop(0)
            print(f"GET: {item} (buffer size: {len(self._buffer)})")
            self._condition.notify()
            return item


buffer = BoundedBuffer(max_size=3)

def producer_bounded(buffer, items):
    """Producer for bounded buffer"""
    for item in items:
        buffer.put(item)
        time.sleep(0.5)

def consumer_bounded(buffer, num_items):
    """Consumer for bounded buffer"""
    for _ in range(num_items):
        item = buffer.get()
        time.sleep(1)

prod = threading.Thread(target=producer_bounded, args=(buffer, range(10)))
cons = threading.Thread(target=consumer_bounded, args=(buffer, 10))

prod.start()
cons.start()

prod.join()
cons.join()

print("Bounded buffer completed!\n")


# Solution 13: Ordered Results from Thread Pool
print("=" * 60)
print("Solution 13: Ordered Results from Thread Pool")
print("=" * 60)

def calculate_square(n):
    """Calculate square of number"""
    time.sleep(random.uniform(0.1, 0.5))
    return n * n

numbers = list(range(1, 11))

# Using map() preserves order
with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(calculate_square, numbers))

print("Numbers and their squares (in order):")
for num, square in zip(numbers, results):
    print(f"{num}^2 = {square}")

print()


# Solution 14: Graceful Shutdown Pattern
print("=" * 60)
print("Solution 14: Graceful Shutdown Pattern")
print("=" * 60)

stop_event = threading.Event()
work_queue = Queue()

def graceful_worker(worker_id):
    """Worker that can be stopped gracefully"""
    print(f"Worker-{worker_id}: Started")
    while not stop_event.is_set():
        try:
            # Use timeout to check stop_event periodically
            item = work_queue.get(timeout=0.5)
            print(f"Worker-{worker_id}: Processing {item}")
            time.sleep(0.3)
            work_queue.task_done()
        except:
            continue  # Queue empty, check stop_event again
    print(f"Worker-{worker_id}: Shutting down gracefully")

# Start workers
workers = [
    threading.Thread(target=graceful_worker, args=(i,))
    for i in range(3)
]

for w in workers:
    w.start()

# Add some work
for i in range(10):
    work_queue.put(f"Task-{i}")

# Wait for all work to complete
work_queue.join()

# Signal workers to stop
print("Main: Signaling workers to stop...")
stop_event.set()

# Wait for workers to finish
for w in workers:
    w.join()

print("Graceful shutdown completed!\n")


# Solution 15: Fix Race Condition in Shopping Cart
print("=" * 60)
print("Solution 15: Fix Race Condition")
print("=" * 60)

class ShoppingCart:
    """Thread-safe shopping cart"""

    def __init__(self):
        self.items = []
        self.total = 0.0
        self._lock = threading.Lock()

    def add_item(self, item, price):
        """Add item to cart - THREAD SAFE"""
        with self._lock:
            self.items.append(item)
            self.total += price
            print(f"Added {item} (${price}) - Total: ${self.total:.2f}")

    def get_total(self):
        with self._lock:
            return self.total


cart = ShoppingCart()

def add_items_to_cart(cart, thread_id):
    """Add items from different threads"""
    items = [
        ("Apple", 1.50),
        ("Banana", 0.75),
        ("Orange", 2.00),
    ]
    for item, price in items:
        cart.add_item(f"{item}-{thread_id}", price)
        time.sleep(0.01)

cart_threads = [
    threading.Thread(target=add_items_to_cart, args=(cart, i))
    for i in range(3)
]

for t in cart_threads:
    t.start()

for t in cart_threads:
    t.join()

expected_total = 3 * (1.50 + 0.75 + 2.00)
print(f"Final total: ${cart.get_total():.2f}")
print(f"Expected: ${expected_total:.2f}")
print(f"Correct: {abs(cart.get_total() - expected_total) < 0.01}\n")


print("=" * 60)
print("All solutions completed!")
print("=" * 60)
