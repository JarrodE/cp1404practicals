from unreliable_car import UnreliableCar

my_unreliable_car = UnreliableCar("Old Junk", 100, 50)

distance_driven = my_unreliable_car.drive(30)

print(f"Attempted to drive 30km: Drove {distance_driven}km")