# Question 1
name = input("Name: ")
name_file = open("name.txt", "w")
print(f"{name}", file=name_file)


# Question 2
name_file = open("name.txt", "r")
stored_name = name_file.read()
print(f"Your name is {stored_name}")


# Question 3
numbers_file = open("numbers.txt", "r")
line1 = int(numbers_file.readline())
line2 = int(numbers_file.readline())
number_addition = line1 + line2
print(f"Result = {number_addition}")


# Question 4
numbers_file = open("numbers.txt", "r")
total = 0
for line in numbers_file:
    number = int(line)
    total += number
print(f"The total = {total}")
