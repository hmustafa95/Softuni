from horse import Horse


class Appaloosa(Horse):
    MAXIMUM_SPEED = 120

    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.is_taken = False

    def take_horse(self):
        if not self.is_taken:
            self.is_taken = True

    def train(self):
        if self.__speed + 2 >= Appaloosa.MAXIMUM_SPEED:
            self.__speed = Appaloosa.MAXIMUM_SPEED
        else:
            self.__speed += 2
