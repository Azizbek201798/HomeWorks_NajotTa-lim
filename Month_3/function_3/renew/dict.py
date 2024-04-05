# COMPLATED

import os
os.system("clear")

word = input("So'z kiriting : ").split()
lst = input("List elementlarini kiriting : ").split()

def countWords(soz : list,massiv : list):
    dc = {}
    for x in  range(len(massiv)):
        if massiv[x] in soz:
            dc[massiv[x]] = soz.count(massiv[x])
        else :
            dc[massiv[x]] = 0

    print(dc)

countWords(word,lst)
