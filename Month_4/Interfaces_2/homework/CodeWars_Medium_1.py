# CodeWars_Medium_1 => DONE by Azizbek

# In this kata, you will have to return the continued fractionwiki of a fraction.
# For example, if the numerator is 311 and the denominator is 144, then you would have to return [2, 6, 3, 1, 5], because: 
# If the numerator is 0, you should return [].

import os
os.system("clear")

def continued_fraction(bolinuvchi: int, boluvchi: int) -> list[int]:
    if bolinuvchi == 0:
        return []

    result = []
    while boluvchi != 0:
        integer_part = bolinuvchi // boluvchi
        result.append(integer_part)
        bolinuvchi, boluvchi = boluvchi, bolinuvchi % boluvchi

    return result