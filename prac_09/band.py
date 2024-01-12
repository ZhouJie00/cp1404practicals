class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add_musician(self, musician):
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            print(musician.play())

# Example usage:
if __name__ == '__main__':
    from guitar import Guitar  # Assuming Guitar class is defined elsewhere

    # Create band
    extreme = Band("Extreme")


    Banding = Band("Nuno Bettencourt")
    Banding.add_musician(Guitar("Washburn N4", 1990, 2499.95))
    Banding.add_musician(Guitar("Takamine acoustic", 1986, 1200.00))

    gary = Band("Gary Cherone")
    pat = Band("Pat Badger")
    pat.add_musician(Guitar("Mouradian CS-74 Bass", 2009, 1500.00))

    kevin = Band("Kevin Figueiredo")

    print(Banding)
    print(Banding.play())

    # Simulate band play
    print(extreme)
    extreme.play()