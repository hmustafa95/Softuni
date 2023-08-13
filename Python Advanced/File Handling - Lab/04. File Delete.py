import os

try:
    os.remove('C:/Users/thind/OneDrive/Desktop/my_first_file.txt')
except FileNotFoundError:
    print('File already deleted!')