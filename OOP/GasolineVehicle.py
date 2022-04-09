# # Gasoline Vehicle
# ``````````````````

from Vehicle import Vehicle


class GasolineVehicle(Vehicle):
    # attributes
    engineType = "gasoline"

    # constructor
    def __init__(self, attribs):
        super().__init__(attribs)

    # methods
    def getVehicleStatus(self):
        vehicleStatus = {}
        vehicleStatus["VIN"] = self.VIN
        vehicleStatus["engine"] = self.engineType
        vehicleStatus["wheels"] = self.numWheels
        vehicleStatus["doors"] = self.numDoors
        vehicleStatus["seats"] = self.numSeats
        vehicleStatus["isRunning"] = self.isRunning
        vehicleStatus["speed"] = self.speed
        vehicleStatus["brakePressure"] = self.brakePressure
        vehicleStatus["isTurning"] = self.isTurning
        vehicleStatus["turnDirection"] = self.turnDirection
        return vehicleStatus
