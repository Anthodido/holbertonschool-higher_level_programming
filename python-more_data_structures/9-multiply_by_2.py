#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for key in a_dictionary:
        new_v = a_dictionary[key] * 2
        new[key] = new_v
    return new
