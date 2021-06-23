class Stationary:
    __title: str

    def draw(self):
        print("Запуск отрисовки")

    def __init__(self, title):
        self._title = title

    def get_title(self):
        return self._title


class Pen(Stationary):

    def draw(self):
        super().draw()
        print(f"Рисую с как {self.get_title()}")

    def __init__(self):
        super().__init__("Ручка")


class Pencil(Stationary):
    def draw(self):
        super().draw()
        print(f"Рисую с как {self.get_title()}")

    def __init__(self):
        super().__init__("Карандаш")


class Handle(Stationary):
    def draw(self):
        super().draw()
        print(f"Рисую с как {self.get_title()}")

    def __init__(self):
        super().__init__("Маркер")


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
