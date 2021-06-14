from sys import argv

try:
    file, worked_hours, payment_for_hour, work_prize = argv
except ValueError:
    print('Не правильное количество аргументов')
    exit(0)


def salary_calculating(hours, payment, prize):
    if hours.isdigit():
        if payment.isdigit():
            if prize.isdigit:
                return hours * payment + prize
            else:
                print('Премия должна быть числом')
        else:
            print('Оплата должна быть числом')
    else:
        print('Отработанные часы должны быть числом')


print(salary_calculating(worked_hours, payment_for_hour, work_prize))
