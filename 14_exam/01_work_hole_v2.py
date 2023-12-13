from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])
matches = 0
drop_out_worm = 0
while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()
    if worm == hole:
        matches += 1
    if worm != hole:
        worm -= 3
        worms.append(worm)
        if worm <= 0:
            worms.pop()
            drop_out_worm += 1

if matches:
    print(f"Matches: {matches}")
else:
    print(f"There are no matches.")

if not worms and drop_out_worm > 0:
    print("Worms left: none")
elif not worms and drop_out_worm == 0:
    print(f"Every worm found a suitable hole!")
elif worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")

if not holes:
    print("Holes left: none")
elif holes:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")