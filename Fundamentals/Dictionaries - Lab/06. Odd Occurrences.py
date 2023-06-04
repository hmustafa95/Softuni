words = input().split(' ')
elements = {}

for index in words:
    lower_index = index.lower()
    if lower_index not in elements:
        elements[lower_index] = 0
    elements[lower_index] += 1

for key, value in elements.items():
    if value % 2 != 0:
        print(key, end=' ')
