import io
from sys import argv

from Matrix import Matrix

f = argv


def readfile(path):

    file = open(path, 'r')
    cont = file.readlines()
    list = []

    for line in cont:
        line = line.strip("\n")
        chars = line.split(",")
        for i in range(len(chars)):
            if chars[i] == "":
                chars[i] = '0'
        list.append(chars)
        print chars

    m = Matrix(9, 9)

    for i in range(9):
        for j in range(9):
            if list[i][j] != '0':
                m.set_value_at_index(i + 1, j + 1, int(list[i][j]))
    file.close()

if __name__ == '__main__':
    readfile(f[1])

