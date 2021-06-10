n = input('Vvedi tseloe polozhitelnoe chislo:\n')
max = 0

if n.isdigit():
    n = int(n)
    while n != 0:
        if n % 10 > max:
            max = n % 10
        n = n // 10
    print(max)
else:
    print('ne tseloe polozhitelnoe chislo')
