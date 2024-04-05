import os
os.system("clear")

# DONE

N1,N2 = map(int,input("N1,N2 = ").split())
mult,count = 1,0
while N2 > N1:
    if N2 % 5 != 0:
        mult *= N2
        count += 1 
    N2 -= 1
    if count == 3:
        print("N1 dan N2 gacha ohirgi 3ta 5 ga bo'linmaydigan sonlar ko'paytmasi = {}".format(mult))

    
