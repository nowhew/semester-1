# Worksheet 1.2: Task 2 Solution

import sys

def read_numbers():
    """
    Prompts the user to enter a series of numbers on a single line,
    separated from each other by spaces.

    Returns a list of float values corresponding to the numbers that were
    input by the user.
    """
    line = input("Enter some numbers, separated by spaces: ")
    numbers = [float(item) for item in line.split()]
    return numbers

numbers = read_numbers()
if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

numbers.sort()

print(f"Minimum = {numbers[0]}")
print(f"Maximum = {numbers[-1]}")
print(f"Mean = {sum(numbers) / len(numbers)}")

if len(numbers) % 2 == 0:
    print(f"Median = {(numbers[len(numbers)//2-1] + numbers[len(numbers)//2]) / 2}")
else:
    print(f"Median = {numbers[len(numbers)//2]}")