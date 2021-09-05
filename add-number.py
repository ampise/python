import os
os.system("clear")

# Ask for a number
num = int(input("Enter a number: "))
addValue = 0
# While loop for while number entered by user is greater than or equal
while num >= 0:
    addValue = addValue + num
    num -= 1         # num = num - 1
    # print(">> ans = {:.0f} \t num = {:.0f}".format(addValue, num))
print("Sum of all numbers between 1 and number you entered is {:.0f}".format(addValue))
