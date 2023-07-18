import os, math
os.system("clear")

# User input
x1 = float(input("Please provide the x-coordinate of the first point: "))
y1 = float(input("Please provide the y-coordinate of the first point: "))
x2 = float(input("Please provide the x-coordinate of the second point: "))
y2 = float(input("Please provide the y-coordinate of the second point: "))

# Calculate distance
distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

# Display distance
print("The distance between the two points is", distance)