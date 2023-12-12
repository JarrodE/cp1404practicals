"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When anything other than a number is input
2. When will a ZeroDivisionError occur?
When a 0 is input in the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Do an error check for 0 before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Please input a number other than zero")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
