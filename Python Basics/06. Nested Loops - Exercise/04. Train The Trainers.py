number = int(input())
presentation = input()
final_average = 0
number_of_presentations = 0

while presentation != 'Finish':
    average_per_presentation = 0
    for num in range(number):
        average_per_presentation += float(input())
    average_per_presentation /= number
    print(f'{presentation} - {average_per_presentation:.2f}.')
    final_average += average_per_presentation
    number_of_presentations += 1
    presentation = input()

final_average /= number_of_presentations
print(f"Student's final assessment is {final_average:.2f}.")
