import os
os.system("clear")

class kitob:
    def __init__(self):
        self.name = None
        self.author = None
        self.written = "dd-mm-yyyy"
        self.count_publish = 0

    def set_info(self,n,a,w,c):
        self.name = n
        self.author = a
        self.written = w
        self.count_publish = c
    
def get_info(a):
    print(a.name)
    print(a.author)
    print(a.written)
    print(a.count_publish)

print("KITOB - 1\n")

result = kitob()
result.name = "Sariq devni minib"
result.author = "Xudoyberdi To'xtaboyev"
result.written = 1990
result.count_publish = 10000

get_info(result)

print("------------------------------------------")
print("KITOB - 2\n")
name = "Python"
author = "Azizbek"
written = 2024
count_publish = 7777
result.set_info(name,author,written,count_publish)
get_info(result)