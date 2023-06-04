targets = list(map(int, input().split(' ')))
count_of_shot = 0

while True:
    command = input()
    if command == 'End':
        break
    indices = int(command)
    if 0 <= indices < len(targets):
        value = targets[indices]
        targets[indices] = -1
        count_of_shot += 1
        for current_index in range(len(targets)):
            if targets[current_index] != -1:
                if targets[current_index] > value:
                    targets[current_index] -= value
                elif targets[current_index] <= value:
                    targets[current_index] += value
    else:
        continue

string_list = [str(x) for x in targets]
print(f"Shot targets: {count_of_shot} -> {(' '.join(string_list))}")
