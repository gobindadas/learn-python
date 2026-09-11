# Module 07: Object-Oriented Programming (OOP)

Master OOP concepts to write more organized, reusable, and maintainable code!

## Topics to Cover

1. **Classes and Objects**
   - What are classes and objects?
   - Creating classes
   - The `__init__` method
   - Instance variables vs class variables
   - The `self` parameter

2. **Methods**
   - Instance methods
   - Class methods (`@classmethod`)
   - Static methods (`@staticmethod`)
   - Magic methods (`__str__`, `__repr__`)

3. **Inheritance**
   - Parent and child classes
   - The `super()` function
   - Method overriding
   - Multiple inheritance

4. **Encapsulation**
   - Public vs private attributes
   - Name mangling with `__`
   - Property decorators (`@property`)
   - Getters and setters

5. **Polymorphism**
   - Method overriding
   - Duck typing
   - Interface concepts

## Key Concepts

```python
# Basic class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"

# Creating objects
my_dog = Dog("Buddy", 3)
print(my_dog.bark())

# Inheritance
class Puppy(Dog):
    def __init__(self, name, age, toy):
        super().__init__(name, age)
        self.toy = toy
    
    def play(self):
        return f"{self.name} plays with {self.toy}"

puppy = Puppy("Max", 1, "ball")
print(puppy.bark())  # Inherited
print(puppy.play())  # New method
```

## Practice Ideas

1. Create a `BankAccount` class with deposit/withdraw methods
2. Build a `Student` class with grades and GPA calculation
3. Create a `Vehicle` parent class with `Car` and `Bike` children
4. Design a simple game with `Player` and `Enemy` classes
5. Build a `Library` system with `Book` and `Member` classes

## OOP Principles (SOLID)

- **S**ingle Responsibility
- **O**pen/Closed
- **L**iskov Substitution
- **I**nterface Segregation
- **D**ependency Inversion

## Coming Soon

Detailed examples and exercises. For now:
- Think in terms of objects and their behaviors
- Practice creating simple classes
- Explore inheritance relationships

## Next Module

Continue to [Module 08: Error Handling](../08_Error_Handling/) to learn about exceptions!
