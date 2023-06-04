sentence = input()
result = ''

for char in sentence:
    new_char = chr(ord(char) + 3)
    result += new_char

print(result)
