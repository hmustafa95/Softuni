word = input()
digits = ''
letters = ''
symbols = ''

for char in word:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        symbols += char

print(digits)
print(letters)
print(symbols)
