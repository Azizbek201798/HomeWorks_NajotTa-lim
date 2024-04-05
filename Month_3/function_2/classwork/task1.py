import os
os.system("clear")

word = input()
print(f"OldWord : {word}")
ls = word.split()
newWord = ""

for x in range(len(ls)):
    temp = ls[x][len(ls[x]) - 1]
    ls[x][len(ls[x]) - 1] = ls[x][0]
    ls[x][0] = temp
    newWord = newWord + ls[x] + " "

print(f"NewWord : {newWord}")


