"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

monthly_savings = 0

try:
    monthly_savings = int(input("Enter your monthly savings amount: "))
    annual_savings = monthly_savings * 12.0
    print(f"You will save £{annual_savings} every year.")

    intrest = annual_savings * 0.008
    total_savings = annual_savings + intrest
    print(f"With intrest, you will save £{total_savings:.2f} per year.")
except:
    print("Invalid amount")
    exit()