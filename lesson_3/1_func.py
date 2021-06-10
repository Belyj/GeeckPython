a = None
b = None


def dev(a, b):
    if b == 0:
        return 'Делить на ноль нельзя'
    return a/b


a = input("Введите делимое:\n")
if a.isdigit():
    b = input("Введите делитель:\n")
    if b.isdigit():
        print(dev(int(a), int(b)))
    else:
        print('Введено не число')
else:
    print('Введено не число')


def fff():
    print(a)
