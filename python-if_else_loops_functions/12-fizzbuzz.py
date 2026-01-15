#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        out = i
        if i % 3 == 0 and i % 5 == 0:
            out = "FizzBuzz"
        elif i % 3 == 0:
            out = "Fizz"
        elif i % 5 == 0:
            out = "Buzz"
        print("{out}".format(out=out), end=" ")
