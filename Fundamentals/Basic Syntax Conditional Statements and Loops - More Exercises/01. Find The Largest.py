number = int(input())
number_list = []

for symbol in str(number):
    number_list.append(symbol)

number_list.sort(reverse=True)
print("".join(number_list))
