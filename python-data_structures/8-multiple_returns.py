#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    first = ""
    if not l:
        first = None
    else:
        first = sentence[0]
    return (l, first)
