class reverse_iter:
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.i = len(self.iter_obj) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 0:
            start = self.iter_obj[self.i]
            self.i -= 1
            return start
        else:
            raise StopIteration()
