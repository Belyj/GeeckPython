file_name = 'num.txt'
localize_file = 'числа.txt'
local_nums = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}


def run_localize(_file_name=file_name):
    with open(f'./resources/{_file_name}') as file:
        last = file.seek(0, 2)
        file.seek(0, 0)
        raws = []
        while file.tell() != last:
            raw = file.readline().replace('\n', '')
            target = raw.split(' ')[0]
            raw = raw.replace(target, local_nums.get(target))
            raws.append(raw)
            print(raw)
    return raws


def write_raws_in_localie_file(raws, _file_name):
    with open(f'./resources/{_file_name}', 'a') as file:
        for i in raws:
            file.write(i + '\n')


raws = run_localize()
write_raws_in_localie_file(raws, localize_file)
