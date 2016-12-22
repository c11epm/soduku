from Matrix import Matrix
from FileReader import readfile
from sys import argv
from time import time

f = argv


def create_matrix(size, data):
    m = Matrix(size, size)

    for i in range(size):
        for j in range(size):
            if data[i][j] != '0':
                m.set_value_at_index(j + 1, i + 1, int(data[i][j]))

    # print m
    return m


def solve_puzzle(puzzle):
    while not puzzle.is_done():
        puzzle.get_possible_values()
        puzzle.update_new_values()


if __name__ == '__main__':
    print "Solving: " + f[1] + " with size: " + f[2]
    content = readfile(f[1])
    puzzle = create_matrix(int(f[2]), content)
    start = time()

    solve_puzzle(puzzle)

    end = time()
    print str(end - start) + " seconds"
