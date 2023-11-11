
try:
    file = open('text.txt', 'r')
    print('File found')
    file.close()
except FileExistsError:
    print('File not found')
