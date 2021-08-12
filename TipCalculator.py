billAmount = float(input("\nEnter bill amount: $"))
tipPercent = float(input("Enter tip % you would like to add: "))

tipAmount = billAmount * (tipPercent / 100)
finalAmount = billAmount + tipAmount

print("\n")
print("Bill Amount: \t${:0,.2f}".format(billAmount))
print("Tip ({:0,.2f}".format(tipPercent)+"%): \t${:0,.2f}".format(tipAmount))
print("-------------------------------------------------------------")
print("Final Amount: \t${:0,.2f}".format(finalAmount))
print("\n")
