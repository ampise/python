import os
os.system("clear")

class Vehicle():
    def __init__(self, bodyStyle):
        self.bodyStyle = bodyStyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed


class Car(Vehicle):
    def __init__(self, engineType):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.engineType = engineType

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engineType, "car at ", self.speed)


class Motorcycle(Vehicle):
    def __init__(self, engineType, sidecar):
        super().__init__("Motorcycle")
        if(sidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.engineType = engineType

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engineType, "motorcycle at ", self.speed)


car1 = Car("gas")
mc1 = Motorcycle("gas", True)

# print(car1.wheels, car1.engienType, car1.bodyStyle)
# print(mc1.wheels, mc1.engineType, mc1.bodyStyle)

car1.drive(10)
mc1.drive(10)