file_name = 'lorem_ipsum.txt'


def counting(_file_name):
    raws = 0
    words = 0
    with open(f'./resources/{_file_name}') as file:
        last = file.seek(0, 2)
        file.seek(0, 0)
        while file.tell() != last:
            words += len(file.readline().split(' '))
            raws += 1
    return raws, words


def run_counting():
    raws, words = counting(file_name)
    print(f'Количество строк в файле = {raws}\nКоличество слов в файле = {words}')


run_counting()
