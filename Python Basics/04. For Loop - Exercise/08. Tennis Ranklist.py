number_tournaments = int(input())
start_points = int(input())
won_points = 0
total_won_tournaments = 0
won_games = 0

for something in range(number_tournaments):
    ranking = input()
    if ranking == 'W':
        won_points += 2000
        won_games += 1
    elif ranking == 'F':
        won_points += 1200
    elif ranking == 'SF':
        won_points += 720

total_points = won_points + start_points
print(f'Final points: {total_points}')

average_points = won_points / number_tournaments
import math
average_points = math.floor(average_points)
print(f'Average points: {average_points}')

average_won_games = won_games / number_tournaments * 100
print(f'{average_won_games:.2f}%')
