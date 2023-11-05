"""CP1404 Practical Week 07
Project Class for Project management program
"""

import datetime


class Project:
    """
    Represents a project with attributes for name, start date, priority, cost estimate, and completion percentage.
    """

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """
        Initialise a new Project instance.
        """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __lt__(self, other):
        """Return True if this project's priority is less than another project's priority, False otherwise."""
        return self.priority < other.priority

    def __str__(self):
        """Return a string representation of the project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def is_complete(self):
        """Check if the project is complete"""
        return self.completion_percentage == 100
