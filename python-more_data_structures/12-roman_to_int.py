#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    values = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    total = 0
    n = len(roman_string)

    for i in range(n):
        val = values.get(roman_string[i], 0)

        if i + 1 < n:
            next_val = values.get(roman_string[i + 1], 0)
            if val < next_val:
                total -= val
            else:
                total += val
        else:
            total += val

    return total
