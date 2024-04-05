import os
os.system("clear")



# from mtCars_mod import myCars
# mine = myCars("Gm","Gentra","Qora","Mexanika",2024,21000)
# print(mine)

# def yigindi(*sonlar):
#     sum = 0
#     for x in sonlar:
#         sum += x
#     return sum

# print(yigindi(1,2,3,4,5,6))
# print(yigindi(11,22))

# def bahola(ismlar : list):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baholar[ism] = int(input(f"{ism} ning bahosini qo'ying : "))
#     return baholar

# talabalar = ["Anvar","Nurbek","Jamoliddin","Axror"]
# info = talabalar.copy()
# baholar = bahola(info)
# print(f"\nKo'rsatgich : {baholar}")

# print("Salonimizga avtomobil ma'lumotlarini kiriting : ")
# avtolar = []

# while True:
#     kompaniya = input("Kompaniya : ")
#     model     = input("Model : ")
#     rang      = input("Rang : ")
#     korobka   = input("Korobka : ")
#     yil       = input("Yil : ")
#     narx      = input("Narx : ")
    
#     avto = {
#         'kompaniya' : kompaniya,
#         'model'     : model,
#         'rang'      : rang,
#         'korobka'   : korobka,
#         'yil'       : yil,
#         'narx'      : narx
#     }

#     avtolar.append(avto)
#     answer = input("Yana avtomobil qo'shasizmi?(yes/no) : ")
#     if answer.lower() == "no":
#         break
#     os.system("clear")
#     print("Salonimizga avtomobil ma'lumotlarini kiriting : ")



# os.system("clear")
# print("Salondagi barcha avtomobillar : \n")

# for avto in avtolar:
#     if avto['narx'] == '':
#         avto['narx'] = 'Nomalum'
#     else :
#         avto['narx'] = avto['narx']
#     print(avto)


# def oraliq(min : int,max : int,step = 1):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += step
#     return sonlar

# mine = oraliq(1,10,3)
# print(mine)

# def myCars(kompaniya : str,model : str,rang : str,korobka : str,yil : int,narx = None):
#     avto = {
#         'kompaniya' : kompaniya,
#         'model' : model,
#         'rang' : rang,
#         'korobka' : korobka,
#         'yil' : yil,
#         'narx' : narx
#     }
#     return avto

# avto1 = myCars("GM","Malibu","Qora","Avtomat",2021)
# avto2 = myCars("Hyundai","Sonata","Qizil","Mexanika",2015,27000)
# avtolar = [avto1,avto2]

# def toliq_ism_sana(ism : str,familiya :str, otasining_ismi = " "):
#     if otasining_ismi:
#         toliq_ism = f"{ism} {familiya} {otasining_ismi}"
#     else :
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism 

# my = toliq_ism_sana("Azizbek","Ziyodullayev","Alisher o'gli")
# print(my)

# def toliq_ism_yasa(ism:str,familiya:str):
#     toliq_ism = f"{ism} : {familiya}"
#     return toliq_ism

# info = toliq_ism_yasa("Azizbek","Ziyodullayev")
# print(info)

# def my(ism,familiya):
#     mine = f"{ism}:{familiya}"
#     print(mine)

# my("Azizbek","Ziyodullayev")
