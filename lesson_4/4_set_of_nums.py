from random import randint

arr = [randint(0, 100) for i in range(randint(0, 100))]
print('Исходный массив')
print(arr)


def set_of(c_list=[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]):
    temp = []
    for i in range(0, len(c_list)):
        if c_list.count(c_list[i]) == 1:
            temp.append(c_list[i])
    return temp


print('Результат')
print(set_of(arr))
