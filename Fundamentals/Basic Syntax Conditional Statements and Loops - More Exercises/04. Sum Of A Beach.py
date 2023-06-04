command = input()
counter = 0

counter += command.lower().count('water')
counter += command.lower().count('fish')
counter += command.lower().count('sun')
counter += command.lower().count('sand')
print(counter)
