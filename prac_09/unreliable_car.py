from car import Car
import random


class UnreliableCar(Car):
    """A car that has a chance of not working."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if a random number is less than the reliability."""
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
