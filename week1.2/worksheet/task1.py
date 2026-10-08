# Worksheet 1.2: Task 1 Solution
import sys

try:
    mark = int(input("enter mark: "))
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if mark < 0 or mark > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")
grade = "Fail"
if mark > 39:
    grade = "Pass"
if mark > 69:
    grade = "Distinction"

print(f"{mark} is a {grade}")