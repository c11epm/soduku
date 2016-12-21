from enum import Enum


def get_indicies(enum):
    if enum == Quadrant.lu:
        return (1, 1), (3, 3)
    elif enum == Quadrant.mu:
        return (4, 1), (6, 3)
    elif enum == Quadrant.ru:
        return (7, 1), (9, 3)
    elif enum == Quadrant.lm:
        return (1, 4), (3, 6)
    elif enum == Quadrant.mm:
        return (4, 4), (6, 6)
    elif enum == Quadrant.rm:
        return (7, 4), (9, 6)
    elif enum == Quadrant.ll:
        return (1, 7), (3, 9)
    elif enum == Quadrant.ml:
        return (4, 7), (6, 9)
    elif enum == Quadrant.rl:
        return (7, 7), (9, 9)
    else:
        raise ValueError("No enum matched: " + enum)


def get_quadrant(x, y):
    if 1 <= x <= 3 and 1 <= y <= 3:
        return Quadrant.lu
    elif 4 <= x <= 6 and 1 <= y <= 3:
        return Quadrant.mu
    elif 7 <= x <= 9 and 1 <= y <= 3:
        return Quadrant.ru
    elif 1 <= x <= 3 and 4 <= y <= 6:
        return Quadrant.lm
    elif 4 <= x <= 6 and 4 <= y <= 6:
        return Quadrant.mm
    elif 7 <= x <= 9 and 4 <= y <= 6:
        return Quadrant.rm
    elif 1 <= x <= 3 and 7 <= y <= 9:
        return Quadrant.ll
    elif 4 <= x <= 6 and 7 <= y <= 9:
        return Quadrant.ml
    elif 7 <= x <= 9 and 7 <= y <= 9:
        return Quadrant.rl
    else:
        raise ValueError("X=%d, Y=%d not valid" % (x, y))


class Quadrant(Enum):
    lu = 1
    mu = 2
    ru = 3
    lm = 4
    mm = 5
    rm = 6
    ll = 7
    ml = 8
    rl = 9


class Matrix:
    """
    Please note matrix is 0 indexed, but used as 1 indexed, conversion is needed to be done in this class
    """
    def __init__(self, x, y):
        self._matrix = []
        self._x = x
        self._y = y
        for i in range(x):
            y_list = [0] * y
            self._matrix.append(y_list)

    def __str__(self):
        matrix = ""
        for i in range(self._y):
            for j in range(self._x):
                matrix += str(self._matrix[i][j]) + " "
            matrix += "\n"
        return matrix

    def get_size(self):
        return self._x, self._y

    def set_value_at_index(self, x, y, val):

        if val < 1 or val > 9:
            raise ValueError("val out of bounds")

        if x < 1 or x > 9:
            raise ValueError("X out of bounds")

        if y < 1 or y > 9:
            raise ValueError("Y out of bounds")

        self._matrix[y - 1][x - 1] = val
        #print self.__str__()

    def _check_row(self, row):
        vals = [0] * 9
        for i in range(self._x):
            vals[self._matrix[row][i]] += 1
        return self._validate_array(vals)

    def _check_col(self, col):
        vals = [0] * 9
        for i in range(self._y):
            vals[self._matrix[i][col]] += 1
        return self._validate_array(vals)

    def _check_quad(self, x, y):
        quad = get_quadrant(x, y)
        ind = get_indicies(quad)
        vals = [0] * 9
        

        return self._validate_array(vals)

    def _validate_array(self, arr):
        """
        This should valudate an array, valid array should only consists of zeroes and ones
        :param arr: the array
        :return: boolean if valid
        """
        for i in range(len(arr)):
            if arr[i] > 1:
                return False
        return True
