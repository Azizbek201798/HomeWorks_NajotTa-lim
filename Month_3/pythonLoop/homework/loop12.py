import os
os.system("clear")

# DONE

N = int(input("Elementlar sonini kiriting : "))
k, count = None, 0

while N > 0:
    number = float(input("Son = "))
    if k is not None and k != number:
        count += 1
    elif k is None :
        k = number
    N -= 1
print(f"\nElementlar o'zgaruvchanligi = {count}!")