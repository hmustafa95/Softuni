from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    FEMALEROBOT_WEIGHT = 7

    def __init__(self, name, kind, price):
        super().__init__(name, kind, price, weight=self.FEMALEROBOT_WEIGHT)

    def eating(self):
        self.weight += 1
