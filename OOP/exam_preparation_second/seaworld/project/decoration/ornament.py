from OOP.exam_preparation_second.seaworld.project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    def __init__(self):
        super().__init__(comfort=1, price=5)
