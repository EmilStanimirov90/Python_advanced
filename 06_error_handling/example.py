a = [1, 2, 3]
index = 4

try:
    print(int(a[5]))
except (IndexError, ValueError):
    print("Invalid index")
# except Exception:
#     print("Invalid index")
