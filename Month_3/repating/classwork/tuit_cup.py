import os
os.system("clear")

n,k = map(int,input().split())
ballar = list(map(int,input().split()))
count = 0

for x in range(len(ballar)):
    if ballar[x] >= ballar[k-1]:
        count += 1
print(count - 1)