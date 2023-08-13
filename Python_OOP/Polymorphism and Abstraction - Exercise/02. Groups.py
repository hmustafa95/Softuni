class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        name = f"{self.name} {self.surname}"
        return name

    def __add__(self, other):
        name = f"{self.name} {other.surname}"
        return name


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        name = f'{self.name} {other.name}'
        people = self.people + other.people
        return Group(name, people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(str(x) for x in self.people)}"

    def __getitem__(self, item):
        return f"Person {item}: {self.people[item]}"

