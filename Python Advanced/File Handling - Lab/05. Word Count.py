words = open('C:/Users/thind/OneDrive/Desktop/text.txt', 'w')
words.write('quick is fault')
words.close()

text = open('C:/Users/thind/OneDrive/Desktop/words.txt', 'w')
text.write("-I was quick to judge him, but it wasn't his fault.\n")
text.write("-Is this some kind of joke?! Is it?\n")
text.write("-Quick, hide here…It is safer")
text.close()

words_as_string = ''
text_as_string = ''

words = open('C:/Users/thind/OneDrive/Desktop/text.txt', 'r')
for word in words:
    words_as_string = word
words.close()

words_list = words_as_string.split()

text = open('C:/Users/thind/OneDrive/Desktop/words.txt', 'r')
for sentence in text:
    text_as_string += sentence
text.close()

output_list = {}
for word in words_list:
    if word not in output_list:
        output_list[word] = 0

for word in words_list:
    text_as_string = text_as_string.lower()
    output_list[word] = text_as_string.count(word)

print(output_list)
