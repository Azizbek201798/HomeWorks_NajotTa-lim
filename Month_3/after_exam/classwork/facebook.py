ls = list(map(str,input("Elementlarini kiriting : ").split(" ")))

if len(ls) == 0:
    print("no one likes this")
elif len(ls) == 1:
    print(f"{ls[0]} likes this")
elif len(ls) >= 2:
    for x in range(len(ls)):
        if x != len(ls) - 2:
            print(f"{ls[x]}, ")
        elif x != len(ls) - 1:
            print(f"{ls[x]} ")
        print(f"and {ls[x]} ")
