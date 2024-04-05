import os
os.system("clear")

S = input()
harflar,dc =[],{}

for x in range(ord('a'),ord('z') + 1):
    harflar.append(chr(x))

for x in range(ord('A'),ord('Z') + 1):
    harflar.append(chr(x))

dc = dc.fromkeys(harflar)
for x in dc:
    dc[x] = 0

for x in range(len(S)):
    if S[x].isalpha() and dc[S[x]] is None:
        dc[S[x]] = 0
    elif S[x].isalpha() and dc[S[x]] is not None:
        dc[S[x]] = dc[S[x]] + 1

for x in dc:
    print(f"{x} {dc[x]}")