numbers_data = tuple(float(el) for el in input().split())

occurrences = {}

for number in numbers_data:
    if number not in occurrences:
        occurrences[number] = numbers_data.count(number)
        print(f'{number} - {numbers_data.count(number)} times')
