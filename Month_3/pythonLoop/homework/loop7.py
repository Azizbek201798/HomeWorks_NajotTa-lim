import os
os.system("clear")

#DONE

N = int(input("Elementlar sonini kiriting : "))
min = None
while N > 0:
    number = float(input("HaqiqiySon = "))
    if min == None and number > 20:
        min = number
    if min is not None and min > number and number > 20:
        min = number
    N -=1
print(f"{min} - 20 dan katta eng kichik son")
