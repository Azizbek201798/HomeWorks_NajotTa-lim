import os
os.system("clear")
# os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/function_3")

f = open("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/function_3/juft.txt","rt")
data = f.read()

def maxEvenLen(data : str):
    data,max,indx = data.split(),0,-1
    for x in range(len(data)):
        if len(data[x]) % 2 == 0 and max < len(data[x]):
            max = len(data[x])
            indx = x
    if indx != -1:
        print(data[indx])
    else :
        print("Juft uzunlikdagi so'z mavjud emas!") 

maxEvenLen(data)

# try :
#     f = open("juft.txt","wt")
#     matn = "nostop"
#     while matn != "stop":
#         matn = input()
#         f.write(matn)

#     f.seek(0)
    
#     z = open("juft.txt","rt")
#     data = z.read()
#     max = 0
#     for x in data.split():
#         if len(x) % 2 == 0 and len(x) >= max:
#             max = x
        
#     if max != 0:
#         print("\nResult : " + max)
#     else :
#         print("Juft uzunlikdagi so'z mavjud emas!")

# except :
#     print("Siz ochmoqchi bo'lgan fayl mavjud emas!")

