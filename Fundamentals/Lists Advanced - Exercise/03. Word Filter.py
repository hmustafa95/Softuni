received_list = input().split(' ')
result = [x for x in received_list if len(x) % 2 == 0]
print('\n'.join(result))
