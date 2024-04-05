import os
os.system("clear")

# 1-yo'l

# satr = input("Satr kiriting : ")
# mineDict = {}



# for x in satr:
#     if x in mineDict: 
#         mineDict[x] = mineDict[x] + 1
#     else :
#         mineDict[x] = 1

# for x in mineDict:
#     print(f"{x} - {mineDict[x]}")

# 2 - yo'l

satr = list(input("Satr kiriting : ").split())
myList = []

for x in satr:
    for y in x:
        myList.append(y)

myList.sort()    

mineDict = {}

for x in satr:
    if x in mineDict: 
        mineDict[x] = mineDict[x] + 1
    else :
        mineDict[x] = 1

for x in mineDict:
    print(f"{x} - {mineDict[x]}")

