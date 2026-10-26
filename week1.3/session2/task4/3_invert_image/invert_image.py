# Week 1.3, Session 2: Invert PGM image

# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except

# Create inverted image
# the formula: invert_pixel_value = max_gray - original_pixel_value

in_path = input("path: ")
in_file = open(in_path)

out_path = in_path[:in_path.find(".pgm")] + "_inverted.pgm"
out_file = open(out_path, "w")

pixels = []

#magic string
in_file.readline()

dimensions = [int(i) for i in in_file.readline().split(" ")]
w, h = dimensions[0], dimensions[1]

max_val = int(in_file.readline().strip())

for line in in_file:
    pixels.extend([int(p) for p in line.strip().split(' ') if p.isnumeric()])

out_file.write("P2\n")
out_file.write(f"{w}\n")
out_file.write(f"{h}\n")
out_file.write(f"{max_val}\n")

for y in range(h):
    for x in range(w):
        out_file.write(f"{max_val - pixels[y * w + x]} ")
    out_file.write("\n")

in_file.close()
out_file.close()
# write the inverted pgm image to a new file.
# Remember to include:
# - the string `P2`
# - the width and height dimensions
# - maximum gray value
# - you could convert numbers in a list to strings and join them with spaces
#   for example line = [255, 255, 0, 255, 255]
#   string_line = " ".join(str(item) for item in line)
#   # output: string_line = "255 255 0 255 255"