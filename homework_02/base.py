from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):

    def __init__(self, weight=200, fuel=50, fuel_consumption=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance):
        self.fuel -= self.fuel_consumption * distance
        if self.fuel >= 0:
            return self.fuel
        else:
            raise exceptions.NotEnoughFuel
