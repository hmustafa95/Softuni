usernames = input().split(', ')

for username in usernames:
    valid_username = True
    if not 3 <= len(username) <= 16:
        valid_username = False
    for char in username:
        if not (char.isalnum() or char == '-' or char == '_'):
            valid_username = False
    if ' ' in username:
        valid_username = False
    if valid_username:
        print(username)
