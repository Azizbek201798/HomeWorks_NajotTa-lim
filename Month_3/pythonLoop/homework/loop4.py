import os 
os.system("clear")

# DONE;

count = 0

while 1 :
    number= int(input("Son = "))
    if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
        count += 1
    if number == 0:
        break

if count >=2 :
    print(True)
else :
    print(False)
