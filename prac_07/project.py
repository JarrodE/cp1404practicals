"""CP1404 Practical Week 07
Project Class for Project management program
"""

import datetime


class Project:
    """Represent a project object."""

    def __int__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a project object."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return a string representation of the Project object."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority},"
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare two projects based on their priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Check if the project is complete"""
        return self.completion_percentage == 100
