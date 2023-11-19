class Band:
    """Band class to manage a collection of musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the band and its musicians."""
        musician_details = ', '.join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_details})"

    def play(self):
        """Simulate each musician in the band playing their instrument."""
        return '\n'.join(musician.play() for musician in self.musicians)

