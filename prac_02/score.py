"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    # score = float(input("Enter score: "))
    # score = parameters(score)
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    score_ranks(random_score)


def score_ranks(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Pass")
    else:
        print("Fail")


def parameters(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


main()
