from abc import ABC


class OfficeEquipment(ABC):
    _name: str
    _width: int
    _length: int
    _height: int

    def __init__(self, name, width, length, height):
        self._name = name
        self._width = width
        self._length = length
        self._height = height

    def get_volume(self):
        return self._width * self._length * self._height

    def get_name(self):
        return self._name


class Printer(OfficeEquipment):

    def __init__(self, name: str = "Принтер", width: int = 30, length: int = 50, height: int = 20):
        super().__init__(name, width, length, height)


class Scanner(OfficeEquipment):

    def __init__(self, name: str = "Сканер", width: int = 50, length: int = 50, height: int = 60):
        super().__init__(name, width, length, height)


class Copier(OfficeEquipment):

    def __init__(self, name: str = "Ксерокс", width: int = 100, length: int = 50, height: int = 40):
        super().__init__(name, width, length, height)


class Store:
    _store: []
    _capacity: int

    def __init__(self, capacity: int = 300000):
        self._store = []
        self._capacity = capacity

    def store(self, equipment: OfficeEquipment):
        try:
            if equipment.get_volume() < self._capacity:
                self._store.append(equipment)
                self._capacity -= equipment.get_volume()
                print(f"Equipment {equipment.get_name()} stored, there is {self._capacity} more capacity")
            else:
                raise Exception(
                    f"Not enough capacity [{self._capacity}] for {equipment.get_name()} [{equipment.get_volume()}]")
        except Exception as e:
            print(e)


store = Store()
printer = Printer()
scanner = Scanner()
copier = Copier()
store.store(printer)
store.store(scanner)
store.store(copier)
