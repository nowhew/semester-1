# Week 1.5, Session 2: Task 5

# Write a program here to create a Dataset containing data
# from a file named by the user

# Your program should display dataset size, mean and median,
# followed by the individual values (using a for loop)

from data import Dataset

filepath = input("input file: ")
dataset = Dataset(filepath)
print(f"dataset length: {len(dataset)}")
print(f"dataset mean: {dataset.mean()}")
print(f"dataset median: {dataset.median()}")

for e in dataset:
    print(e)