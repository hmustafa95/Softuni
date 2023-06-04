def palindrome_numbers(a):
    return a == a[::-1]

received_list = input().split(", ")

for current_index in received_list:
    if palindrome_numbers(current_index):
        print("True")
    else:
        print("False")
