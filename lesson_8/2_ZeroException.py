class ZeroDelimiterException(ZeroDivisionError):
    pass


class Delimiter:

    @staticmethod
    def divide(divisible: int, delimiter: int):
        try:
            if delimiter == 0:
                raise ZeroDelimiterException("На ноль делить нельзя")
            print(divisible / delimiter)
        except ZeroDivisionError as e:
            print(e)


Delimiter.divide(10, 1)
