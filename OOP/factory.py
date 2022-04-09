import os
os.system("clear")

from GasolineVehicle import GasolineVehicle
from HybridVehicle import HybridVehicle

yarisAttributes = {}
yarisAttributes["vin"] = "YARIS123000000"
yarisAttributes["wheels"] = 4
yarisAttributes["doors"] = 4
yarisAttributes["seats"] = 4

tandcAttributes = {}
tandcAttributes["vin"] = "CHRYSLER123000"
tandcAttributes["wheels"] = 4
tandcAttributes["doors"] = 4
tandcAttributes["seats"] = 7

priusAttributes = {}
priusAttributes["vin"] = "PRIUS123000000"
priusAttributes["wheels"] = 4
priusAttributes["doors"] = 4
priusAttributes["seats"] = 5
priusBattery = 2.4

yaris = GasolineVehicle(yarisAttributes)
prius = HybridVehicle(priusAttributes, priusBattery)
chrysler = GasolineVehicle(tandcAttributes)

print(yaris.getVehicleStatus())
print()
print(prius.getVehicleStatus())
print()
print(chrysler.getVehicleStatus())

chrysler.turn("left")
print(chrysler.getVehicleStatus())
chrysler.turn("straight")
print(chrysler.getVehicleStatus())
