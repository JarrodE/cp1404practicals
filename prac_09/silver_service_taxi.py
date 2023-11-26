from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a Silver Service Taxi."""
    flagfall = 450  # Task 2

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness  # Task 1

    def get_fare(self):
        """Calculate and return the total fare."""
        return super().get.fare() + self.flagfall  # Task 3

    def __str__(self):  # Task 4
        """Return a string representation of SilverServiceTaci."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"