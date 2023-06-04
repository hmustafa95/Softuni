def characters_long(a):
    if 6 <= len(a) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False

def only_letters_digits(a):
    if a.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False

def atleast_two_digits(a):
    digits = 0
    for current_index in a:
        if current_index.isdigit():
            digits += 1
    if digits >= 2:
        return True
    print("Password must have at least 2 digits")
    return False

password = input()
valid_pass = [characters_long(password), only_letters_digits(password), atleast_two_digits(password)]

if all(valid_pass):
    print('Password is valid')
