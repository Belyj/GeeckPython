n = input('Vvedi chislo:\n')

if n.isdigit():
    n = int(n)
    print(n + n * 10 + n + n * 100 + n * 10 + n)
else:
    print('Eto bylo ne chislo')
