
# Vehicle
# ``````````
class Vehicle:
    # attributes
    VIN = "NONE"
    numWheels = 4
    numDoors = 4
    numSeats = 4
    isRunning = False
    speed = 0
    brakePressure = 0
    isTurning = False
    turnDirection = 0   # -1 (left) | 0 (straight / not turning) | 1 (right)

    # constructor
    def __init__(self, attribs):
        self.VIN = attribs["vin"]
        self.numWheels = attribs["wheels"]
        self.numDoors = attribs["doors"]
        self.numSeats = attribs["seats"]

    # methods
    def start(self):
        self.isRunning = True
        self.speed = 0

    def stop(self):
        if self.speed > 0:
            print("It is dangerous to turn off a running vehicle. Please coome to an hault first.")
        else:
            self.isRunning = False
            self.speed = 0
            self.brakePressure = 0

    def brake(self, pressure):
        self.brakePressure = pressure
        if self.speed >= pressure:
            self.speed = self.speed - pressure
        else:
            self.speed = 0

    def accelerate(self, speed):
        if self.isRunning:
            self.speed = speed
        else:
            print("Vehicle is currently not running")

    def turn(self, direction):  # "left" | "straight" | "right"
        self.isTurning = True
        if direction == "left":
            self.turnDirection = -1
        elif direction == "right":
            self.turnDirection = 1
        else:
            self.turnDirection = 0
            self.isTurning = False

    def getVehicleStatus(self):
        vehicleStatus = {}
        vehicleStatus["VIN"] = self.VIN
        vehicleStatus["wheels"] = self.numWheels
        vehicleStatus["doors"] = self.numDoors
        vehicleStatus["seats"] = self.numSeats
        vehicleStatus["isRunning"] = self.isRunning
        vehicleStatus["speed"] = self.speed
        vehicleStatus["brakePressure"] = self.brakePressure
        vehicleStatus["isTurning"] = self.isTurning
        vehicleStatus["turnDirection"] = self.turnDirection
        return vehicleStatus

