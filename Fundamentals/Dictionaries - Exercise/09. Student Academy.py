number = int(input())
academy = {}

for index in range(number):
    name = input()
    grade = float(input())
    if name not in academy:
        academy[name] = []
    academy[name] += [grade]

for current_index in academy.keys():
    average_grades = sum(academy[current_index]) / len(academy[current_index])
    academy[current_index] = average_grades

for k, v in academy.items():
    if academy[k] >= 4.50:
        print(f"{k} -> {v:.2f}")
