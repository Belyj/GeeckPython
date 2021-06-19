file_name = 'file.txt'


def clean(string):
    return string.replace('\n', '')


def file_working(_file_name):
    with open(f'./resources/{file_name}', 'a') as file:
        console_input = '_'
        while console_input != '':
            print(file.tell())
            file.seek(0, 2)
            console_input = input('Введите строку (Пустая строка для выхода):\n')
            # print(file.__sizeof__())
            print(file.tell())
            print(clean(console_input), file=file)


file_working(file_name)
