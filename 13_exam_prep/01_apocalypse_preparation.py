from collections import deque

textiles = deque([int(x) for x in input().split()])
medicines = [int(x) for x in input().split()]

items = {30: "Patch", 40: "Bandage", 100: "MedKit"}
items_made = {}
already_added = False

while True:
    if not textiles or not medicines:
        break
    medicine = medicines.pop()
    textile = textiles.popleft()
    result = textile + medicine
    if result > 100:
        if "MedKit" not in items_made:
            items_made["MedKit"] = 0
        items_made["MedKit"] += 1
        excess = result - 100
        if medicines:
            medicines[-1] += excess
        else:
            medicines.append(excess)
        continue

    for value in items.keys():
        if value == result:
            if items[value] not in items_made:
                items_made[items[value]] = 0
            items_made[items[value]] += 1
            break
    else:
        medicines.append(medicine + 10)

if not textiles and not medicines:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicines:
    print("Medicaments are empty.")

sorted_items = dict(sorted(items_made.items(), key=lambda x: (-x[1], x[0])))
for i, q in sorted_items.items():
    print(f"{i} - {q}")

if medicines:
    print(f'Medicaments left: {", ".join(str(x) for x in medicines)}')
if textiles:
    print(f'Textiles left: {", ".join(str(x) for x in textiles)}')
