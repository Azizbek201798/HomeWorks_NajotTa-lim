# T5 => DONE by Azizbek

# Function tuzing. String qabul qilsin. Katta harflar sonini va kichik harflarni sonini qaytarsin.
# Input: "Good Luck"
# Output: [2, 6]

import os
os.system("clear")

satr = input("Satr kiriting : ")
ls1 = []

def countLetter(x : str):
    countLower,countUpper = 0,0
    for z in x:
        if z.islower():
            countLower += 1
        elif z.isupper():
            countUpper += 1

    ls1.append(countUpper)
    ls1.append(countLower)

    print(f"Result(upper,lower) = {ls1}")        

countLetter(satr)

