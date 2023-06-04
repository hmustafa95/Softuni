received_list = input().split(', ')
numarized_list = [int(x) for x in received_list]
indices = map(lambda x: x if numarized_list[x] % 2 == 0 else 'no', range(len(numarized_list)))
even_indices = list(filter(lambda a: a != 'no', indices))
print(even_indices)
