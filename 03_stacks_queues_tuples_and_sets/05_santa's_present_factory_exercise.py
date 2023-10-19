from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

presents_magic_needed = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
crafted_toys = {}
while materials and magic_level:
    current_magic = materials[-1] * magic_level[0]
    if current_magic in presents_magic_needed.keys():
        new_toy = presents_magic_needed[current_magic]
        if new_toy not in crafted_toys:
            crafted_toys[new_toy] = 0
        crafted_toys[new_toy] += 1
        materials.pop()
        magic_level.popleft()
    elif current_magic < 0:
        materials.append(materials.pop() + magic_level.popleft())
    elif current_magic > 0:
        magic_level.popleft()
        materials[-1] += 15
    elif materials[-1] == 0 and magic_level[0] == 0:
        materials.pop()
        magic_level.popleft()
    elif materials[-1] == 0:
        materials.pop()
    elif magic_level[0] == 0:
        magic_level.popleft()

if ("Doll" in crafted_toys and "Wooden train" in crafted_toys) or ("Teddy bear" in crafted_toys and "Bicycle" in crafted_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials[::-1]])}")
if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

sorted_crafted_toys = sorted(crafted_toys)
for key, value in sorted(crafted_toys.items()):
    print(f"{key}: {value}")