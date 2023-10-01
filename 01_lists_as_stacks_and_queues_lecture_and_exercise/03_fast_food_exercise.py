from collections import deque

qty_food = int(input())
order_queue = deque([int(x) for x in input().split()])

print(max(order_queue))

while order_queue and order_queue[0] <= qty_food:
    current_order = order_queue.popleft()
    qty_food -= current_order


if not order_queue:
    print("Orders complete")
else:
    print("Orders left:", end='')
    while order_queue:
        print(f' {order_queue.popleft()}', end="")
