# Worksheet 1.2: Task 2 Solution

import sys
from util import read_numbers

numbers = read_numbers()
if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

numbers.sort()

print(f"Minimum: {numbers[0]}")
print(f"Maximum: {numbers[-1]}")
print(f"Mean: {sum(numbers) / len(numbers)}")

if len(numbers) % 2 == 0:
    print(f"Median: {(numbers[len(numbers)//2] + numbers[len(numbers)//2]) / 2}")
else:
    print(f"Median: {numbers[len(numbers)//2]}")