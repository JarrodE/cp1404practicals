"""CP1404 Practical - Programming Language
Estimated: 30 minutes
Current time: 16:54
Finish time:
"""


class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """ Initialise ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return true if the programming language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Print python string"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
