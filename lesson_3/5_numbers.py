sum = 0

while True:
    str = input('Введите строку чисел через пробел:\n')
    arr = str.split(' ')
    for i in arr:
        if i.isdigit():
            sum += int(i)
        else:
            print(sum)
            exit(0)
    print(sum)