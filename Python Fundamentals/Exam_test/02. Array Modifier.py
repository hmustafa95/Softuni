elements = [int(x) for x in input().split(' ')]

while True:
    token = input()
    if token == 'end':
        break

    tokens = token.split(' ')
    command = tokens[0]

    if command == 'swap':
        index1 = int(tokens[1])
        index2 = int(tokens[2])

        first_num = elements[index1]
        second_num = elements[index2]

        elements[index1] = second_num
        elements[index2] = first_num
    elif command == 'multiply':
        index1 = int(tokens[1])
        index2 = int(tokens[2])

        first_num = elements[index1]
        second_num = elements[index2]

        elements[index1] = first_num * second_num
    elif command == 'decrease':
        for index in range(len(elements)):
            elements[index] -= 1

result = list(map(str, elements))
print(', '.join(result))