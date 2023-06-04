words = input()
counting = {}

for current_index in words:
    if current_index != ' ':
        if current_index not in counting:
            counting[current_index] = 0
        counting[current_index] += 1

for key, value in counting.items():
    print(f"{key} -> {value}")
