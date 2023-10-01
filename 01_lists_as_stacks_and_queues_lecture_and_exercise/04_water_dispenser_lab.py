from collections import deque
water_capacity = int(input())
water_queue = deque()

while True:
    command = input()
    if command == "Start":
        break
    else:
        water_queue.append(command)

while True:
    used_water = input()
    if used_water == "End":
        break
    if "refill" in used_water:
        a, refill_liters = used_water.split(' ')
        water_capacity += int(refill_liters)
    else:

        if water_capacity >= int(used_water):
            print(f"{water_queue.popleft()} got water")
            water_capacity -= int(used_water)
        else:
            print(f"{water_queue.popleft()} must wait")

print(f"{water_capacity} liters left")
