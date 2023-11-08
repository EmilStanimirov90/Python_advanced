text = input()
try:
    n = int(input())
    [print(text, end='') for times in range(n)]
except ValueError:
    print("Variable times must be an integer")
else:
    [print(text, end='') for times in range(n)]
    # print(text*n)

