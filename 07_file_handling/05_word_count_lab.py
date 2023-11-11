import re

with open("words.txt", "r") as file:
    searched_words = file.read().lower().split()

with open("input.txt", 'r') as file:
    text = file.read().lower()

result = {}

for word in searched_words:
    pattern = rf"\b{word}\b"
    found = re.findall(pattern, text)
    result[word] = len(found)


result = dict(sorted(result.items(), key=lambda x: (-x[1])))

with open("output.txt", 'w') as file:
    for k, v in result.items():
        file.write(f'{k} - {v}\n')
