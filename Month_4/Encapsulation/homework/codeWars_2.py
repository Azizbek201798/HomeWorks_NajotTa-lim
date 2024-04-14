import os
os.system("clear")

# CodeWars Degree 7

word = input("Word : ")

def validate_word(word):
    word = word.lower()
    length = len(word)
    count,key = 0,{}
    key = key.fromkeys(word)
    count = len(key.keys())
    if length % count == 0:
        return True
    else :
        return False

print(validate_word(word))

# client
# A