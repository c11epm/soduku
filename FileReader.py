import io
from sys import argv
import pprint
from Matrix import Matrix

f = argv


def readfile(path):

    file = open(path, 'r')
    cont = file.readlines()
    list = []

    for line in cont:
        line = line.strip("\n")
        if "," in line:
            chars = line.split(",")
            for i in range(len(chars)):
                if chars[i] == "":
                    chars[i] = '0'
            list.append(chars)
        else:
            list.append(line)


    m = Matrix(9, 9)

    for i in range(9):
        for j in range(9):
            if list[i][j] != '0':
                m.set_value_at_index(j + 1, i + 1, int(list[i][j]))
    file.close()
    print m
    while not m.is_done():
        m.get_possible_values()
        m.update_new_values()
        print m


if __name__ == '__main__':
    readfile(f[1])

