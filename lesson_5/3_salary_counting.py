file_name = 'employees_salary.txt'


def low_salary_searching(botom_sum=20000, _file_name=file_name):
    with open(f'./resources/{_file_name}') as file:
        last = file.seek(0, 2)
        file.seek(0, 0)
        underpayed_employees = []
        salaries = []
        while file.tell() != last:
            surname, salary = file.readline().split(' ')
            salaries.append(float(salary))
            if float(salary) < botom_sum:
                underpayed_employees.append(surname)
        print(f'Сотрудники с оплатой ниже {botom_sum}:\n{underpayed_employees}')
        print(f'Средняя величина дохода сотрудников:\n{sum(salaries)/len(salaries)}')


low_salary_searching()
