from collections import deque

expression = input().split()

operators = "+-*/"

calculation = deque()

for symbol in expression:

    if symbol not in operators:
        calculation.append(int(symbol))
    else:
        while len(calculation) > 1:

            if symbol == "+":
                calculation.appendleft(calculation.popleft() + calculation.popleft())
            elif symbol == "-":
                calculation.appendleft(calculation.popleft() - calculation.popleft())
            elif symbol == "*":
                calculation.appendleft(calculation.popleft() * calculation.popleft())
            elif symbol == "/":
                calculation.appendleft(calculation.popleft() // calculation.popleft())


print(calculation.pop())
