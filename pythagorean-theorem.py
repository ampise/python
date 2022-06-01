from math import sqrt

# Find the hypotenuse of a triangle in a given scenario.

height = float(input("Provide the height: "))
base = float(input("Provide the base length: "))

hypotenuse = sqrt((height ** 2) + (base ** 2))

# Using the hypotenuse as the distance, ask user for speed to calculate time (hours for MPH)
# S = D/T  |  T = D/S  |  D = ST

speed = 7000    # Meters per second
time = hypotenuse / speed


print()