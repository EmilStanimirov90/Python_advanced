# file = open('my_first_file.txt', 'w')
#
# file.write('I just created my first file!')
# file.close()

with open('my_first_file.txt', 'w') as file:
    file.write('I just created my first file!')