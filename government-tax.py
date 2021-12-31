import os
os.system("clear")

UNTIL_AGE = 22
INCOME = 1000
total = 0

def calculateTax(age, income):
    taxPercent = (age / 2) / 100
    tax = taxPercent * income
    print(" >> age = ", age, " taxRate = ", taxPercent, " tax = ", tax)
    return tax

for age in range(18, 23):
    total = total + calculateTax(age, INCOME)

print(total)