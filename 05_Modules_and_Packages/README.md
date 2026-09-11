# Module 05: Modules and Packages

Learn how to organize code into reusable modules and use Python's vast ecosystem of packages!

## Topics to Cover

1. **What are Modules?**
   - Understanding modules
   - Importing modules
   - Using built-in modules

2. **Creating Your Own Modules**
   - Writing module files
   - Importing your modules
   - `if __name__ == "__main__"`

3. **Common Built-in Modules**
   - `math` - Mathematical functions
   - `random` - Random number generation
   - `datetime` - Date and time
   - `os` - Operating system interface
   - `json` - JSON handling

4. **Packages and pip**
   - What are packages?
   - Installing packages with pip
   - Popular packages to explore

5. **Import Variations**
   - `import module`
   - `from module import function`
   - `import module as alias`
   - `from module import *` (and why to avoid it)

## Key Concepts

```python
# Importing entire module
import math
result = math.sqrt(16)

# Importing specific function
from random import randint
number = randint(1, 10)

# Using alias
import datetime as dt
now = dt.datetime.now()

# Creating your own module
# In mymodule.py:
# def greet(name):
#     return f"Hello, {name}!"

# In main.py:
# import mymodule
# mymodule.greet("Alice")
```

## Practice Ideas

1. Create a `calculator.py` module with math functions
2. Create a `utils.py` module with helper functions
3. Explore `random` module to create a dice game
4. Use `datetime` to create an age calculator
5. Use `json` to save and load data

## Coming Soon

Detailed examples and exercises will be added here. For now:
- Explore Python's [standard library documentation](https://docs.python.org/3/library/)
- Practice importing and using built-in modules
- Try creating your own simple modules

## Next Module

Continue to [Module 06: File Handling](../06_File_Handling/) to learn reading and writing files!
