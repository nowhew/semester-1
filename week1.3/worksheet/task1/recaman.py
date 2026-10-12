# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'


# You may wish to use further output for testing purposes while you develop your code

sequence = set([])
last = 0
for n in range(L):
    if n == 0:
        val = 0
    elif last - n > 0 and last-n in sequence:
        val = last-n
    else:
        val = last+n
    
    last = val
    sequence.add(val)

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence