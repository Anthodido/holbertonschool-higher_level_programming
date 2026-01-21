#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    m = sorted(a_dictionary, key=a_dictionary, reverse=True)
    return m 