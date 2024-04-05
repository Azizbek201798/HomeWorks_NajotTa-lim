import os
os.system("clear")

satr = list(map(str,input().split()))
print(f"Old : {satr}")
k = 0

for x in satr:
    x = list(x)
    x[0],x[-1] = x[-1],x[0]
    x = "".join(x)
    satr[k] = x
    k += 1
    
print(f"New : {satr}")
