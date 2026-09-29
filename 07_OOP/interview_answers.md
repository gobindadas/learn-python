# Object-Oriented Programming - Interview Answers

## Level: Normal (1-5)

### Answer 1: Class vs Instance Attributes
```python
class Dog:
    species = "Canis familiaris"  # Class attribute
    
    def __init__(self, name):
        self.name = name  # Instance attribute

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.species)  # Canis familiaris (shared)
print(dog1.name)     # Buddy (unique)
print(dog2.name)     # Max (unique)

Dog.species = "Modified"
print(dog1.species)  # Modified (affects all)
```

### Answer 2: `__init__` vs `__new__`
```python
class MyClass:
    def __new__(cls, *args, **kwargs):
        """Creates and returns instance"""
        print("__new__ called")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, value):
        """Initializes instance"""
        print("__init__ called")
        self.value = value

# __new__ is called first, then __init__
obj = MyClass(42)
```

### Answer 3: Inheritance
```python
# Single inheritance
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

# Multiple inheritance
class Flyable:
    def fly(self):
        return "Flying"

class Swimmable:
    def swim(self):
        return "Swimming"

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return "Quack!"
```

### Answer 4: Method Types
```python
class MyClass:
    class_var = 0
    
    def instance_method(self):
        """Has access to instance (self)"""
        return self
    
    @classmethod
    def class_method(cls):
        """Has access to class (cls)"""
        return cls
    
    @staticmethod
    def static_method():
        """No access to instance or class"""
        return "static"
```

## Level: Medium (6-10)

### Answer 6: Property Decorator
```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter with validation"""
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value
    
    @celsius.deleter
    def celsius(self):
        """Deleter"""
        del self._celsius

t = Temperature()
t.celsius = 25  # Uses setter
print(t.celsius)  # Uses getter
```

### Answer 8: Abstract Base Classes
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# shape = Shape()  # TypeError: Can't instantiate abstract class
rect = Rectangle(5, 10)  # OK
```

## Level: Hard (11-15)

### Answer 11: Metaclasses
```python
class SingletonMeta(type):
    """Metaclass for Singleton pattern"""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        print("Database initialized")

db1 = Database()  # Prints: Database initialized
db2 = Database()  # No print, returns same instance
print(db1 is db2)  # True
```

### Answer 12: Descriptor Protocol
```python
class Validator:
    """Descriptor for validation"""
    
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} below minimum")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} above maximum")
        instance.__dict__[self.name] = value

class Person:
    age = Validator(min_value=0, max_value=150)
    
    def __init__(self, age):
        self.age = age

p = Person(25)
# p.age = -5  # ValueError
```

### Answer 13: Singleton Pattern
```python
# Method 1: Using metaclass (see Answer 11)

# Method 2: Using decorator
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    pass

# Method 3: Using __new__
class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```
