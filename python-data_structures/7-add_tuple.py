#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tA = tuple_a + (0, 0)
    tA = tA[:2]
    a0 = tA[0]
    a1 = tA[1]
    tB = tuple_b + (0, 0)
    tB = tB[:2]
    b0 = tB[0]
    b1 = tB[1]
    som1 = a0 + b0
    som2 = a1 + b1
    return (som1, som2)
