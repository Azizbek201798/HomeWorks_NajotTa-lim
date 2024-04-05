import os
os.system("clear")

massiv = list((12,2,34,5,67,4,98,16,76))

local_min,count,sum = None,0,0

print("Result : ",end = "")
for x in range(1,len(massiv)-1):
    if massiv[x] < massiv[x-1] and massiv[x] < massiv[x+1] and massiv[x] % 2 == 0:
        local_min = massiv[x]
        print(massiv[x],end = " ")
        count += 1
        sum += massiv[x]
if local_min is not None:
    print(f"\nSoni = {count}", end = " , ")
    print(f"Average = {round(sum/count,2)}")
else :
    print("Massiv local minimumga ega emas!")