# Modules and Packages - Interview Questions

## Level: Normal (1-5)

### Question 1: Import Statements
What's the difference between these import statements?
```python
import math
from math import sqrt
from math import *
import math as m
```

### Question 2: Module Search Path
When you `import mymodule`, where does Python look for it? Explain the search order.

### Question 3: `__name__` Variable
What does `if __name__ == "__main__":` do and why is it important?

### Question 4: Package Structure
What files are required to make a directory a Python package? What changed in Python 3.3+?

### Question 5: Relative vs Absolute Imports
Explain the difference and when to use each:
```python
from . import module
from .. import module
from package import module
```

## Level: Medium (6-10)

### Question 6: Circular Imports
How do circular imports occur and how do you fix them?
```python
# module_a.py
from module_b import func_b

# module_b.py
from module_a import func_a
```

### Question 7: `sys.path` Manipulation
How and when should you modify `sys.path`? What are the risks?

### Question 8: Lazy Imports
What are lazy imports? Implement a lazy import mechanism.

### Question 9: `__init__.py` Usage
What can you put in `__init__.py`? Provide practical examples of its uses.

### Question 10: Import Hooks
What are import hooks? How would you implement a custom importer?

## Level: Hard (11-15)

### Question 11: Module Reloading
How do you reload a module? What are the pitfalls of using `importlib.reload()`?

### Question 12: Package Distribution
How do you structure a Python package for distribution? What files are needed (setup.py, pyproject.toml, etc.)?

### Question 13: Namespace Packages
What are namespace packages (PEP 420)? When would you use them?

### Question 14: Import Performance
How can imports affect application startup time? What strategies can optimize import performance?

### Question 15: Module Singleton Pattern
Modules are singletons in Python. Explain this concept and demonstrate practical implications.

## Bonus Challenge

### Question 16: Plugin System
Design a plugin system using Python's import mechanism that:
- Automatically discovers plugins in a directory
- Loads them dynamically
- Provides a registry for plugin management

### Question 17: Import Security
What security risks exist with Python imports? How can you mitigate them?

### Question 18: Conditional Imports
When and how should you use conditional imports? Provide scenarios where they're beneficial.
