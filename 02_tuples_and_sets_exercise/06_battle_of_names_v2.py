n = int(input())
row_number = 0

odd_set = set()
even_set = set()
for _ in range(n):
    row_number += 1
    name = input()
    ascii_sum = sum([ord(letter) for letter in name]) // row_number

    if ascii_sum % 2 == 0:
        even_set.add(ascii_sum)
    else:
        odd_set.add(ascii_sum)

if sum(odd_set) == sum(even_set):
    result = odd_set | even_set
elif sum(odd_set) > sum(even_set):
    result = odd_set - even_set
elif sum(odd_set) < sum(even_set):
    result = odd_set ^ even_set

result = {str(x) for x in result}
print(", ".join(result))
