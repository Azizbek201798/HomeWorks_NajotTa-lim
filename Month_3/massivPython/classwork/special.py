import os
os.system("clear")

word = input("Son = ")
box = word

word = word.replace("6","*")
word = word.replace("9","6")
word = word.replace("*","9")

if word[::-1] == box:
    print(True)
else :
    print(False)    