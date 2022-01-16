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
def changeDenomination(change):
    change = change * 100
    coins = [25, 10, 5, 1]
    coinCounter = [0, 0, 0, 0]
    for i, coin in enumerate(coins):
        while change >= coin:
            change = change - coin
            coinCounter[i] = coinCounter[i] + 1
    # printing results
    verifiedAmount = 0
    for i, count in enumerate(coinCounter):
        verifiedAmount = verifiedAmount + (count * coins[i])
        print(count, " x ", coins[i] , " cent coins = ", count * coins[i])
    print("Change returned = ", verifiedAmount / 100)


billAmount = generateBill()
print("Bill amount = ", billAmount)

changeAmount = calculateChange(billAmount)
print("Change from 50.00 = ", changeAmount)

changeDenomination(changeAmount)

# print("test ", billAmount + changeAmount)
