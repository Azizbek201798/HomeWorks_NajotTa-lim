# COMPLATED

import os
os.system("clear")

word = list(map(str,input("So'zlarni kiriting :").split()))

def convertLeftToRight(ls : list):
    wordNew = map(lambda x : x.replace("left","right"),ls)
    result = ",".join(wordNew)
    print(result)

convertLeftToRight(word)

