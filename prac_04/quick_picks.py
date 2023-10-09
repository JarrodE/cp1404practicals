"""A Program the generates "quick picks" like the lottery"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_QUICK_PICK = 6
NUMBER_OF_QUICK_PICKS = int(input("How many quick picks? "))


def main():
    return generate_quick_pick()


def generate_quick_pick():
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_QUICK_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick


def print_quick_pick():
    for i in range(NUMBER_OF_QUICK_PICKS):
        quick_pick = generate_quick_pick()
        formatted_numbers = " ".join(map("{:2}".format, quick_pick))
        print(formatted_numbers)


print_quick_pick()


main()
