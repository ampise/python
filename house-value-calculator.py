import os
os.system("clear")

# Input assessed value of home
originalValue = float(input("What is the assessed value of the house?: "))
# Calculate tax on home
newValue = (originalValue * 0.0645) + originalValue

print("The assessed value of a ${:.2f} home at the current tax rate (6.45%) would be ${:.2f}.".format(originalValue, newValue))