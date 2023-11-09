email = input()


file = open('users.txt', 'a')
file.write(email + '\n')

print(email)