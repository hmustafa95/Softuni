from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        valid_services = ['MainService', 'SecondaryService']
        if service_type not in valid_services:
            raise Exception("Invalid service type!")

        if service_type == 'MainService':
            self.services.append(MainService(name))
        elif service_type == 'SecondaryService':
            self.services.append(SecondaryService(name))

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        valid_robots = ['MaleRobot', 'FemaleRobot']
        if robot_type not in valid_robots:
            raise Exception("Invalid robot type!")

        if robot_type == 'MaleRobot':
            self.robots.append(MaleRobot(name, kind, price))
        elif robot_type == 'FemaleRobot':
            self.robots.append(FemaleRobot(name, kind, price))

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [x for x in self.robots if x.name == robot_name]
        service = [y for y in self.services if y.name == service_name]

        if robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ == "SecondaryService":
            return "Unsuitable service."

        if robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ == "MainService":
            return "Unsuitable service."

        if service.capacity < robot.weight:
            return "Not enough capacity for this robot!"

        service.robots.append(robot)
        self.robots.remove(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = [y for y in self.services if y.name == service_name]
        flag = False
        robot = object

        for x in service.robots:
            if x.name == robot_name:
                flag = True
                robot = x

        if not flag:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = [y for y in self.services if y.name == service_name]
        counter = 0

        for robot in service.robots:
            counter += 1
            robot.eating()

        return f"Robots fed: {counter}."

    def service_price(self, service_name: str):
        service = [y for y in self.services if y.name == service_name]
        total_price = 0

        for robot in service.robots:
            total_price += robot.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = ''
        for service in self.services:
            result += service.details() + '\n'
