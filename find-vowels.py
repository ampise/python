# Have the user input a string of text and count all of the vowels in the string that was inputted. 
# This should work for all vowels, even if it is uppercase or lowercase. 
# Finally, print the statement “There are _ vowels in the string” with the blank being the number of vowels in the string.

import os
os.system("clear")

# Ask input for string of text from user
    # Make loop to count vowels in text
# Print vowel count

count = 0
text = input("Please enter a string of text: ")
# Find vowels in text
for vowel in text:
    if vowel in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]:
        # Increase count by one each time found one
        count += 1
print("There are", count, "vowels in the string.")
