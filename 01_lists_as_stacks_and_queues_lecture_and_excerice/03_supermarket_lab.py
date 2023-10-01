from collections import deque


queue = deque()

while True:
    customer = input()
    if customer == "End":
        break
    if customer == "Paid":
        for index in range(len(queue)):
            print(queue.popleft())
    if customer != "Paid":
        queue.append(customer)

print(f"{len(queue)} people remaining.")
