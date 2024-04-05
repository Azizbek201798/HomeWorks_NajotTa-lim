import pickle
import os
os.system("clear")

os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/function_3/classwork")

ls1 = ["Barselona","Arsenal"]
ls2 = ["Real","Surxon"]

with open("info.dat","wb") as f:
    pickle.dump(ls1,f)
    pickle.dump(ls2,f)

res = open("info.dat","rb")

while True:
    try:
        result = pickle.load(res)
        print(result)
    except:
        break