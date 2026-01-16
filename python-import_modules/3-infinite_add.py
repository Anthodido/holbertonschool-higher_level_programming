#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = len(argv) - 1
    toto = 0
    for pos in range(1, n + 1):
        toto += int(argv[pos])
    print("{}".format(toto))
