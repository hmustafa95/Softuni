number = int(input())
registered = {}

for index in range(number):
    command = input().split(' ')
    if command[0] == 'register':
        if command[1] not in registered:
            registered[command[1]] = command[2]
            print(f"{command[1]} registered {command[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {command[2]}")
    elif command[0] == 'unregister':
        if command[1] not in registered:
            print(f"ERROR: user {command[1]} not found")
        else:
            del registered[command[1]]
            print(f"{command[1]} unregistered successfully")

for key, value in registered.items():
    print(f"{key} => {value}")
