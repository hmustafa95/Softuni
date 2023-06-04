import re

sentence = input()
regex = r'([\=|\/])([A-Z][A-Za-z][A-Za-z]+)\1'
matches = re.finditer(regex, sentence)
travel = []
points = 0
for match in matches:
    location = match.group(2)
    travel.append(location)
    points += len(location)

print(f"Destinations: {', '.join(travel)}")
print(f'Travel Points: {points}')
