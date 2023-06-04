from computer_types.desktop_computer import DesktopComputer
from computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        valid_computers = ["Desktop Computer", "Laptop"]
        if type_computer not in valid_computers:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        if type_computer == valid_computers[0]:
            pc = DesktopComputer(manufacturer, model)
            pc.configure_computer(processor, ram)
            self.warehouse.append(pc)
            return pc.configure_computer(processor, ram)
        elif type_computer == valid_computers[1]:
            pc = Laptop(manufacturer, model)
            pc.configure_computer(processor, ram)
            self.warehouse.append(pc)
            return pc.configure_computer(processor, ram)

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.processor == wanted_processor and computer.ram >= wanted_ram:
                self.profits += (client_budget - computer.price)
                self.warehouse.remove(computer)
                return f"{computer} sold for {client_budget}$."
        raise Exception("Sorry, we don't have a computer for you.")

