import os
os.system("clear")

# DONE

K = int(input("K = "))
sum = 0
for i in range(1,K):
    if i % 4 != 0:
        sum += i
print("1 dan K gacha 4 ga karrali bo'lmagan sonlar yig'indisi = {}".format(sum))