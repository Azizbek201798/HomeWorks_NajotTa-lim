import os
os.system("clear")

word = input("Satrni kiriting : ")
res = word.split()
for x in range(len(res) - 1):
    for y in range(x+1,len(res)):
        if res[x] > res[y]:
            res[x],res[y] = res[y],res[x]
for k in res:
    print(k)


    