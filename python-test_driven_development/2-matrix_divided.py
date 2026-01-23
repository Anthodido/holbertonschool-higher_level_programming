#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(div) not in (int, float):
        raise TypeError("div mustbe a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (type(matrix) is not list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for x in row:
            if type(x) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integer/floats")
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    new_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            new_row.append(roud(x / div, 2))
        new_matrix.append(new_row)
    return new_matrix
    