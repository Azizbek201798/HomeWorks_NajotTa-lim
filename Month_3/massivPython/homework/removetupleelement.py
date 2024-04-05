import os
os.system("clear")
ls = []
n = int(input("Elementlar sonini kiriting : "))

for x in range(n):
    r = tuple(map(int,input("Elementlarni kiriting : ").split()))
    ls.append(r)
print(ls)

index,maxl = 0,len(ls[0])

for z in range(len(ls)):
    if len(ls[z]) > maxl:
        index = z
print(f"Elementlari eng ko'pi {ls[index]}")

