import os

WORKING_PATH_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_PATH_DIRECTORY, "numbers.txt")

file = open(file_path, "r")
sum = 0
for line in file.readlines():
    sum += int(line)

print(sum)
file.close()
# file = open("numbers.txt ", 'r')
# sum = 0
#
# for line in file:
#
#     sum += int(line)
#
# print(sum)

