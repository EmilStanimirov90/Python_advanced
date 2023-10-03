# text = list(input())
#
# unique_symbols = sorted(set(text))
#
# for symbol in unique_symbols:
#     print(f"{symbol}: {text.count(symbol)} time/s")
#
text = list(input())
occurrences = {}
for symbol in text:
    if symbol not in occurrences:
        occurrences[symbol] = 1
    else:
        occurrences[symbol] += 1
sorted_items = sorted(occurrences.items())
sorted_dict = dict(sorted_items)

for char, qty in sorted_dict.items():
    print(f"{char}: {qty} time/s")
