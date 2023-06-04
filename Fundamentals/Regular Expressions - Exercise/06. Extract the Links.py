import re

sentences = input()
valid_sites = []
regex = r'www\.[A-Za-z0-9\-]+\.[a-z]+[\.a-z]*'
while sentences:
    matches = re.finditer(regex, sentences)
    for match in matches:
        valid_sites.append(match.group(0))
    sentences = input()

for site in valid_sites:
    print(site)