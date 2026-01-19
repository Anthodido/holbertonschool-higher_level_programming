#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for y in range(len(i)):
            if y == len(i) - 1:
                end= ""
            else:
                end= " "
            print("{:d}".format(i[y]), end=end)
        print()
        