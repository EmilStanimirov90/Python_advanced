qty_numbers = int(input())
stack = []
for index in range(qty_numbers):
    query = input()
    if query.startswith("1"):
        query = query.split()
        stack.append(query[1])

    elif stack:
        if query == "2":
            stack.pop()
        elif query == "3":
            print(max(stack))
        elif query == "4":
            print(min(stack))

reversed_stack = []
while stack:
    reversed_stack.append(stack.pop())
print(", ".join(reversed_stack))
