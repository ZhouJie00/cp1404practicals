from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, reliability, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel, reliability)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Calculate and return the price for the SilverServiceTaxi trip."""
        return super().get_fare() + self.flagfall

# Example test code for SilverServiceTaxi
if __name__ == "__main__":
    fancy_taxi = SilverServiceTaxi("Hummer", 200, 100, 2)
    fancy_taxi.drive(18)
    print(f"Total fare for 18 km trip: ${fancy_taxi.get_fare():.2f}")  # Expected: $48.78