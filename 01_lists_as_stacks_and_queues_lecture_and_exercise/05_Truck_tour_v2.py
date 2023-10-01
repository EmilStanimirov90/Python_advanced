from collections import deque
n_petrol_stations = int(input())

gas_stations_data = deque()

for _ in range(n_petrol_stations):
    fuel, distance = input().split()
    gas_stations_data.append([fuel, distance])

starting_station = 0
stops = 0

while stops < n_petrol_stations:

    fuel_filled = 0
    for index in range(n_petrol_stations):
        fuel_filled += int(gas_stations_data[index][0])
        distance_till_next_station = int(gas_stations_data[index][1])
        if fuel_filled < distance_till_next_station:
            stops = 0
            gas_stations_data.rotate(-1)
            starting_station += 1
            break
        fuel_filled -= distance_till_next_station
        stops += 1

print(starting_station)