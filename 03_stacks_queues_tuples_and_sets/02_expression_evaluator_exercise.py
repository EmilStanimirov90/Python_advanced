from collections import deque

expression = input().split()

operators = '+-/*'
# operators = {
#     '+': lambda a, b: a + b,
#     '-': lambda a, b: a - b,
#     '*': lambda a, b: a * b,
#     '/': lambda a, b: a // b,
# }

numbers = deque()

for symbol in expression:
    if symbol not in operators:
        numbers.append(int(symbol))
    else:
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            if symbol == "+":
                numbers.appendleft(first_num + second_num)
            elif symbol == "-":
                numbers.appendleft(first_num - second_num)
            elif symbol == "*":
                numbers.appendleft(first_num * second_num)
            elif symbol == "/":
                numbers.appendleft(first_num // second_num)
    # numbers.appendleft(operators[symbol](first_num, second_num))

print(numbers[0])
