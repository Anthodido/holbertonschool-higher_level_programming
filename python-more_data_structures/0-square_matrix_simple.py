#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        new_r = []
        for y in i:
            new_v = y * y
            new_r.append(new_v)
        new.append(new_r)
    return new
