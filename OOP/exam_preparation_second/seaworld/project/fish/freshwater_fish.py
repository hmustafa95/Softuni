from OOP.exam_preparation_second.seaworld.project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    def __init__(self, name, species, price):
        self.size = 3
        super().__init__(name, species, self.size, price)

    def eat(self):
        self.size += 3
