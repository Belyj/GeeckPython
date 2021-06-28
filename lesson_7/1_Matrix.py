from random import randrange


class Matrix:

    def __init__(self, list_of_lists: [[]]):
        self.list_of_lists = list_of_lists

    def __str__(self):
        tmp = ''
        i_list = self.list_of_lists
        for i in i_list:
            j_list = i
            tmp += '\n'
            for j in j_list:
                tmp += str(j) + ' '
        return tmp

    def __add__(self, other: 'Matrix'):
        if self.size == other.size:
            for i in range(len(self.list_of_lists)):
                for j in range(len(self.list_of_lists[0])):
                    self.list_of_lists[i][j] += other.list_of_lists[i][j]
        else:
            raise Exception("Matrices sizes must be equals")
        return self

    def add(self, other: 'Matrix'):
        return self.__add__(other)

    def str(self):
        return self.__str__()

    @property
    def size(self):
        return len(self.list_of_lists), len(self.list_of_lists[0])


matrix_1 = Matrix([[randrange(0, 10) for y in range(10)] for x in range(5)])
print(matrix_1)
print("===")
matrix_2 = Matrix([[randrange(0, 10) for y in range(10)] for x in range(5)])
print(matrix_2)
print("===")
print(matrix_2.add(matrix_1))

