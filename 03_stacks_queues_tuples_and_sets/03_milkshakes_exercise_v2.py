from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk = deque([int(x) for x in input().split(", ")])

milkshakes = 0

while milkshakes < 5 and milk and chocolates:
    firs_milk = milk[0]
    last_chocolate = chocolates[-1]
    if firs_milk <= 0 and last_chocolate <=0:
        milk.popleft()
        chocolates.pop()
    elif firs_milk <= 0:
        milk.popleft()
    elif last_chocolate <=0:
        chocolates.pop()
    else:

        if last_chocolate == firs_milk:
                milkshakes += 1
                milk.popleft()
                chocolates.pop()
        elif last_chocolate != firs_milk:
            milk.rotate(-1)
            chocolates[-1] -= 5
if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join([str(x) for x in milk])}")
else:
    print("Milk: empty")
