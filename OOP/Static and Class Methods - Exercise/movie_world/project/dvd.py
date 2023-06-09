import calendar


class DVD:
    def __init__(self, name: str, id_number: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id_number
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id_number: int, name: str, date: str, age_restriction: int):
        day, month, year = date.split('.')
        month = calendar.month_name[int(month)]
        return cls(name, id_number, int(year), month, age_restriction)

    def __repr__(self):
        status = ''
        if self.is_rented:
            status = 'rented'
        else:
            status = 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"
