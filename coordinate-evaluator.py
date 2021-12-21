import os
os.system("clear")
# Use everything learned so far all into one program.

# Program Prompt:
# Input cell coordinates in duplets.
# Output tells path robot travels to collect all the packages.
# Final goal is to deliver all the packages to the exit.


# Module A: Evalute if entered coordinate is in range (Up to 10 in both (x, y))
def validateInputCoordinates(inputValues):
    arrValues = []
    for c in inputValues.split(" "):
        if int(c) < 9:
            arrValues.append(int(c))
        else:
            print("Value is out of range. Must be between 0 and 9.")
    return arrValues


# --- Main ---
pairs = input("Please enter a few coordinate pairs in which both the axes are less than or equal to 10. \nPlease enter with the specified format x y x y: ")
coords = validateInputCoordinates(pairs)


