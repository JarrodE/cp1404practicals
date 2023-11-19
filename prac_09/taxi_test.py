from taxi import Taxi

my_taxi = Taxi("Prius 1", 100)  # Task 1 (program 1) & Task 3 (program 2)

my_taxi.drive(40)  # task 2

print(my_taxi)  # Task 3
print(f"The curren fare is: {my_taxi.get_fare():.2f}")

my_taxi.start_fare()  # Task 4

my_taxi.drive(100)  # Task 4

print(my_taxi)  # Task 5
print(f"The curren fare is: {my_taxi.get_fare():.2f}")
