from ..project.baked_food.cake import Cake
from ..project.baked_food.bread import Bread
from ..project.drink.tea import Tea
from ..project.drink.water import Water
from ..project.table.inside_table import InsideTable
from ..project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    def add_food(self, food_type: str, name: str, price: float):
        valid_types = ['Bread', 'Cake']
        if food_type in valid_types:
            for food in self.food_menu:
                if food.name == name:
                    raise Exception(f"{food_type} {name} is already in the menu!")
            if food_type == valid_types[0]:
                new_food = Bread(name, price)
                self.food_menu.append(new_food)
                return f"Added {name} ({food_type}) to the food menu"
            new_food = Cake(name, price)
            self.food_menu.append(new_food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        valid_types = ['Tea', 'Water']
        if drink_type in valid_types:
            for drink in self.drinks_menu:
                if drink.name == name:
                    raise Exception(f"{drink_type} {name} is already in the menu!")
            if drink_type == valid_types[0]:
                new_drink = Tea(name, portion, brand)
                self.drinks_menu.append(new_drink)
                return f"Added {drink_type} ({brand}) to the drink menu"
            new_drink = Water(name, portion, brand)
            self.drinks_menu.append(new_drink)
            return f"Added {drink_type} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        valid_types = ['InsideTable', 'OutsideTable']
        if table_type in valid_types:
            for table in self.tables_repository:
                if table.table_number == table_number:
                    raise Exception(f"Table {table_number} is already in the bakery!")
            if table_type == valid_types[0]:
                new_table = InsideTable(table_number, capacity)
                self.tables_repository.append(new_table)
                return f"Added table number {table_number} in the bakery"
            new_table = OutsideTable(table_number, capacity)
            self.tables_repository.append(new_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved:
                if table.capacity >= number_of_people:
                    table.reserve(number_of_people)
                    return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        try:
            table = next(filter(lambda x: x.table_number == table_number, self.tables_repository))
        except StopIteration:
            return f"Could not find table {table_number}"

        food_not_on_menu = []
        for food in food_names:
            for food_in_menu in self.food_menu:
                if food == food_in_menu.name:
                    table.order_food(food)
            else:
                food_not_on_menu.append(food)

        result = [f'Table {table_number} ordered:']
        for order in table.food_orders:
            result.append(order)
        result.append(f"{self.name} does not have in the menu:")
        for not_in_order in food_not_on_menu:
            result.append(not_in_order)
        return '\n'.join(result)

    def order_drink(self, table_number: int, *drinks_name):
        try:
            table = next(filter(lambda x: x.table_number == table_number, self.tables_repository))
        except StopIteration:
            return f"Could not find table {table_number}"

        drinks_not_on_menu = []
        for drink in drinks_name:
            for drink_in_menu in self.drinks_menu:
                if drink == drink_in_menu.name:
                    table.order_drink(drink)
            else:
                drinks_not_on_menu.append(drink)

        result = [f'Table {table_number} ordered:']
        for order in table.drink_orders:
            result.append(order)
        result.append(f"{self.name} does not have in the menu:")
        for not_in_order in drinks_not_on_menu:
            result.append(not_in_order)
        return '\n'.join(result)

    def leave_table(self, table_number: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                self.total_income += table.get_bill()
                table.clear()
                return f"Table: {table_number}\nBill: {table.get_bill():.2f}"

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            if not table.is_reserved:
                result.append(table.free_table_info())
        return '\n'.join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
