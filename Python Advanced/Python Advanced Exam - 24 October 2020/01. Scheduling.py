from collections import deque

jobs = deque(map(int, input().split(', ')))
interested_job = int(input())
cycles = 0

max_checks = max(jobs)

for idx in range(1, max_checks + 1):
    for job in jobs:
        if idx == job:
            cycles += idx
    if idx == jobs[interested_job]:
        break

print(cycles)