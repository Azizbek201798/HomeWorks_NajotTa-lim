import os
os.system("clear")

n,pozitsiya = int(input()),1
a,b = "L","R"
buyruq = input()
st = set()

for x in buyruq:
    if x == "L" or x == "R":
        pozitsiya += 1

print(pozitsiya)

# ACCEPTED 100%
