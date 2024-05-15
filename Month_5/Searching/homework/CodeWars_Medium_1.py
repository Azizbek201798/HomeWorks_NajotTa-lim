# CodeWars_Medium_1 => DONE by Azizbek

# Once upon a time, on a way through the old wild mountainous west,…
# … a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

# Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!
# How I crossed a mountainous desert the smart way.
# The directions given to the man are, for example, the following (depending on the language):

# ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
# or
# { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
# or
# [North, South, South, East, West, North, West]

import os
os.system("clear")

def dirReduc (arr : list) -> list:
    qarama_qarshi = {"NORTH": "SOUTH", "SOUTH": "NORTH", "WEST" : "EAST", "EAST": "WEST"}
    massiv = []
    
    for i in arr:
        if len(massiv) == 0 or massiv[-1] != qarama_qarshi[i]: 
            massiv.append(i)
            continue
        massiv.pop()
    return massiv
