class Inventory:
    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        self.items = []
        self.capacity = __capacity

    def add_item(self, item: str):
        if self.capacity > 0:
            self.items.append(item)
            self.capacity -= 1
        else:
            return 'not enough room in the inventory'

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.capacity}"

