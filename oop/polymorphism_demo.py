# polymorphism_demo.py

import math

# Base class
class Shape:
    def area(self):
        """Method to be overridden by derived classes."""
        raise NotImplementedError("Subclasses must implement this method.")


# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.length * self.width


# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2
