import os
os.system("clear")

celsius = float(input("Please enter a celsius value that you wish to convert to fahrenheit: "))
# Convert celsius to fahrenheit using formula
fahrenheit = (celsius * 1.8) + 32

print("Your new value in fahrenheit is " + str(fahrenheit))