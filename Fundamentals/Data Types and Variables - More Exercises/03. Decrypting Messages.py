import rsa

key = int(input())
number_of_lines = int(input())
message = ''

for digit in range(number_of_lines):
    letters = input()
    message += letters

decmessage = rsa.decrypt(message, key).decode()

print(f'{decmessage}')
