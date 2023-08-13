class dictionary_iter:
    def __init__(self, dict_object):
        self.dict_object = list(dict_object.items())
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == len(self.dict_object):
            raise StopIteration
        self.iterations += 1
        return self.dict_object[self.iterations - 1]
