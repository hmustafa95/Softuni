phonebook = {}

while True:
    command = input()
    if len(command) < 3:
        break
    people_numbers = command.split('-')
    name = people_numbers[0]
    phone = people_numbers[1]
    if name not in phonebook:
        phonebook[name] = 0
    phonebook[name] = phone

number = int(command)

for current_index in range(number):
    rcvd_name = input()
    if rcvd_name in phonebook:
        print(f"{rcvd_name} -> {phonebook[rcvd_name]}")
    else:
        print(f"Contact {rcvd_name} does not exist.")
