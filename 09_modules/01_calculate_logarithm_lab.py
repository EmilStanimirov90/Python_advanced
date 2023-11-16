# from math import log
# number = int(input())
# command = input()
#
# if command == "natural":
#     print(f"{log(number):.2f}")
#
# else:
#     print(f"{log(number, int(command)):.2f}")
#

import math
number = int(input())
command = input()

if command == "natural":
    print(f"{math.log(number):.2f}")

else:
    print(f"{math.log(number, int(command)):.2f}")