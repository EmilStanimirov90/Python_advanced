qty_names = int(input())
names = set()

for name in range(qty_names):
    names.add(input())

print("\n".join(names))