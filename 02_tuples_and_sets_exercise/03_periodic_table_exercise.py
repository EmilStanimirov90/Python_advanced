n = int(input())
unique_elements = set()
for _ in range(n):
    current_elements = (input().split())
    for element in current_elements:
        unique_elements.add(element)
print(*unique_elements, sep="\n")
