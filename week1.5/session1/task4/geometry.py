# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!

class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x : float, y : float):
        self.x = x
        self.y = y

    # Add constructor here

    # Add distance() method here

    def distance(self) -> float:
        return math.sqrt(self.x*self.x+self.y*self.y)

    # Add distance_to() method here

    def distance_to(self, other : Point) -> float:
        dif_x = self.x - other.x
        dif_y = self.y - other.y
        return math.sqrt(dif_x*dif_x + dif_y*dif_y)
    # (This will need a parameter representing another point)

class Cirlce:
    def __init__(self, centre : Point, radius : float):
        self.centre = centre
        self.radius - radius

    def area(self) -> float:
        return math.pi * self.radius*self.radius
    
    def perimeter(self) -> float:
        return math.pi*2*self.radius