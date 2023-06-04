first, second = input().split(' ')
total = 0

if len(first) > len(second):
    for index in range(len(second)):
        total += ord(first[index]) * ord(second[index])
    for index in range(len(second), len(first)):
        total += ord(first[index])
elif len(second) > len(first):
    for index in range(len(first)):
        total += ord(first[index]) * ord(second[index])
    for index in range(len(first), len(second)):
        total += ord(second[index])
elif len(first) == len(second):
    for index in range(len(first)):
        total += ord(first[index]) * ord(second[index])
print(total)