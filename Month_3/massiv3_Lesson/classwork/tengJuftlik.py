a,b = map(int,input().split())
count = 0

if a > b:
    while True: # 69,30; 40,50,60,
        a -= 10
        if a < b:
            break
        count += 1
elif b > a:
    while True: # 30,69; 40,50,60,
        a += 10
        if b < a:
            break
        count += 1
        
if a != b:
    print(count + 1)
else : 
    print(0)

    