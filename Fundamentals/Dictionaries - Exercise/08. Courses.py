courses = {}

while True:
    command = input()
    if command == 'end':
        break
    command_list = command.split(' : ')
    course = command_list[0]
    student = command_list[1]
    if course not in courses:
        courses[course] = []
    courses[course] += [student]

for index in courses.keys():
    print(f"{index}: {len(courses[index])}")
    for value in courses[index]:
        print(f"-- {value}")
