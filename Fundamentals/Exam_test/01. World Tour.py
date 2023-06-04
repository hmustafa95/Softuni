stops = input()

while True:
    token = input()
    if token == 'Travel':
        print(f"Ready for world tour! Planned stops: {stops}")
        break

    tokens = token.split(':')
    command = tokens[0]

    if command == 'Add Stop':
        index = int(tokens[1])
        text = tokens[2]

        if 0 <= index < len(stops):
            stops = stops[:index] + text + stops[index:]
        print(stops)
    elif command == 'Remove Stop':
        start_index = int(tokens[1])
        end_index = int(tokens[2])

        if 0 <= start_index <= end_index and start_index <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index + 1:]
        print(stops)
    elif command == 'Switch':
        old_string = tokens[1]
        new_string = tokens[2]

        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)