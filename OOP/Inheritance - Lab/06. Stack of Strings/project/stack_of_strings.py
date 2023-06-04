class Stack:
    def __init__(self, data: list):
        self.data = list(data)

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if len(self.data) > 0:
            pop_data = self.data.pop()
            return pop_data

    def top(self):
        if len(self.data) > 0:
            return self.data[-1]

    def is_empty(self):
        if len(self.data) == 0:
            return True
        if len(self.data) > 0:
            return False

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"