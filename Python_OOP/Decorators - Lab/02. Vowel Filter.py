def vowel_filter(function):
    vowels = ['A', 'O', 'E', 'I', 'Y', 'U', 'a', 'o', 'e', 'i', 'y', 'u']
    def wrapper():
        result = function()
        vowels_list = []
        for letter in result:
            if letter in vowels:
                vowels_list.append(letter)
        return vowels_list
    return wrapper()

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
