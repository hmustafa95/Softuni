def vowel_filter(function):
    vowels = 'aoeiuy'

    def wrapper():
        result = function()
        return [x for x in result if x in vowels]
    return wrapper
