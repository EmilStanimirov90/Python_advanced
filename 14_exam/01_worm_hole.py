from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])
matches = 0
did_not_find_a_hole = False
while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()
    if hole == worm:
        matches += 1
        pass
    else:
        worm -= 3
        if worm > 0:
            worms.append(worm)
        else:
            did_not_find_a_hole = True

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms and did_not_find_a_hole:
    print("Worms left: none")
elif not worms:
    print("Every worm found a suitable hole!")

elif worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")

if not holes:
    print("Holes left: none")
else:
    print(f"Worms left: {', '.join(str(x) for x in holes)}")

