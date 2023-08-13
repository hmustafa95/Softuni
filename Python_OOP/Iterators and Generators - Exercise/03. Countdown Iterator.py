class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == -1:
            raise StopIteration
        self.count -= 1
        return self.count + 1
