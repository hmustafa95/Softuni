number_lines = int(input())
open_counter = 0
close_counter = 0
total_open = 0
total_closed = 0
unbalanced_check = False

for current_index in range(number_lines):
    received_symbol = input()
    if open_counter == 0 or close_counter == 0:
        unbalanced_check = True
        print('UNBALANCED')
        break
    if received_symbol == '(':
        open_counter += 1
        total_open += 1
        continue
    elif received_symbol == ')':
        close_counter += 1
        total_closed += 1
        continue
    open_counter = 0
    close_counter = 0

if total_open < total_closed:
    unbalanced_check = True
    print('UNBALANCED')

if not unbalanced_check:
    print('BALANCED')
