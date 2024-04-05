import os
os.system("clear")

#DONE

N = int(input("N = "))
count,sum = 0,0
print("Bular = ",end = "")
for x in range(N,0,-1):
    if x % 4 == 0:
        print("{}".format(x),end = " | ")
        count += 1
        sum += x
    if count == 3 :
        break
print("\n4 ga karrali ohirgi 3 ta sonlar yig'indisi = {}".format(sum))