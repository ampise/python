import os
os.system("clear")

num = int(input("Enter a number: "))
addValue = 0
while num >= 0:
    addValue = addValue + num
    num -= 1         # num = num - 1
    # print(">> ans = {:.0f} \t num = {:.0f}".format(addValue, num))
print("Sum of all numbers between 1 and number you entered is {:.0f}".format(addValue))
