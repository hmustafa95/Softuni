movie = input()
free_spots = int(input())
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
ticket_counter = 0

while movie != 'Finish':
    type_of_ticket = input()
    while type_of_ticket != 'End':
        ticket_counter += 1
        free_spots -= 1
        if free_spots < 0:
            break
        else:
            if type_of_ticket == 'standard':
                standard_tickets += 1
            elif type_of_ticket == 'student':
                student_tickets += 1
            elif type_of_ticket == 'kid':
                kids_tickets += 1
        type_of_ticket = input()
    percent_full = (standard_tickets + student_tickets + kids_tickets) / free_spots * 100
    print(f'{movie} - {percent_full:.2f}% full.')
    movie = input()

percent_student = student_tickets / ticket_counter * 100
percent_standard = standard_tickets / ticket_counter * 100
percent_kids = kids_tickets / ticket_counter * 100

print(f'Total tickets: {ticket_counter}')
print(f'{percent_student:.2f}% student tickets.')
print(f'{percent_standard:.2f}% standard tickets.')
print(f'{percent_kids:.2f}% kids tickets.')
