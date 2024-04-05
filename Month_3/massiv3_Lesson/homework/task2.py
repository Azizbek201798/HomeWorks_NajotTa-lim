# Topshiriq_2 => DONE by LeoMessi

# Kiritilgan string ma'lumotini dictionaryga har bir belgi keyga va ushbu belgi nechtaligi valuega yozilsin.
# Input: 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

import os
os.system("clear")

word = input("Satr kiriting: ")
myDict = {}

for x in word:
    if x not in myDict:
        myDict.update({x:1})
    else :
        myDict[x] = myDict[x] + 1

print(myDict)

