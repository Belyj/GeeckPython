from itertools import count
from itertools import cycle


def iter_count(start=3, end=10):
    arr_ = []
    for i in count(start):
        if i == end:
            return arr_
        arr_.append(i)


arr = iter_count()

print(arr)


def iter_cycle(arr_, times=10):
    i = 0
    for x in cycle(arr_):
        print(x)
        i += 1
        if i == times:
            exit(0)


iter_cycle(arr)
