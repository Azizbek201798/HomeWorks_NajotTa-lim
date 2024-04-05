import os
os.system("clear")

f = open("satr.txt","at+")
f.seek(0)
data = f.read()
number,summa = "",0

for x in data:
    if x.isdigit():
        number += x
    else :
        if len(number) != 0:
            summa += int(number)
            number = ""
f.write(f"\nSummaNumbers = {summa}")
