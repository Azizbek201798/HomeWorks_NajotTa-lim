

# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.
# Example:# Task - 2 => CodeWars_Medium_1
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

import os
os.system("clear")

def alphabet_position(matn):
    matn = matn.lower()
    
    positions = []
    
    for char in matn:
        if char.isalpha():
            position = ord(char) - ord('a') + 1
            positions.append(str(position))
    
    result = ' '.join(positions)
    
    return result

print(alphabet_position("The sunset sets at twelve o' clock."))
