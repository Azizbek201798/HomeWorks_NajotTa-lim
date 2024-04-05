# T15 => DONE by Azizbek

# List ichida berilgan strlarni leni boyicha sortladigan funktsiya yozing.
# Input:
# ["Tarvuz" , "Nok", "Olma"]
# Output:
# ["Nok", "Olma", "Tarvuz"]

import os
os.system("clear")

ls1 = list(map(str,input("List elementlarini kiriting : ").split()))

def sortStr(k : list):
    print(f"Input  : {k}")
    for x in range(len(k)):
        for y in range(1,len(k)):
            if len(k[y-1]) >= len(k[y]):
                k[y-1],k[y] = k[y],k[y-1]

    print(f"Output : {k}")

os.system("clear")
sortStr(ls1)
