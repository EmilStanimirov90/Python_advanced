def accommodate_new_pets(hotel_capacity: int, weight_limit: float, *args):
    accommodated_pets = {}
    valid_pets = 0
    for pet_type, pet_weight in args:
        valid_pets += 1
        if hotel_capacity > 0:

            if pet_weight > weight_limit:
                valid_pets -= 1
                continue
            if pet_type not in accommodated_pets.keys():
                accommodated_pets[pet_type] = 0
            accommodated_pets[pet_type] += 1
            hotel_capacity -= 1

    if valid_pets == sum([p for p in accommodated_pets.values()]):
        result = f"All pets are accommodated! Available capacity: {hotel_capacity}.\n"
    else:
        result = f"You did not manage to accommodate all pets!\n"

    result += "Accommodated pets:\n"
    sorted_pets = sorted(accommodated_pets.items())
    for p, q in sorted_pets:
        result += f"{p}: {q}\n"

    return result


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),

))
