# The following general format can me used with some modifications to print out almost any table of data

#for row in range(?):
    # print(start of each row)
    # for col in range(?):
        # print(main row of data)
    # print(end of each row)

# Outside of loop controls the number of rows
# Inside controls number of columns

# First print statement is optional. Include if there is special value to print at the start of each row
# Middle print statement does most of the work: Print the main data in each row
# Last print statement is required and can either print a value at the end of each row or just a blank line

# Only specifies how many rows wanted
for col in range(2, 11, 2):
    # Nothing at start, so removed optional print
    # Data changes in the column, detail is needed
    for row in range (4):
        print(col, end = " ")
    # Nothing special at the end, so empty print
    print()

# If the row and col for loops are switched, then the rows will all have the same values
# It will print the following:

# 2 2 2 2
# 4 4 4 4
# 6 6 6 6
# 8 8 8 8
# 10 10 10 10

# Exercises in making tables:

for row in range(4):
    print("*", end = " ")
    for col in range (2, 11, 2):
        print(col, end = " ")
    # Note: No end= here!
    print("$")

for row in range(4):
    for col in range(0, 13, 2):
        if col == 0:
            print("*", end = " ")
        elif col == 12:
            print("$")
        else:
            print(col, end = " ")
    print()

for col in range(2):
    for row in range (3, 3, 13):
        print(col, end = " ")
    print()

for row in range(3):
    for col in range(1, 4):
        print(col, end = " ")
    print()

for row in range(3):
    for col in range (2, 9):
        if col == 5:
            print("*", end = " ")
        else:
            print(col, end = " ")
    print()