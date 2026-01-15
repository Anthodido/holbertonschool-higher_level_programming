#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord("a") <= ord(ch) <= ord("z"):
            out = chr(ord(ch) - 32)
        else:
            out = ch
        print("{}".format(out), end="")
    print()