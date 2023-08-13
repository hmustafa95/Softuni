received_string = input()
vowels = ['a', 'o', 'u', 'e', 'i']
result = [x for x in received_string if x.lower() not in vowels]
print(''.join(result))
