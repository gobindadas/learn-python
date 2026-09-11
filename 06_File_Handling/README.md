# Module 06: File Handling

Learn to read from and write to files, essential for data persistence and processing!

## Topics to Cover

1. **Reading Files**
   - Opening files with `open()`
   - Reading entire file vs line by line
   - The `with` statement (context manager)
   - File modes: 'r', 'w', 'a', 'r+'

2. **Writing Files**
   - Creating new files
   - Writing text to files
   - Appending to existing files
   - Overwriting files safely

3. **Working with CSV Files**
   - Reading CSV files
   - Writing CSV files
   - Using the `csv` module

4. **Working with JSON**
   - Reading JSON files
   - Writing JSON files
   - Converting between Python dicts and JSON
   - Using the `json` module

5. **File Paths**
   - Absolute vs relative paths
   - Using `os.path` module
   - Checking if files exist

6. **Error Handling with Files**
   - FileNotFoundError
   - Permission errors
   - Using try-except with files

## Key Concepts

```python
# Reading a file
with open('data.txt', 'r') as file:
    content = file.read()

# Writing to a file
with open('output.txt', 'w') as file:
    file.write("Hello, World!")

# Working with JSON
import json

data = {"name": "Alice", "age": 25}
with open('data.json', 'w') as file:
    json.dump(data, file)

with open('data.json', 'r') as file:
    loaded_data = json.load(file)
```

## Practice Ideas

1. Create a program that reads a text file and counts words
2. Build a simple contact manager that saves to a JSON file
3. Read a CSV file and calculate statistics
4. Create a log file that appends new entries
5. Build a configuration file reader

## Coming Soon

Full examples and exercises will be added. Meanwhile:
- Practice reading text files
- Create and modify files safely
- Explore the `csv` and `json` modules

## Next Module

Move to [Module 07: Object-Oriented Programming](../07_OOP/) to learn about classes and objects!
