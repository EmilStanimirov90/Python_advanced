from collections import deque

parenthesis = deque(input())

opening_brackets = "([{"
closing_brackets = ")]}"
counter = 0
while parenthesis and counter < len(parenthesis) / 2:
    if parenthesis[0] not in opening_brackets:
        break
    index = opening_brackets.index(parenthesis[0])
    if parenthesis[1] == closing_brackets[index]:
        parenthesis.popleft()
        parenthesis.popleft()
        parenthesis.rotate(counter)
        counter = 0
    else:
        parenthesis.rotate(-1)
        counter += 1

if parenthesis:
    print("NO")
else:
    print("YES")

