def operate(sign, *args):
    def add():
        return sum(args)

    def subtract():
        result = args[0]
        for index in range(1, len(args)):
            result -= args[index]
        return result

    def multiply():
        result = args[0]
        for index in range(1, len(args)):
            result *= args[index]
        return result

    def divide():
        result = args[0]
        for index in range(1, len(args)):
            result /= args[index]
        return result

    if sign == "+":
        return add()
    elif sign == "-":
        return subtract()
    elif sign == "*":
        return multiply()
    elif sign == "/":
        return divide()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
