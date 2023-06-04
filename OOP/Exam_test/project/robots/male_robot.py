from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    MALEROBOT_WEIGHT = 9

    def __init__(self, name, kind, price):
        super().__init__(name, kind, price, weight=self.MALEROBOT_WEIGHT)

    def eating(self):
        self.weight += 3
