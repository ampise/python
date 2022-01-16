import os, random
os.system("clear")

# generateBill
def generateBill():
    amount = random.randint(4500, 5000)
    return amount / 100

# calculateChange
def calculateChange(bill):
    change = 5000 - (bill * 100)
    return change / 100

# changeDenomination
def changeDenomination(###):
    coins = [25, 10, 5, 1]
    while change > 0:
        for i in coins:
            if (change - i) >= 0:
                change = change - i
            do until change <= 0:
                

# billAmount = generateBill()
# print(billAmount)

# changeAmount = calculateChange(billAmount)
# print(changeAmount)

# print("test ", billAmount + changeAmount)
