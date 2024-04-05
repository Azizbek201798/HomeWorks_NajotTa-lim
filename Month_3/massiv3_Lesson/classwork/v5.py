son = input("Son = ")
check = False

for x in son:
    if x == '0':
        print("NO")
        check = True
        break

if check == False:
    print("YES")

