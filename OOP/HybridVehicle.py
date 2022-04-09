# # Hybrid Vehicle
# ``````````````````

from Vehicle import Vehicle


class HybridVehicle(Vehicle):
    # attributes
    engineType = "hybrid"
    batteryKWH = 0.0

    # constructor
    def __init__(self, attribs, battery):
        super().__init__(attribs)
        self.batteryKWH = battery

    # methods
    def getVehicleStatus(self):
        vehicleStatus = {}
        vehicleStatus["VIN"] = self.VIN
        vehicleStatus["engine"] = self.engineType
        vehicleStatus["batteryKWH"] = self.batteryKWH
        vehicleStatus["wheels"] = self.numWheels
        vehicleStatus["doors"] = self.numDoors
        vehicleStatus["seats"] = self.numSeats
        vehicleStatus["isRunning"] = self.isRunning
        vehicleStatus["speed"] = self.speed
        vehicleStatus["brakePressure"] = self.brakePressure
        vehicleStatus["isTurning"] = self.isTurning
        vehicleStatus["turnDirection"] = self.turnDirection
        return vehicleStatus
