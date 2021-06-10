x = 2
y = -2


def my_func(x, y):
    return x ** y


print(my_func(x, y))


def my__func(x, y):
    temp = 1
    for i in range(y, 0):
        temp = temp/x
    print(temp)


my__func(x, y)