characters_list = input().split(', ')
asci_dict = {}

for current_index in characters_list:
    letter = current_index
    number = ord(letter)
    asci_dict[letter] = number

print(asci_dict)