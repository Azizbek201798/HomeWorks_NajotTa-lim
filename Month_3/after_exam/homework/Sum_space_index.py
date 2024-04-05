import os
os.system("clear")

N,day = map(int,input().split())
days = list(map(int,input().split()))
indexes = []

for x in range(len(days)):
    if days[x] == day:
        indexes.append(x+1)

print(len(indexes) * day)
for x in indexes:
    print(x,end = " ")

# EXCEPTED 100%