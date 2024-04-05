import os
os.system("clear")

massiv = []

n = int(input("Elementlar sonini kiriting : "))

while n > 0 :
    tp = tuple(map(int,input("Tuple kiriting : ").split()))
    massiv.append(tp)
    n -= 1

print(massiv)