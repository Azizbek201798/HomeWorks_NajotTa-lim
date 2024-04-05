import os
os.system("clear")

parol,summa = input(),0
for x in parol:
    summa += int(x)

if len(parol) == 9 and not parol.startswith("0") and summa % 2:
    print("yes")
else :
    print("no")

# EXCEPTED 100%
    