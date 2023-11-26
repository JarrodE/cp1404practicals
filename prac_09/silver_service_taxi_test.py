from silver_service_taxi import SilverServiceTaxi
# task 5
luxury_taxi = SilverServiceTaxi("Limo", 200, 2)

luxury_taxi.drive(18)

print(luxury_taxi)
print(f"Total fare: ${luxury_taxi.get_fare():.2f}")
