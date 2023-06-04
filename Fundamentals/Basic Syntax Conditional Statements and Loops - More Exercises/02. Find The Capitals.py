word = input()
list_of_index = []
counter = -1

for current_index in word:
    counter += 1
    if current_index.isupper():
        list_of_index.append(counter)

print(list_of_index)
