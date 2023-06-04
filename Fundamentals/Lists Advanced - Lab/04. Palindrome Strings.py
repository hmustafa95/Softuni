def palindrome(any_list):
    result = []
    for word in any_list:
        if word == word[::-1]:
            result.append(word)
    return result

given_list = input().split(' ')
given_word = input()

result = palindrome(given_list)
print(result)

counter = 0
for current_index in result:
    if current_index == given_word:
        counter += 1

print(f'Found palindrome {counter} times')
