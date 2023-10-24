from collections import deque

string = deque(input().split())

main = ["red", "yellow", "blue"]
secondary = ["orange", "purple", "green"]

colors = []
while string:
    left_string = string.popleft()
    if string:
        right_string = string.pop()
    else:
        right_string = ''

    if left_string + right_string in main or left_string + right_string in secondary:
        colors.append(left_string + right_string)
    elif right_string + left_string in main or right_string + left_string in secondary:
        colors.append(right_string + left_string)

    else:
        if len(left_string) > 1:
            string.insert(len(string) // 2, left_string[:-1])
        if len(right_string) > 1:
            string.insert(len(string) // 2, right_string[:-1])
for el in colors:
    if el == "orange":
        if 'red' not in colors or "yellow" not in colors:
            colors.remove("orange")
    elif el == "purple":
        if 'red' not in colors or "blue" not in colors:
            colors.remove("purple")
    elif el == "green":
        if 'blue' not in colors or "yellow" not in colors:
            colors.remove("green")

print(colors)
