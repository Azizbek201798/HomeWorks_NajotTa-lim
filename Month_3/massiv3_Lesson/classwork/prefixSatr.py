import os
os.system("clear")

satr = input("Satr kiriting : ")
k = set()

for x in range(len(satr)):
    prefix = satr[:(x+1)]
    k.add(prefix)
print(k)
print(len(k))