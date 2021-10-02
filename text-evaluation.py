import os
os.system("clear")

s = input("Please enter a string: ")
length = print("The length of the string is: ", len(s))
first = print("The first letter of the string is: ", s[0])
last = print("The last letter of the string is: ", s[len(s)-1])

# Find if specific letter(s) are in string

if (s.find('ch') != -1):
    print ("Contains \"ch\" at position " + str(s.find('ch')))
else:
    print ("Doesn't contain \"ch\".")

# Replace

change = print("Replace \"e\" with \"y\": ", s.replace("e", "y"))

print("Every 3rd letter: ")
for p in range(0, len(s) + 1, 3):
    print(s[p], end = " ")

print("\nReverse: ")
for p in range(len(s) - 1, -1, -1):
    print(s[p], end = " ")