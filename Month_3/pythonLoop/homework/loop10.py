import os
os.system("clear")

#

check = True
k = None
while 1:
    number = int(input("Son = "))
    if k is not None and number > k:
        check = False
    elif k == None:
        k = number
    k = number
    if number == 0:
        break
if check == True:
    print("\nKetma-ketlik kamayish tartibida!")
else :
    print("\nKetma-ketlik kamayish tartibida EMAS!")

