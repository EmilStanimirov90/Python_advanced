qty_guests = int(input())
guest_list = set()

for _ in range(qty_guests):
    guest_list.add(input())

while True:
    name = input()
    if name == "END":
        break
    guest_list.discard(name)

print(len(guest_list))
print("\n".join(sorted(guest_list)))