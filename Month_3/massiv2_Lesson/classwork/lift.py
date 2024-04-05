import os 
os.system("clear")

mx = [[1,4,3,2],[1,10,2],["-"],[3,6,4,5,6],["-"],["-"],[0,0,0],["-"],[4],[6,5,2],["-"]]

for x in range(len(mx)):
    for y in range(len(mx[x])):
        if mx[x][y] == mx[x]:
            mx.remove(mx[x])

for x in range(len(mx)):
    for y in range(len(mx[x])):
        print(mx[x][y], end = "   ")
    print("")

