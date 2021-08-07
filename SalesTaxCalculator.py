#
# Program to calculate Final bill amount
# based on patron's state.
#

states = ["AL", "AK", "AZ", "AR"]
salesTaxRates = [0.04, 0.00, 0.05, 0.06]
locationRate = -1

# Function to get a location and lookup sales tax rate


def getStateRate():
    location = input(
        "Where are you located (enter short state code, e.g. OH for Ohio)? ")
    try:
        return salesTaxRates[states.index(location)]
    except ValueError:
        print("\n!! ERROR !! That state code, " + location + " does not exist.")
        return -1

# Function to calculate final amount


def calculateFinalAmount(locationRate):
    amount = float(input("How much is the bill amount?  "))
    taxValue = amount * locationRate
    finalAmount = amount + taxValue
    print("You final amount after tax (per state tax rate) is " + str(finalAmount))


while locationRate == -1:
    locationRate = getStateRate()

calculateFinalAmount(locationRate)
