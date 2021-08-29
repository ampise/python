import os
os.system("clear")

name = input("Please enter employee name: ")

hoursWorked = float(input("How many hours did you work today?: "))
hourlyRate = float(input("What is your hourly rate?: "))
# Calculating payment for employee
wage = hoursWorked * hourlyRate

print(name + " worked {:.2f} hours at a rate of ${:.2f} and earned ${:.2f}.".format(hoursWorked, hourlyRate, wage))