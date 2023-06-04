import re
words = input()
searched_word = input()
regex = fr'\b{searched_word}\b'
matches = re.findall(regex, words, re.IGNORECASE)
print(len(matches))