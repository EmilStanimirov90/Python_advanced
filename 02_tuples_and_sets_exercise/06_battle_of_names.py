n = int(input())

even_set = set()
odd_set = set()
# row_number = 0

# for _ in range(n):
#     ascii_sum = 0
#     row_number += 1
#     name = input()

for i in range(1, n + 1):
    ascii_sum = sum([ord(letter) for letter in input()]) // i

    # for letter in name:
    #     ascii_sum += ord(letter)
    # ascii_sum //= row_number

    if ascii_sum % 2 != 0:
        odd_set.add(ascii_sum)
    elif ascii_sum % 2 == 0:
        even_set.add(ascii_sum)

if sum(odd_set) < sum(even_set):
    result = odd_set.symmetric_difference(even_set)
elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)
elif sum(odd_set) == sum(even_set):
    result = odd_set.union(even_set)

#result = {x for x in result}
# print(", ".join(result))
print(*result, sep=', ')