massiv = list(map(int,input("List elementlarini kiriting : ").split()))
key = int(input("Key = "))

for x in range(len(massiv)-1,-1,-1) :
    if key == massiv[x]:
        print(x)
        break
    