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
    new_guitars = get_user_guitars()
    guitars.extend(new_guitars)
    save_guitars(guitars, FILENAME)
    print(f"\nGuitars saved to {FILENAME}")


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


def get_user_guitars():
    """Prompt user for details of new guitars and return a list of Guitar objects."""
    guitars = []
    print("\nAdd new Guitar:")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ")
    return guitars


def save_guitars(guitars, filename):
    """Save list of guitars to file."""
    with open(filename, "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost:.2f}\n")


if __name__ == "__main__":
    main()
