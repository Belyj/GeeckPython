a = input('Vvedi kolichestvo km, skolko probegaet sportsmen v pervyi den\' trenirovok:\n')
percent_per_day = 10
days = 1

if a.isdigit():
    a = int(a)
    b = input('Vvedi, skolko km nuzhno probegat\':\n')
    if b.isdigit():
        b = int(b)
        while a < b:
            a = a + a/10
            days += 1
        print(f'Dnei do pobedy {days}')
    else:
        print('Ty vvel ne chislo')
else:
    print('Ty vvel ne chislo')
