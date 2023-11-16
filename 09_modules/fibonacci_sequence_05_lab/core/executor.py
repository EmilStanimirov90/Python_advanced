from fib_helpers import create_sequence, locate


def play_fibonacci():
    sequence = []
    while True:
        command = input()
        if command == "Stop":
            break
        if command.startswith("Create"):
            n = int(command.split()[-1])
            sequence = create_sequence(n)
            print(*sequence)
        else:
            number = int(command.split()[-1])

            print(locate(number, sequence))
