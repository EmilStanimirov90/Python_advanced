first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    command = input().split()

    if f"{command[0]} {command[1]}" == "Add First":
        numbers = [int(x) for x in command[2:]]
        first_set.update(numbers)
    elif f"{command[0]} {command[1]}" == "Add Second":
        numbers = [int(x) for x in command[2:]]
        second_set.update(numbers)
    elif f"{command[0]} {command[1]}" == "Remove First":
        numbers = [int(x) for x in command[2:]]
        first_set = first_set - set(numbers)
    elif f"{command[0]} {command[1]}" == "Remove Second":
        numbers = [int(x) for x in command[2:]]
        second_set = second_set - set(numbers)
    elif f"{command[0]} {command[1]}" == "Check Subset":
        if first_set < second_set or second_set < first_set:
            print("True")
        else:
            print("False")

print(', '. join([str(x) for x in sorted(first_set)]))

print(', '. join([str(x) for x in sorted(second_set)]))
