def int_func(word):
    word = word.capitalize()
    return word


def word_cap(str):
    cap_str = ''
    for i in str.split(' '):
        cap_str = cap_str + int_func(i) + ' '
    return cap_str


print(word_cap('text text text'))