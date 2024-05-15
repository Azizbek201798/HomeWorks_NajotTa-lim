import os
os.system("clear")

N = int(input("N = "))
M = int(input("M = "))

def islands(N,M):
    massiv = []
    massiv_indx = []
    count = 0
    for x in range(N):
        ls = []
        indx = []
        for y in range(M):
            k = int(input("1 yoki 0 kiriting: "))
            if k == 1:
                indx.append(y)
            ls.append(k)
        os.system("clear")
        massiv.append(ls)
        massiv_indx.append(indx)
                
    for x in range(1,len(massiv_indx)):
        i = 0
        while len(x) > 0:
            count += 1
            i += 1
    # print(massiv_indx)

islands(N,M)

# res = islands(N,M)
# print(res)

# 0 1 2 3 4
# 0 1 2 3 4
# 0 1 2 3 4
# 0 1 2 3 4
