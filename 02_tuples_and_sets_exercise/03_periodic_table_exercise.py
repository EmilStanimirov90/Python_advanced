n = int(input())
unique_elements = set()

for _ in range(n):

    unique_elements.update([el for el in input().split()])

#     current_elements = (input().split())
#     for element in current_elements:
#         unique_elements.add(element)

print(*unique_elements, sep="\n")
