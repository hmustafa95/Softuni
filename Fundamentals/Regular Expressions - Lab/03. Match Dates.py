import re
dates = input()
regex = r'\b(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})\b'
matches = re.findall(regex, dates)

for pattern in matches:
    print(f'Day: {pattern[0]}, Month: {pattern[2]}, Year: {pattern[3]}')