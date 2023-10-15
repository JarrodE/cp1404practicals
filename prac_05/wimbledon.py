"""
Wimbledon
Estimated: 1 hour
Actual: 2 hours
"""

import csv


def main():
    """Main function to process and display Wimbledon data."""
    winners = []
    champion_to_wins = {}
    countries = set()
    filename = "wimbledon.csv"
    read_wimbledon_data(filename, winners)
    count_wins_and_countries(winners, champion_to_wins, countries)
    display_winners(champion_to_wins, countries)


def read_wimbledon_data(filename, winners):
    """Read Wimbledon data from A CSV file and populate winners list."""
    with open(filename, 'r', encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            winners.append(parts)


def count_wins_and_countries(winners, champion_to_wins, countries):
    """Count the wins of each champion and collect countries."""
    for winner in winners:
        countries.add(winner[1])
        try:
            champion_to_wins[winner[2]] += 1
        except KeyError:
            champion_to_wins[winner[2]] = 1


def display_winners(champion_to_wins, countries):
    """Display champions, their win counts and the list of countries that have won."""
    print("Wimbledon Champions: ")
    for champion, wins in sorted(champion_to_wins.items()):
        print(f"{champion} {wins}")
    countries_str = ", ".join(sorted(countries))
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(countries_str)


main()
