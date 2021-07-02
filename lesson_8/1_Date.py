_big_month_data = (1, 3, 5, 7, 8, 10, 12)
_moth_data = {
    1: "Января",
    2: "Февраля",
    3: "Марта",
    4: "Апрел",
    5: "Мая",
    6: "Июня",
    7: "Июля",
    8: "Августа",
    9: "Сентября",
    10: "Октября",
    11: "Ноября",
    12: "Декабря",
}


class Date:
    _date: str

    def __init__(self, date: str):
        self._date = date
        Date._validation(date)

    @classmethod
    def _date_separate(cls, date: str):
        arr = date.split("-")
        return int(arr[0]), int(arr[1]), int(arr[2])

    @staticmethod
    def _validation(date: str):
        day, month, year = Date._date_separate(date)
        if 1 > month or 13 < month:
            raise Exception("Месяц должен быть в диапазоне от 1 до 12")
        if day < 1:
            raise Exception("День не может быть меньше одного")
        if _big_month_data.__contains__(month) and day > 31:
            raise Exception(f"День {_moth_data.get(month)} должен быть меньше 32")
        elif month == 2 and day > 29:
            raise Exception(f"День {_moth_data.get(month)} должен быть меньше 30")
        elif day > 30:
            raise Exception(f"День {_moth_data.get(month)} должен быть меньше 31")


date = Date("01-01-1970")
