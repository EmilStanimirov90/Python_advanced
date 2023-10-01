qty_movement = int(input())

cars_data = set()

for car in range(qty_movement):
    direction, car_number = input().split(", ")

    if direction == "IN":
        cars_data.add(car_number)
    else:
        cars_data.discard(car_number)
if cars_data:
    print("\n".join(cars_data))
else:
    print("Parking Lot is Empty")