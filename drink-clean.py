# This program helps education people about water insecurity by asking them questions to see what they already know.

# Question 1

print("Q: People need 3 liters of drinking water every day to survive.\n")
answer1 = input("Enter T for True or F for False: ")
if answer1 == "T":
  print("Correct!\n")
else:
  print("This is true. People need 3 liters of drinking water every day.\n")


# Question 2

print("Q: 10% of the global population lack access to safe drinking water.\n")
answer2 = input("Enter T for True or F for False: ")
if answer2 == "F":
  print("Correct! 33% of the global population lacks access to safe drinking water.\n")
else:
  print("Sorry, the correct answer was False. It is 33%, not 10%.\n")


# Question 3

print("Q: 72,000 children under the age of five die every year due to contaminated drinking water and poor sanitation.\n")
answer3 = input("Enter T for True or F for False: ")
if answer3 == "T":
  print("Correct! This is a very sad fact.\n")
else:
  print("Unfortunately, the correct answer was True. Sadly, this affects 72,000 children every year.\n")
  
  
print("\nNow that you know some more about these sad facts, see how our invention can potentially help!\n")





# This program performs calculations to show how DrinkClean can help.

# Prompt user to enter the population

population = input("\nEnter the population of the sample country: ")
population = int(population)
needs = (int)(population * 3)
print("\nThis country needs " + str(needs) + " liters of clean drinking water every single day.")

# Promt user to enter how much water the country can provide

provided = (int)(input("\nEnter the amount of water that the country can already provide: "))

# Calculate and print results

print("\nThe country will need to provide this many more liters of clean drinking water:")
print(needs - provided)

# Prompt user to enter how many liters can be cleaned

clean = input("\nHow many liters can one DrinkClean device purify?: ")
clean = int(clean)

# Calculate how many DrinkClean devices

stillNeeds = ((needs - provided) / clean)
print("\nThe country needs to buy this many DrinkClean devices:")
print(stillNeeds)

# Calculate total cost

cost = input("\nWhat is the cost for each DrinkClean device?")
cost = int(cost)
totalCost = stillNeeds * cost
print("The cost for this number of DrinkCleans would be: ")
print("${:.2f}".format(totalCost))