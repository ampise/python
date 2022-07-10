import os
os.system("clear")

def motorbike():
    motorbikeSpeed = 60
    time = distance * motorbikeSpeed
    print("The time it will take to travel a distance of", distance, "with a speed of 60: ", time)

def van():
    vanSpeed = 110
    time = distance * vanSpeed
    print("The time it will take to travel a distance of", distance, "with a speed of 110: ", time)
def sedan():
    sedanSpeed = 160
    time = distance * sedanSpeed
    print("The time it will take to travel a distance of", distance, "with a speed of 160: ", time)

def getVehicle(car):
    vehicleType = {
        "1": motorbike,
        "2": van,
        "3": sedan,
    }
    transportation = vehicleType.get(car)
    transportation()
    print("\n")

# Main entry
print("What is your car type?")
print("1. Motorbike")
print("2. Van")
print("3. Sedan")
car = input("(Ex. Enter 1 for Motorbike) >> ")
distance = int(input("What is the distance you have to travel?: "))
getVehicle(car)