import os
os.system("clear")

L,R = map(int,input().split())
check,count = True,0

for x in range(L,R+1):
    son = x
    check = True
    while x > 0:
        qoldiq = x % 10
        if qoldiq == 0:
            check = False
            break
        if son % (qoldiq) != 0:
            check = False
            break  
        x //= 10
    if check == True:
        count += 1

print(count)

# ACCEPTED 100%