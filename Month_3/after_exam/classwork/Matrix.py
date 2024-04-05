import os
os.system("clear")

r = open("result.txt","w")

N = int(input("N = "))
matrix = []

for x in range(N):
    for y in range(N):
        if x == y or x + y == N - 1:
            r.write(" 1 ")
        else :
            r.write(" 0 ")
    r.write("\n")