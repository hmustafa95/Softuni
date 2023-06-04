data = {}

while True:
    command = input()
    if ":" in command:
        tokens = command.split(":")
        name = tokens[0]
        id_student = int(tokens[1])
        course = tokens[2]
        if course not in data:
            data[course] = {}
        data[course][name] = id_student
    else:
        course = command.replace("_", ' ')
        break

for k, v in data[course].items():
    print(f"{k} - {v}")
