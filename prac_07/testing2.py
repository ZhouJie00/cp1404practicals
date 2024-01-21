class Car:
    # Assuming Car is a base class with its own __init__ method
    def __init__(self, make, model):
        self.make = make
        self.model = model
    # ... other Car methods ...

class Taxi(Car):
    # Class variable (acting as a constant) that will be shared by all instances of Taxi
    PRICE_PER_KM = 1.23  # Naming the constant in uppercase to follow convention

    def __init__(self, name, fuel):
        super().__init__(name, fuel)  # Calling the __init__ of the Car class
        # ... other Taxi-specific initializations ...

    # ... other Taxi methods ...

# Example usage:
# Creating instances of Taxi
taxi1 = Taxi('Toyota Prius', 'hybrid')
taxi2 = Taxi('Ford Transit', 'diesel')

# Accessing the class variable
print(Taxi.PRICE_PER_KM)  # Outputs: 1.23

# If the price per km needs to be updated, you update the class variable like this:
Taxi.PRICE_PER_KM *= 1.1

# Now all instances of Taxi will reflect the new price per km
print(Taxi.PRICE_PER_KM)  # 1.23

taxi1.PRICE_PER_KM = 5 # still 1.23


print(taxi2.PRICE_PER_KM)