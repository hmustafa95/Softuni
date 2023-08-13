text_doc = open('C:/Users/thind/OneDrive/Desktop/text.txt')
sum_numbers = 0
for number in text_doc:
    sum_numbers += int(number)
print(sum_numbers)