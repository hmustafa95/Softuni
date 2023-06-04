from project.client import Client
from project.meals.starter import Starter
from project.meals.main_dish import MainDish
from project.meals.dessert import Dessert


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        dishes = ["Starter", "MainDish", "Dessert"]
        for meal in meals:
            if type(meal).__name__ in dishes:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        result = []
        for meal in self.menu:
            result.append(meal.details())
        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        try:
            client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list))
        except StopIteration:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        meals = []
        for meal in self.menu:
            meals.append(meal.name)

        for meal_requested in meal_names_and_quantities:
            if meal_requested not in meals:
                raise Exception(f"{meal_requested} is not on the menu!")

        quantities_available = {}
        for meal in self.menu:
            if meal not in quantities_available:
                quantities_available[meal.name] = 0
            quantities_available[meal.name] = meal.quantity

        for k, v in meal_names_and_quantities.items():
            if quantities_available[k] < v:
                for type_meal in self.menu:
                    if type_meal.name == k:
                        meal_type = type_meal
                raise Exception(f"Not enough quantity of {meal_type.__class__.__name__}: {k}!")

        meal_names = []
        for k, v in meal_names_and_quantities.items():
            meal_names.append(k)
            if quantities_available[k] < v:
                for type_meal in self.menu:
                    if type_meal.name == k:
                        meal_type = type_meal
                        food = meal_type.__class__(k, v)
                        client.shopping_cart.append(food)
                        self.menu[type_meal.quantity] -= v

        for item in client.shopping_cart:
            client.bill += item.quantity * item.price

        return f"Client {client_phone_number} successfully ordered {', '.join(meal_names)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        try:
            client = next(filter(lambda x: x.phone_number == client_phone_number, self.clients_list))
        except StopIteration:
            raise Exception("There are no ordered meals!")

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

    def finish_order(self):
        pass

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
