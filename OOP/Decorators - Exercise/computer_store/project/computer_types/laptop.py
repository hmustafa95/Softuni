from math import log2

from computer import Computer


class Laptop(Computer):
    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        valid_processors = {'AMD Ryzen 9 5950X': 900, 'Intel Core i9-11900H': 1050, 'Apple M1 Pro': 1200}
        if processor not in valid_processors:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!!")
        if ram < 2 or ram > 64 or ram % 2 != 0:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")
        self.price = valid_processors[processor] + int(log2(ram)) * 100
        self.processor = processor
        self.ram = ram
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."
