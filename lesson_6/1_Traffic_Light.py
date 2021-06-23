import time

color_data = {
    "Красрный": 7,
    "Желтый": 2,
    "Зеленый": 7
}


class TrafficLight:
    __color: str

    def running(self):
        for i in color_data:
            print(i)
            time.sleep(color_data.get(i))


traffic_light = TrafficLight()
traffic_light.running()
