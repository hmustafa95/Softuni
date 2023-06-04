first_list = input().split(', ')
second_list = input().split(', ')
result = []

for index_first in first_list:
    for index_second in second_list:
        if index_first in index_second:
            result.append(index_first)
            break

print(result)
