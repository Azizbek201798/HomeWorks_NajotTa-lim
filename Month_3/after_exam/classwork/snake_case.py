import os
os.system("clear")

def to_case(satr : str):
    for x in range(len(satr)):
        if "_" in satr[x]:
            satr[x+1].upper()
