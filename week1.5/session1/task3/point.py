# Week 1.5, Session 1: Task 3

import math

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



# Finally, add code here to demonstrate use of Point
p1 = Point(10, 20)
p2 = Point(-5, 15)

print(f"length of p1: {p1.distance()}")
print(f"length of p2: {p2.distance()}")

print(f"distance between points: {p1.distance_to(p2)}")