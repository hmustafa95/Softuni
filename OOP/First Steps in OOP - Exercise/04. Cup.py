class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, mils):
        if self.quantity + mils <= self.size:
            self.quantity += mils

    def status(self):
        return self.size - self.quantity
