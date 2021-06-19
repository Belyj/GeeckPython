from random import randint
from random import shuffle
from os import path

file_name = 'num_list.txt'


def generate_nums():
    arr = [randint(0, 100) for i in range(randint(0, 100))]
    shuffle(arr)
    return arr


def check_file(path_file):
    if not path.exists(path_file):
        with open(path_file, 'x'):
            print(f'File {path_file} created')


def write_in_file(arr, path_file):
    check_file(path_file)
    with open(path_file, 'w') as file:
        file.seek(0, 0)
        # for i in arr:
        i = 0
        while True:
            file.write(str(arr[i]))
            i += 1
            if i == len(arr):
                break
            file.write(' ')


def counting_file_nums(path_file):
    with open(path_file) as file:
        count = 0
        for i in file.readline().split(' '):
            count += int(i)
        print(count)


def run_generate_sum_nums_in_file(_filename = file_name):
    path_file = f'./resources/{_filename}'
    write_in_file(generate_nums(), path_file)
    counting_file_nums(path_file)

run_generate_sum_nums_in_file()
