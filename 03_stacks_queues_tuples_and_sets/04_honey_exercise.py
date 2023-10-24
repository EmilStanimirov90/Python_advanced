from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0

while bees and nectar:
    first_bee = bees[0]
    last_nectar = nectar[-1]
    if last_nectar >= first_bee:
        if symbols[0] == "+":
            result = bees.popleft() + nectar.pop()
            total_honey += abs(result)
            symbols.popleft()
        elif symbols[0] == "-":
            result = bees.popleft() - nectar.pop()
            total_honey += abs(result)
            symbols.popleft()
        elif symbols[0] == "/":
            if last_nectar == 0:
                symbols.popleft()
                bees.popleft()
                nectar.pop()
            else:
                result = bees.popleft() / nectar.pop()
                total_honey += abs(result)
                symbols.popleft()
        elif symbols[0] == '*':
            result = bees.popleft() * nectar.pop()
            total_honey += abs(result)
    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")