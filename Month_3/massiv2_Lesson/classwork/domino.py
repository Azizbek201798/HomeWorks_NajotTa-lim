import os
os.system("clear")

domino = []
for x in range(7):
    for y in range(x,7):
        domino.append([x,y])
print(domino)
ls = [[1,1],[5,6],[6,6],[0,6],[0,0],[2,2]]

print("\n\nResult : ")
for k in domino:
    if ls.count(k) == 0 and ls.count(k) == 0:
            print(k,end = " | ")
