class Car:
    _speed: int
    _color: str
    _is_police: bool

    def __init__(self, color, speed, is_police):
        self._color = color
        self._speed = speed
        self._is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(self._speed)

    def get_speed(self):
        return self._speed

    def get_color(self):
        return self._color

    def get_is_police(self):
        return self._is_police


class TownCar(Car):

    def __init__(self, color, speed=60):
        super().__init__(color, speed, False)

    def go(self):
        super().go()
        if self._speed > 60:
            print("Превышена скорость")


class SportCar(Car):

    def __init__(self, color, speed):
        super().__init__(color, speed, False)


class WorkCar(Car):

    def __init__(self, color, speed):
        super().__init__(color, speed, False)

    def go(self):
        super().go()
        if self._speed > 40:
            print("Превышена скорость")


class PoliceCar(Car):

    def __init__(self, color, speed):
        super().__init__(color, speed, True)


town_car = TownCar("Желтый", 60)
town_car.go()
town_car.stop()
town_car.turn("Влево")
town_car.show_speed()

work_car = WorkCar("Желтый", 60)
work_car.go()
work_car.stop()
work_car.turn("Влево")
work_car.show_speed()

sport_car = SportCar("Желтый", 60)
sport_car.go()
sport_car.stop()
sport_car.turn("Влево")
sport_car.show_speed()

police_car = PoliceCar("Желтый", 60)
police_car.go()
police_car.stop()
police_car.turn("Влево")
police_car.show_speed()
