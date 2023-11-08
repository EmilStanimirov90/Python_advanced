a = [1, 2, 3]
index = 4

try:
    print(int(a[5]))

except IndexError:
    print("Invalid index")
except ValueError:
    print("Invalid type")

# except (IndexError, ValueError):
#     print("Error")

# except Exception:
#     print("Invalid index")
