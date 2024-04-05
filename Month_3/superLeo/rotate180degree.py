import os
os.system("clear")

word = "69069069"
box = word

word = word.replace("6", "*")
word = word.replace("9", "6")
word = word.replace("*", "9")

print(True) if word[::-1] == box else print(False)
