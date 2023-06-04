text = input()

last_char = ''
new_text = ''

for char in text:
    if char != last_char:
        new_text += char
        last_char = char
        continue

print(new_text)