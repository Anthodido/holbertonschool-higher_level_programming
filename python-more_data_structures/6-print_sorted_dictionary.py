#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = sorted(a_dictionary)
    for i in key:
        print("{}: {}".format(i, a_dictionary[i]))
