# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

import geometry

p1 = geometry.Point(0, 0)
c1 = geometry.Cirlce(p1, 5)

print(f"c1 area: {c1.area()}")
print(f"c1 perimeter: {c1.perimeter()}")