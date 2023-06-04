received_list = input().split(" ")
numarized_list = [int(a) for a in received_list]
actual_list = list(filter(lambda x: x % 2 == 0, numarized_list))
print(actual_list)
