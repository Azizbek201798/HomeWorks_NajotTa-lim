# CodeWars_Medium_3 => DONE BY Azizbek;

# Write a function that takes in a string of one or more words, and returns the same string, 
# but with all words that have five or more letters reversed (Just like the name of this Kata). 
# Strings passed in will consist of only letters and spaces. Spaces will be included only when 
# more than one word is present.

# Examples:

# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"

import os
os.system("clear")

def spin_words(sentence):
    sentence = sentence.split()
    natija = []

    # Uzunligi 5 dan katta bo'lgan so'zlarni reverse qilish;
    for x in sentence:
        if len(x) >= 5:
            natija.append(x[::-1])
        else:
            natija.append(x)
    return (" ").join(natija)

print(spin_words("This is another test"))