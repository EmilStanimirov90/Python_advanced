from collections import deque

gas_stations = deque()
qty_gas_stations = int(input())
start_position = 0
stops = 0

for _ in range(qty_gas_stations):
    fuel_filled, distance_until_next = input().split()
    gas_stations.append([int(fuel_filled), int(distance_until_next)])

while True:
    if stops > qty_gas_stations:
        break

    fuel = 0
    for index in range(qty_gas_stations):
        fuel += gas_stations[index][0]
        distance = gas_stations[index][1]
        stops += 1
        if fuel < distance:
            gas_stations.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= distance
        stops += 1
print(start_position)



