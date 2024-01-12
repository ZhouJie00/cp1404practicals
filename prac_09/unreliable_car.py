import random
from car import Car


#this is unreliable_car.py

class Taxi(Car):


    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel, reliability)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance based on reliability.

        Only drive if a random number is less than the car's reliability.
        """
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0


