from horse import Horse


class Thoroughbred(Horse):
    MAXIMUM_SPEED = 140

    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.is_taken = False

    def take_horse(self):
        if not self.is_taken:
            self.is_taken = True

    def train(self):
        if self.__speed + 3 >= Thoroughbred.MAXIMUM_SPEED:
            self.__speed = Thoroughbred.MAXIMUM_SPEED
        else:
            self.__speed += 3
