#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    keyword = 0
    prev_value = 0
    for rs in reversed(roman_string):

        if rs not in rom_n:
            return 0

        value = rom_n[rs]

        if value < prev_value:
            keyword -= value
        else:
            keyword += value
        prev_value = value
    return (keyword)
