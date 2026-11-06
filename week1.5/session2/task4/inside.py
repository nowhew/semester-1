# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class

import geometry

circle = geometry.Circle(5, geometry.Point(2, 2))
point1 = geometry.Point(2, 2)
point2 = geometry.Point(7, 10)

print(f"point1 {"is" if point1 in circle else "isnt"} in the circle")
print(f"point2 {"is" if point2 in circle else "isnt"} in the circle")