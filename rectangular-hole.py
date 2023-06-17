# Objective: Calculate the volume of a rectangular hole within a given rectangular block, where the wall thickness is consistent on all sides

# Ask user input
l = int(input("Please enter the length of the rectangular block: "))
w = int(input("Please enter the width of the rectangular block: "))
h = int(input("Please enter the height of the rectangular block: "))
t = int(input("Please enter the consistent thickness around the hole: "))

# Find length and width of hole
sL = l - (t * 2)
sW = w - (t * 2)

# Find volume
v = sL * sW * (h - t)

# Display volume
print("The volume of the hole is", v, "units cubed.")