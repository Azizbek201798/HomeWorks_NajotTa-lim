import os
os.system("clear")

n = int(input())
elementlar = list(map(int,input().split()))
elementlar.remove(max(elementlar))
print(max(elementlar))

