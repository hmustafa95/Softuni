sentence = input()
index = 0
indexes = []

for char in sentence:
    index += 1
    if char == ':':
        indexes.append(index)

for current_index in indexes:
    print(f"{sentence[current_index - 1]}{sentence[current_index]}")
