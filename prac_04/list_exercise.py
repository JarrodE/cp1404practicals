"""Program that prompts user for 5 numbers and then stores each
of these in a list"""


def main():
    numbers = []
    get_numbers(numbers)
    average_number, first_number, largest_number, last_number, smallest_number = calculate_numbers(numbers)
    print_numbers(average_number, first_number, largest_number, last_number, smallest_number)


def print_numbers(average_number, first_number, largest_number, last_number, smallest_number):
    print(f" The first number is {first_number}")
    print(f" The last number is {last_number}")
    print(f" The smallest number is {smallest_number}")
    print(f" The largest number is {largest_number}")
    print(f" The average of the numbers is {average_number:.1f}")


def calculate_numbers(numbers):
    first_number = numbers[0]
    last_number = numbers[-1]
    smallest_number = min(numbers)
    largest_number = max(numbers)
    average_number = sum(numbers) / len(numbers)
    return average_number, first_number, largest_number, last_number, smallest_number


def get_numbers(numbers):
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)


main()
