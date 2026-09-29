# File Handling - Interview Answers

## Level: Normal (1-5)

### Answer 1: File Opening Modes
- 'r': Read (default), error if file doesn't exist
- 'w': Write, creates new or truncates existing
- 'a': Append, creates if doesn't exist
- 'r+': Read+write, error if doesn't exist
- 'w+': Write+read, truncates existing
- 'rb'/'wb': Binary mode

### Answer 2: Context Managers
```python
# Without context manager (BAD)
f = open('file.txt')
data = f.read()
f.close()  # Might not execute if exception occurs

# With context manager (GOOD)
with open('file.txt') as f:
    data = f.read()
# File automatically closed, even if exception
```

### Answer 3: Reading Methods
```python
# read() - entire file
with open('file.txt') as f:
    content = f.read()

# readline() - one line
with open('file.txt') as f:
    line = f.readline()

# readlines() - list of lines
with open('file.txt') as f:
    lines = f.readlines()

# Iteration (BEST for large files)
with open('file.txt') as f:
    for line in f:
        process(line)
```

### Answer 4: File Paths
```python
from pathlib import Path
import os

# Using pathlib (recommended)
path = Path('folder') / 'file.txt'
path.read_text()

# Using os.path
path = os.path.join('folder', 'file.txt')
```

### Answer 5: File Existence Check
```python
from pathlib import Path
import os

# Method 1: pathlib
if Path('file.txt').exists():
    pass

# Method 2: os.path
if os.path.exists('file.txt'):
    pass

# Check if it's a file
if Path('file.txt').is_file():
    pass
```

## Level: Medium (6-10)

### Answer 6: Large File Processing
```python
def process_large_file(filename, chunk_size=8192):
    """Process large file in chunks"""
    with open(filename, 'rb') as f:
        while chunk := f.read(chunk_size):
            process_chunk(chunk)

# Or line by line
def process_line_by_line(filename):
    with open(filename) as f:
        for line in f:
            process_line(line)
```

### Answer 7: CSV vs JSON
```python
import csv
import json

# CSV - tabular data, Excel compatibility
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age'])
    writer.writerow(['Alice', 30])

# JSON - nested data, web APIs
data = {'name': 'Alice', 'age': 30}
with open('data.json', 'w') as f:
    json.dump(data, f)
```

### Answer 10: Temporary Files
```python
import tempfile

# Temporary file (auto-deleted)
with tempfile.NamedTemporaryFile(mode='w', delete=True) as f:
    f.write('temporary data')
    f.flush()
    # File deleted after context

# Temporary directory
with tempfile.TemporaryDirectory() as tmpdir:
    # Use tmpdir
    pass  # Directory deleted after
```

## Level: Hard (11-15)

### Answer 12: Atomic File Writes
```python
import os
import tempfile

def atomic_write(filename, content):
    """Atomic file write using write-then-rename"""
    dir_name = os.path.dirname(filename) or '.'
    
    # Write to temporary file
    with tempfile.NamedTemporaryFile(
        mode='w',
        dir=dir_name,
        delete=False
    ) as temp_file:
        temp_file.write(content)
        temp_name = temp_file.name
    
    # Atomic rename
    os.replace(temp_name, filename)
```

### Answer 15: File Compression
```python
import gzip
import zipfile

# Gzip
with gzip.open('file.gz', 'wt') as f:
    f.write('compressed data')

with gzip.open('file.gz', 'rt') as f:
    data = f.read()

# Zip
with zipfile.ZipFile('archive.zip', 'w') as z:
    z.write('file.txt')

with zipfile.ZipFile('archive.zip', 'r') as z:
    z.extractall('output_dir')
```
