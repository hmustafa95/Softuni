from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name):
        super().__init__(name, capacity=self.CAPACITY)
        self.robots = []

    def details(self):
        result = f"{self.name} Secondary Service:"
        if self.robots:
            result += f"\nRobots: {' '.join(self.robots)}"
        else:
            result += "\nRobots: none"

        return result
