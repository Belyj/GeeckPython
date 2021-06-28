from abc import ABC, abstractmethod


class Clothes(ABC):
    _name: str

    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):
    _size: int

    def __init__(self, name: str, size: int):
        self._size = size
        super().__init__(name)

    @property
    def calculate(self):
        return self._size/6.5 + 0.5


class Suit(Clothes):
    _height: int

    def __init__(self, name: str, height: int):
        self._height = height
        super().__init__(name)

    @property
    def calculate(self):
        return 2*self._height + 0.3

coat = Coat("As", 30)
print(coat.calculate)
suit = Suit("asd", 30)
print(suit.calculate)
