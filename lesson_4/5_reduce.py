from functools import reduce
arr = [x for x in range(100, 1001) if x % 2 == 0]

print(reduce(lambda x, y: x*y, arr))
