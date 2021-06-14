def fact(n):
    if n == 0 or n == 1:
        return 1
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


def gen_fact(n):
    for el in fact(n):
        yield el


a = gen_fact(4)
print(a)
