class Cell:
    _cells: int

    def __init__(self, cells):
        self._cells = cells

    def __add__(self, other):
        return Cell(self._cells + other._cells)

    def add(self, other: 'Cell'):
        return self.__add__(other)

    def __sub__(self, other):
        sub = self._cells - other._cells
        if sub > 0:
            return Cell(sub)
        else:
            raise Exception("Sub must be > 0")

    def sub(self, other: 'Cell'):
        return self.__sub__(other)

    def __mul__(self, other):
        return Cell(self._cells * other._cells)

    def mul(self, other: 'Cell'):
        return self.__mul__(other)

    def __truediv__(self, other):
        return Cell(self._cells / other._cells)

    def truediv(self, other: 'Cell'):
        return self.__truediv__(other)

    def make_order(self, count = 5):
        string = ""
        for i in range(0, int(self._cells)):
            count -= 1
            string += "*"
            if count == 0:
                string += "\n"
                count = 5
        return string


cell_1 = Cell(10)
cell_2 = Cell(5)

cell_3 = cell_1.add(cell_2)
print(cell_3._cells)
print(cell_3.make_order())
