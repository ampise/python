# -----------------------------------------------------------------------------------------------
# Print odd and even numbers between 0 and a range provided by the user
# -----------------------------------------------------------------------------------------------

number = input("Enter a number: ")

for x in range(number + 1):
    oddeven = (x % 2)
    if oddeven == 0:
        # True block
        print(str(x) + " is even")
    else:
        # False block
        print(str(x) + " is odd")
