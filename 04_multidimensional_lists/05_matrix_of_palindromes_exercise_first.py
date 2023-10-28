a = "a"
a = ord(a)

rows, cols = [int(x) for x in input().split()]

for row in range(rows):
    print()
    for col in range(cols):
        print(f"{chr(a + row)}{chr(a+row+col)}{chr(a+row)}", end=' ')
