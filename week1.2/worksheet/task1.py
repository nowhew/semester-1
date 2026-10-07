# Worksheet 1.2: Task 1 Solution
import sys

try:
    mark = int(input("enter mark: "))
    if mark < 0 or mark > 100:
        print("Error: Grade must be an integer between 0 and 100")
        sys.exit()

    grade = "Fail"
    if grade > 39:
        grade = "Pass"
    if grade > 69:
        grade = "Distinction"

    print(f"{mark} is {grade}")

except:
    print("Error: non integer input")
    sys.exit(-1)