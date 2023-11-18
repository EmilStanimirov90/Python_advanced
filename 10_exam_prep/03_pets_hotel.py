def accommodate_new_pets(total_capacity, max_weight, *args):
    total_pets = len(args)
    accommodated_pets = {}
    available_capacity = total_capacity
    for pet, weight in args:
        if available_capacity == 0:
            break
        if weight > max_weight:
            total_pets -= 1
            continue
        if pet not in accommodated_pets:
            accommodated_pets[pet] = 0
        accommodated_pets[pet] += 1
        available_capacity -= 1
        total_pets -= 1
    result = ""
    if total_pets == 0:
        result += f"All pets are accommodated! Available capacity: {available_capacity}.\n"
    else:
        result += "You did not manage to accommodate all pets!\n"
    result += f'Accommodated pets:\n'
    accommodated_pets = sorted(accommodated_pets.items())
    for p, count in accommodated_pets:
        result += f"{p}: {count}\n"

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
