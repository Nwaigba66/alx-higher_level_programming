def roman_to_int(roman_string):
    from functools import reduce
    rd = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if not roman_string or not isinstance(roman_string, str):
        return 0

    match_val = list(map(lambda x: rd.get(x, 0), list(roman_string.upper())))
    i, j = 0, 1
    while j < len(match_val):
        if match_val[i] < match_val[j]:
            match_val[i] *= -1
        i += 1
        j += 1
    return reduce(lambda x, y: x + y, match_val)
