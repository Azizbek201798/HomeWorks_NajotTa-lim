import os
os.system("clear")

word = input("Sartni kiriting : ")
l,index = len(word),0
while l > 0:
    print(ord(word[index]),end = ",")
    l -= 1
    index += 1
print("")