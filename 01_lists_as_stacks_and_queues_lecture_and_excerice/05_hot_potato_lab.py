from collections import deque

kids_circle = (input().split())
kids_circle = deque(kids_circle)
burnt_toss = int(input())
counter = 1
while len(kids_circle) > 1:
    if counter == burnt_toss:
        print(f'Removed {kids_circle.popleft()}')
        counter = 1

    else:
        counter += 1
        non_burnt_kid = kids_circle.popleft()
        kids_circle.append(non_burnt_kid)

print(f"Last is {kids_circle[0]}")
