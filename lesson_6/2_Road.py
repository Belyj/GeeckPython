class Road:
    _length: int
    _width: int

    def __init__(self, length=20, width=5000):
        self._length = length
        self._width = width

    def work_calc(self, one_meter_weigh=25, height=5):
        print(
            f"Масса асфальта, необходимая для покрытия всего дорожного полотна {self._length * self._width * one_meter_weigh * height}")


road = Road(2, 5)
road.work_calc()
