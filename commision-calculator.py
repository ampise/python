import os
os.system("clear")

dollars = int(input("Enter the original price: "))
percentage = float(input("Enter percentage amount in decimal: "))
commision = percentage * dollars

print(commision)