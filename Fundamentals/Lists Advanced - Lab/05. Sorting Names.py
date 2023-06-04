received_list = input().split(', ')
sorted_list = sorted(received_list, key=lambda x: (-len(x), x))
print(sorted_list)
