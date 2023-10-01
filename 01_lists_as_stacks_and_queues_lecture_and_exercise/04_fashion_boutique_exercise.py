box_of_clothes = [int(x) for x in input().split()]
racks_capacity = int(input())

racks_counter = 0

while box_of_clothes:
    racks_counter += 1
    current_rack_capacity = racks_capacity
    while box_of_clothes and box_of_clothes[-1] <= current_rack_capacity:
        current_rack_capacity -= box_of_clothes.pop()

print(racks_counter)

