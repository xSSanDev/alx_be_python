# polymorphism_demo.py

import math

# Define the base class Shape
class Shape:
    # Method to calculate the area, to be overridden by derived classes
    def area(self):
        raise NotImplementedError("Subclasses must override the area() method")

# Define the derived class Rectangle that inherits from Shape
class Rectangle(Shape):
    # Constructor to initialize the Rectangle instance with length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Override the area method to calculate the rectangle's area
    def area(self):
        return self.length * self.width

# Define the derived class Circle that inherits from Shape
class Circle(Shape):
    # Constructor to initialize the Circle instance with radius
    def __init__(self, radius):
        self.radius = radius

    # Override the area method to calculate the circle's area
    def area(self):
        return math.pi * (self.radius ** 2)