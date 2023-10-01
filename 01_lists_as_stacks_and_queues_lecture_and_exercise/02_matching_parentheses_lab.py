expression = input()
stack = []
for i in range(len(expression)):
    if expression[i] == "(":
        stack.append(i)
    if expression[i] == ")":
        end = i+1
        start = stack.pop()
        print(expression[start:end])
