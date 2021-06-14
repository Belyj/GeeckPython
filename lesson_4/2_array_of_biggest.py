from random import randint
from random import shuffle


arr = [x for x in range(0, randint(1, 1000))]
shuffle(arr)

print('Исходный список')
print(arr)


def biggest_arr(c_list=[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]):
    b_list = []
    for i in range(1, len(c_list)):
        if c_list[i] > c_list[i - 1]:
            b_list.append(c_list[i])
    return b_list


print('Результат')
print(biggest_arr(arr))
