from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name):
        super().__init__(name, capacity=self.CAPACITY)
        self.robots = []

    def details(self):
        result = f"{self.name} Main Service:"
        if self.robots:
            result += f"\nRobots: {' '.join(self.robots)}"
        else:
            result += "\nRobots: none"

        return result
