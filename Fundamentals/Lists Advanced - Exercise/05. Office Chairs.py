def check_charis(number_of_rooms):
    total_free_chairs = 0
    chairs_needed = 0
    for current_room in range(1, number_of_rooms + 1):
        free_chairs, visitors = input().split()
        difference = len(free_chairs) - int(visitors)
        if difference >= 0:
            total_free_chairs += difference
        else:
            chairs_needed += abs(difference)
            print(f'{abs(difference)} more chairs needed in room {current_room}')
    return total_free_chairs, chairs_needed

number_of_rooms = int(input())
total_free_chairs, needed_chairs = check_charis(number_of_rooms)
if total_free_chairs >= needed_chairs:
    print(f'Game On, {total_free_chairs} free chairs left')

