book = input()
book_count = 0
current_book = input()

while current_book != 'No More Books':
    if current_book == book:
        break
    book_count += 1
    current_book = input()

if current_book == book:
    print(f'You checked {book_count} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {book_count} books.')
