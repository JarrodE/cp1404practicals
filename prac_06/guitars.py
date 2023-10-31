"""CP1404 Practical - Guitars
Estimated: 30 minutes
Actual:  25 minutes
Current time: 17:50
Finish time: 18:15
"""
from guitar import Guitar


def main():
    """Main program to store and display guitar details."""
    guitars = get_user_guitars()
    display_guitars(guitars)


def get_user_guitars():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ")
    return guitars


def display_guitars(guitars):
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()
