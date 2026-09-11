# Getting Started with Python

Welcome! This guide will help you start your Python learning journey.

## Step 1: Verify Python Installation

First, check if Python is installed on your system:

```bash
python3 --version
```

You should see something like: `Python 3.8.10` or higher.

If Python is not installed:
- **Linux (Fedora/RHEL)**: `sudo dnf install python3`
- **Ubuntu/Debian**: `sudo apt install python3`
- **macOS**: `brew install python3`
- **Windows**: Download from [python.org](https://www.python.org/downloads/)

## Step 2: Your First Python Program

Let's write your first program!

1. Navigate to Module 01:
```bash
cd 01_Basics
```

2. Create a file called `hello.py`:
```bash
echo 'print("Hello, Python!")' > hello.py
```

3. Run it:
```bash
python3 hello.py
```

You should see: `Hello, Python!`

Congratulations! You've written your first Python program!

## Step 3: Explore Module 01

Now that Python works, start learning:

1. **Read the theory**:
```bash
cat README.md  # Or open in your favorite text editor
```

2. **Run the examples**:
```bash
python3 examples.py
```

3. **Try the exercises**:
```bash
python3 exercises.py
```

4. **Check solutions** (after trying):
```bash
python3 solutions.py
```

## Learning Path

Follow these modules in order:

### Week 1-2: Foundations
1. **Module 01: Python Basics** (3-4 days)
   - Variables, data types, operators
   - Input/output
   - Practice exercises daily

2. **Module 02: Control Flow** (3-4 days)
   - If statements
   - Loops (for, while)
   - Practice with patterns

3. **Module 03: Data Structures** (4-5 days)
   - Lists, tuples
   - Dictionaries, sets
   - List comprehensions

### Week 3-4: Building Blocks
4. **Module 04: Functions** (4-5 days)
   - Defining functions
   - Parameters and returns
   - Lambda functions

5. **Module 05: Modules** (2-3 days)
   - Importing modules
   - Built-in modules
   - Creating your own

6. **Module 06: File Handling** (3-4 days)
   - Reading/writing files
   - JSON and CSV
   - File operations

### Week 5-6: Advanced Concepts
7. **Module 07: OOP** (5-6 days)
   - Classes and objects
   - Inheritance
   - Encapsulation

8. **Module 08: Error Handling** (2-3 days)
   - Try-except blocks
   - Exception types
   - Best practices

9. **Module 09: Advanced Topics** (4-5 days)
   - Decorators
   - Generators
   - Advanced features

### Week 7+: Practice
10. **Module 10: Projects**
   - Build real applications
   - Apply what you learned
   - Expand your portfolio

## Daily Routine

### 30-Minute Sessions
- **10 min**: Read theory
- **15 min**: Run and study examples
- **5 min**: Try 1-2 exercises

### 1-Hour Sessions
- **15 min**: Read theory thoroughly
- **20 min**: Study all examples
- **20 min**: Complete exercises
- **5 min**: Review solutions

### 2-Hour Sessions
- **20 min**: Read and take notes
- **30 min**: Study examples, experiment
- **50 min**: Complete all exercises
- **20 min**: Review, document learnings

## Tips for Success

### 1. Type, Don't Copy-Paste
- Typing code builds muscle memory
- You'll catch mistakes and learn from them

### 2. Experiment
```python
# Don't just run examples, modify them!
# Original:
name = "Alice"
print(f"Hello, {name}")

# Try changing:
name = "Your Name"  # What happens?
print(f"Hi, {name}!")  # Different greeting?
```

### 3. Use the Python Interactive Shell
```bash
python3
>>> 2 + 2
4
>>> name = "Python"
>>> print(name)
Python
>>> exit()
```

### 4. Read Error Messages
Errors are your friends! They tell you what's wrong:
```
Traceback (most recent call last):
  File "test.py", line 5, in <module>
    print(age)
NameError: name 'age' is not defined
```
This tells you: variable 'age' doesn't exist on line 5

### 5. Practice Daily
- Even 20 minutes daily beats 3 hours once a week
- Consistency builds understanding

### 6. Build Things
- After every module, build a mini-project
- Apply what you learned
- Make it your own

## Tools You'll Need

### Text Editor / IDE
Choose one:
- **VS Code** (Recommended for beginners)
- **PyCharm** (Full-featured IDE)
- **Sublime Text** (Lightweight)
- **Vim/Nano** (Terminal-based)

### Python Interactive Environment
```bash
# Standard Python REPL
python3

# IPython (enhanced, install with: pip3 install ipython)
ipython
```

## Common Issues and Solutions

### Issue: "python: command not found"
**Solution**: Use `python3` instead of `python`

### Issue: Permission denied
**Solution**: 
```bash
chmod +x script.py
```

### Issue: Module not found
**Solution**: Install with pip:
```bash
pip3 install <module-name>
```

### Issue: Syntax error
**Solution**: 
- Check for missing colons `:`
- Check indentation (Python uses spaces/tabs)
- Verify matching quotes and parentheses

## Python Style Guide (PEP 8)

Follow these conventions:

```python
# Good variable names (lowercase with underscores)
user_name = "Alice"
total_price = 99.99

# Bad variable names
userName = "Alice"    # camelCase (not Python style)
TOTALPRICE = 99.99    # ALL CAPS (reserved for constants)

# Good function names
def calculate_total():
    pass

# Constants (all uppercase)
MAX_SIZE = 100
PI = 3.14159

# Indentation: 4 spaces (not tabs)
def greet(name):
    if name:
        print(f"Hello, {name}")
```

## Getting Help

### Built-in Help
```python
help(print)
help(str)
dir(str)  # See all methods
```

### Documentation
- [Python Official Docs](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 Style Guide](https://pep8.org/)

### Communities
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python)
- [r/learnpython](https://reddit.com/r/learnpython)
- [Python Discord](https://discord.gg/python)

## Your First Week Challenge

Complete these tasks in your first week:

- [ ] Install Python and verify version
- [ ] Write and run "Hello, World!"
- [ ] Complete Module 01 exercises
- [ ] Write a simple calculator
- [ ] Create a number guessing game
- [ ] Ask for help on a forum (practice asking good questions!)

## Remember

> "The only way to learn a new programming language is by writing programs in it."
> — Dennis Ritchie

- **Everyone starts as a beginner**
- **Mistakes are part of learning**
- **Progress > Perfection**
- **Build things that interest you**

## Ready?

Start with Module 01:
```bash
cd 01_Basics
cat README.md
python3 examples.py
```

Happy coding! You've got this!
