import re
number = input()
regex = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
matches = re.finditer(regex, number)

for pattern in matches:
    print(pattern.group(), end=' ')