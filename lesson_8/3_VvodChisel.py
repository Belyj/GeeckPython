class NotNumException(Exception):
    pass


arr = []
while True:
    str = input('Введите число:\n')
    try:
        if str.isdigit():
            arr.append(str)
        else:
            if str == "stop":
                print(arr)
                exit(0)
            raise NotNumException("Введено не число")
    except NotNumException as e:
        print(e)
