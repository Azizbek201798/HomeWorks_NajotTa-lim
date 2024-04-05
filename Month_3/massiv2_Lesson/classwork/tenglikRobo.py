import os
os.system("clear")

a,b = map(int,input().split())
count = 0

while True:
    if a == b:
      print(0)
      break

    if b > a: # 13 45
      a += 10 # 23 33 43 
      count += 1
      continue
    
    if a > b :
      a -= 10
      count += 1
      continue
    else :
       break
print(count + 1)
