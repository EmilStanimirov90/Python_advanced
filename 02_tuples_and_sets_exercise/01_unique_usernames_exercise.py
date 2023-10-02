number_of_usernames = int(input())

list_of_usernames = set()

for _ in range(number_of_usernames):
    list_of_usernames.add(input())

print('\n'.join(list_of_usernames))