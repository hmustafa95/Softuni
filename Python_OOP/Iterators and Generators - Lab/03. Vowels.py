class vowels:
    VOWELS = 'AOEIYUaoeiyu'

    def __init__(self, text):
        self.text = text
        self.vowels = [el for el in self.text if el in vowels.VOWELS]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.vowels:
            raise StopIteration

        return self.vowels.pop(0)
