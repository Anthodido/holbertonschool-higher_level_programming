#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for ch in my_string:
        if ch == "c" or ch == "C":
            pass
        elif ch not in ("c", "C"):
            result += ch
    return result