materials = [int(x) for x in input().split()]
magic_level = list(reversed([int(x) for x in input().split()]))

magic_needed_for_toys = {150: 'Doll', 250: "Wooden train", 300: 'Teddy bear', 400: "Bicycle"}
crafted = {}

while materials and magic_level:
    current_toy_magic = materials[-1] * magic_level[-1]

    if materials[-1] == 0 and magic_level[-1] == 0:
        materials.pop()
        magic_level.pop()
    elif materials[-1] == 0:
        materials.pop()
    elif magic_level[-1] == 0:
        magic_level.pop()
    elif current_toy_magic in magic_needed_for_toys.keys():
        if magic_needed_for_toys[current_toy_magic] not in crafted:
            crafted[magic_needed_for_toys[current_toy_magic]] = 0
        crafted[magic_needed_for_toys[current_toy_magic]] += 1
        materials.pop()
        magic_level.pop()
    elif current_toy_magic < 0:
        materials.append(materials.pop() + magic_level.pop())
    elif current_toy_magic > 0:
        magic_level.pop()
        materials[-1] += 15


if ("Doll" in crafted and "Wooden train" in crafted) or ('Teddy bear' in crafted and "Bicycle" in crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    materials = reversed(materials)
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_level:
    magic_level = reversed(magic_level)
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")
if crafted:
    for toy, qty in sorted(crafted.items()):
        print(f'{toy}: {qty}')
