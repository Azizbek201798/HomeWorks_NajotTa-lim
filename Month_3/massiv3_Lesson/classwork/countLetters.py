satr = input("Satr kiriting : ")
res = {}

for x in satr:
    if x in res:
        res[x] += 1
    else :
        res[x] = 1

k = res.items()

for x in range(len(k)):
    for y in k:
        if y[1] < y[1]:
            y[1],y[1] = y[1],y[1]

for x in k:
    print(x,":",k[x])