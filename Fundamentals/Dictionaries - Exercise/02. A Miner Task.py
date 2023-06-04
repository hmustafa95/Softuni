resources = {}

while True:
    command = input()
    if command == 'stop':
        break
    material = command
    quantity = int(input())
    if material not in resources:
        resources[material] = 0
    resources[material] += quantity

for key, value in resources.items():
    print(f"{key} -> {value}")
