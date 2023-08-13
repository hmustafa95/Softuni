try:
    text_doc = open('C:/Users/thind/OneDrive/Desktop/text.txt', 'r')
    print('File found')
except FileNotFoundError:
    print('File not found')