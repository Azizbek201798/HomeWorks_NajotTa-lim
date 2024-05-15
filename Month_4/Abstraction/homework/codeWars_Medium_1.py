import os
os.system("clear")

def slice(a, b):

    result = ""  

    for x in range(ord(a),ord(b)+1):
        result += chr(x)

    return result    

print(slice("f","f"))

