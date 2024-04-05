import os
os.system("clear")

a,b = map(int,input().split())
fact = 1
min = min(a,b)
for x in range(1,min+1):
  fact *= x
print(fact)

#ACCEPTED 100%