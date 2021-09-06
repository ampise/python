# Establish a list with 5 different numbers (can be integers or have decimals and be as big or as small as you want). 
# Add up all the numbers and find and print the average of all the numbers in the list

import os
os.system("clear")

# Define array with 5 numbers (Store in "list")
    # Loop for places in array (For loop with range)
        # Add numbers and store in variable
# Divide variable by length of array (Use len)

list = [160, 35, 49, 72, 83]
# Add values in array
add = sum(list)
# Find average
average = add / len(list)
# Print average to user
print("The average of the numbers is", average)