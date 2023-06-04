import re
sentence = input()
regex = r'\b(?<=\s)([A-Za-z0-9]+([\.\-\_][A-Za-z0-9]+)*@[A-Za-z]+([\-][A-Za-z]+)*\.[A-Za-z]+([\.][A-Za-z]+)*)'
matches = re.findall(regex, sentence)
for match in matches:
    print(match[0])