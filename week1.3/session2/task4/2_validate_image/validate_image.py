# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except

# Read the file content

# Store the width, the height, and the maximum gray value

# For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive

# Check if the widths and heights are the same as specified

in_path = input("path: ")
in_file = open(in_path)

#magic string

try:
#magic string
    in_file.read()
    dimensions = [int(i) for i in in_file.readline().split(" ")]

    w, h = dimensions[0], dimensions[1]
    max_val = int(in_file.readline().strip())

    num_rows = 0
    max_observed_val = 0

    for line in in_file:
        pixels = [int(n) for n in line.strip().split(' ') if n.isnumeric()]
        if len(pixels) != w:
            raise ValueError("Invalid Width") 

        for pixel in pixels:
            if pixel < 0:
                raise ValueError("invalid Pixel Values")

            max_observed_val = max(pixel, max_observed_val)
        
        num_rows += 1

    if max_observed_val > max_val:
        raise ValueError("Invalid Pixel Values")
    if num_rows != h:
        raise ValueError("Invalid Height")
except ValueError as e:
    print(e.args[0])
    exit(0)

print("Valid Image")

in_file.close()

# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value