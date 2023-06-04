import re
text = input()
regex = r'\d+'
while True:
    if text:
        match = re.findall(regex, text)
        if match:
            print(' '.join(match), end= ' ')
    else:
        break
    text = input()