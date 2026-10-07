# Fill out the code to make a very simple calculator

a, b, = 0, 0
try:
    # ask the user to enter number1:
    a = int(input("enter a: "))
# ask the user to enter number 2:
    b = int(input("enter b: "))
except:
    print("invalid input")

# calculate the result of adding those numbers together

c = a + b

# print out the answer

print(c)