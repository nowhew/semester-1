# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file

file_name = input("input file: ")

# open the file

file = open(file_name, "r")
out_file = open(file_name+"_out.csv", "w")
# read in the data, and for each student calculate their average grade and classification

#header
file.readline()

for line in file:
    line = line.strip()
    cols = line.split(",")
    id = cols[0]

    num_modules = 0
    total = 0

    for col in cols[1:]:
        if not col.isnumeric():
            continue
        total += int(col)
        num_modules += 1

    mean = total / num_modules
    grade = ""
    if mean >= 70:
        grade = "1"
    elif mean >= 60:
        grade = "2:1"
    elif mean >= 50:
        grade = "2:2"
    elif mean >= 40:
        grade = "3"
    else:
        grade = "3"

    out_file.write(f"{id},{mean:.2f},{grade}\n")

# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder