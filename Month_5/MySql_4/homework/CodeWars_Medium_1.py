# CodeWars_Medium_1 => DONE BY Azizbek;

# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

import os
os.system("clear")

def move_zeros(massiv):

    count = 0
    new_massiv = []

    for x in massiv:
        if x == 0:
            count += 1
            continue
        new_massiv.append(x)

    for x in range(count):
        new_massiv.append(0)

    return new_massiv