import re

sentence = input()
regex = r'([\@|\#])([A-Za-z][A-Za-z][A-Za-z]+)\1\1([A-Za-z][A-Za-z][A-Za-z]+)\1'
matches = re.finditer(regex, sentence)
list_words = []

for match in matches:
    word = match.group(2)
    word_two = match.group(3)
    list_words.append(word)
    list_words.append(word_two)

pairs = len(list_words) // 2

if pairs == 0:
    print('No word pairs found!')
else:
    print(f'{pairs} word pairs found!')

mirror_words = []

for current_index in range(0, len(list_words), 2):
    first_word = list_words[current_index]
    second_word = list_words[current_index + 1]
    if first_word == second_word[::-1]:
        mirror_words.append(first_word)
        mirror_words.append(second_word)

list_result = []
for current in range(0, len(mirror_words), 2):
    one = mirror_words[current]
    two = mirror_words[current + 1]
    result = one + ' <=> ' + two
    list_result.append(result)

if len(mirror_words) == 0:
    print('No mirror words!')
else:
    print('The mirror words are:')
    print(', '.join(list_result))
