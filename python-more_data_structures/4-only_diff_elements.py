#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    s = set()
    for i in set_1:
        if i not in set_2:
            s.add(i)
    for y in set_2:
        if y not in set_1:
            s.add(y)
    return s
