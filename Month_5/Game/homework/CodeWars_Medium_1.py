# # CodeWars_Medium_1 => Done by Azizbek

# A pangram is a sentence that contains every single letter of the alphabet at least once.
#  For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
# because it uses the letters A-Z at least once (case is irrelevant).
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

import os
os.system("clear")

def is_pangram(soz):
    massiv = []
    for harf in soz:
        if harf.isalpha():
            massiv.append((harf.lower()))
    new_massiv = []
    for x in range(97,123):
        new_massiv.append(chr(x))
    
    for x in massiv:
        if x in new_massiv:
            new_massiv.remove(x)
    
    return True if len(new_massiv) == 0 else False
