import math

tvseries = input()
length_episode = int(input())
length_break = int(input())

lunch = length_break / 8
time_break = length_break / 4

left_over = length_break - lunch - time_break

result = math.ceil(left_over - length_episode)

needed = math.ceil(length_episode - left_over)

if left_over >= length_episode:
    print(f'You have enough time to watch {tvseries} and left with {result} minutes free time.')
else:
    print(f"You don't have enough time to watch {tvseries}, you need {needed} more minutes.")
