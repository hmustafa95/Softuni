received_list = input().split('@')
neighbourhood_list = [int(x) for x in received_list]
index_counter = 0

while True:
    command = input()
    if command == 'Love!':
        break
    command_list = command.split(' ')
    index_counter += int(command_list[1])
    if index_counter >= len(neighbourhood_list):
        index_counter = 0
    neighbourhood_list[index_counter] -= 2
    if neighbourhood_list[index_counter] == 0:
        print(f"Place {index_counter} has Valentine's day.")
    elif neighbourhood_list[index_counter] < 0:
        neighbourhood_list[index_counter] = 0
        print(f"Place {index_counter} already had Valentine's day.")

failed_number = [x for x in neighbourhood_list if x != 0]
numbers_failed = len(failed_number)

print(f"Cupid's last position was {index_counter}.")
if sum(neighbourhood_list) == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {numbers_failed} places.")
