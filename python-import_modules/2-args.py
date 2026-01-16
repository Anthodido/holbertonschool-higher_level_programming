#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = len(argv) - 1
    if i == 0:
        print("{0} arguments.".format(i))
    elif i == 1:
        print("{0} argument:".format(i))
    else:
        print("{i} arguments:".format(i=i))
    for pos in range(1, i + 1):
        print("{}: {}".format(pos, argv[pos]))
