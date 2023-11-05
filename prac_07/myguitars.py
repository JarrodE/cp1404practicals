"""CP1404 Week 07 Practicals
My guitars program
Estimate: 30
Start: 1610
Finish:
"""

import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Load and display guitars and sorted by year."""
    guitars = load_guitars(FILENAME)
    print("Guitars:")
    for guitar in guitars:
        print(guitar)
    guitars.sort()
    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)


def load_guitars(filename):
    """Load guitars from file amd return a list of guitar objects."""
    guitars = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


if __name__ == "__main__":
    main()
