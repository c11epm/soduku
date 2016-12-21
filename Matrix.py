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
            print self._matrix

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

        self._matrix[x - 1][y - 1] = val
        print self.__str__()
