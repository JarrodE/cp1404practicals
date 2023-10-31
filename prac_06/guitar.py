"""CP1404 Practical - Guitar
Estimated: 30 minutes
Actual: 27 minutes
Current time: 17:20
Finish time: 17:47
"""


class Guitar:
    """Class to represent Guitar."""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a new Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Calculate the age of the guitar based on the current year."""
        return 2023 - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage based on its age."""
        return self.get_age() >= 50

