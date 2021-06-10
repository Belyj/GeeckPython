income = input('Vvedi vyruchku:\n')
employee_count = 0

if income.isdigit():
    income = int(income)
    outcome = input('Vvedi izderzhki:\n')
    if outcome.isdigit():
        outcome = int(outcome)
        if income - outcome > 0:
            print('Kompanya rabotaet s pribylu')
            print(f'Rentabelnost bisnesa = {income/outcome}')
            employee_count = input('Vvedi kolichestvo sotrudnikov:\n')
            if employee_count.isdigit():
                print(f'Pribl\' na odnogo sotrudnika = {(income - outcome)/int(employee_count)}')
        elif income - outcome < 0:
            print('Kompania rabotaet s ubytkom')
        else:
            print('Kompania rabotaet v nol\'')
    else:
        print('Ty vvel ne chislo')
else:
    print('Ty vvel ne chislo')
