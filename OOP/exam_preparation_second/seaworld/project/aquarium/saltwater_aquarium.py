from OOP.exam_preparation_second.seaworld.project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    def __init__(self, name):
        super().__init__(name, capacity=25)
