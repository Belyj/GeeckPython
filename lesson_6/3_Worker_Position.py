incomes = {
    "wage": 1000,
    "bonus": 6000
}


class Worker:
    name: str
    surname: str
    position = "Рабочий"
    _income: {}

    def __init__(self, name, surname, income):
        self.name = name
        self.surname = surname
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{self._income.get('wage') * 12 + self._income.get('bonus')}"

    def __init__(self, name, surname):
        super().__init__(name, surname, incomes)


position = Position("John", "Doe")
print(position.get_full_name())
print(position.get_total_income())


