# Topshiriq_6 => DONE by Azizbek

# Komanda nomli class berilgan 5ta obyektli. 
#      Ma'lumotlari: (nomi, ishtirokchilari_soni, trener, kapitani).
#      Kirish va chiqarish methodlari bo'lishi kerak.
#      Methodda Komanda nomi bo'yicha saralab chiqaradigan dastur tuzing va boshqa methodda new_komanda nomi bor yo'qligini 
#      aniqlaydigan va shu komanda ma'lumotlarini chiqaradigan dastur tuzing va agar bo'lmasa 'Bunday komanda yo'q' deb chiqsin.
#      #topshiriq_class_merosxo'rlik

import os
os.system("clear")

class Komanda:
    def __init__(self,nomi : str, ishtirokchilar_soni : int,murabbiy : str, kapitan : str):
        self.nomi = nomi
        self.ishtirokchilar_soni = ishtirokchilar_soni
        self.murabbiy = murabbiy
        self.kapitan = kapitan
    
    def set_info(self):
        nomi = input("Nomi : ")
        ishtirokchilar_soni = int(input("Ishtirokchilar soni : "))
        murabbiy = input("Murabbiy : ")
        kapitan = input("Kapitan : ")
        
        return Komanda(nomi,ishtirokchilar_soni,murabbiy,kapitan)
    
    def get_info(self):
        print(f"Nomi : {self.nomi}; Ishtirokchilar soni : {self.ishtirokchilar_soni}; Murabbiy : {self.murabbiy}; Kapitan : {self.kapitan}")

def sort_by_name(ls : list):
    return sorted(ls,key = lambda x : x.nomi)

# TASK - 1; Kiritish va chiqarish methodlarini ishlatish;

# op, komandalar = 1,[]

# while op:
#     komanda = Komanda("Surxon",11,"Andrey","Azizbek Ziyodullayev")
#     komandalar.append(komanda.set_info())
#     op = int(input("Yana komanda qo'shmoqchimisiz? 1.Ha 2.Yo'q : "))

# for x in komandalar:
#     x.get_info()

# TASK - 2: Methodda Komanda nomi bo'yicha saralab chiqaradigan dastur tuzing;

# Komandalar = [Komanda("Barselona",35,"Xavi Ernandes","Lewandowski"),
#               Komanda("Real Madrid",33,"Karlo Anchelotti","Vinisius"),
#               Komanda("Arsenal",27,"Arteta","Teo"),
#               Komanda("Chelsea",35,"Lampard","Rudiger"),
#               Komanda("Atletiko",21,"Simyone","Suares"),]

# os.system("clear")
# result = sort_by_name(Komandalar)
# for x in result:
#     x.get_info()

# TASK - 3: Boshqa methodda new_komanda nomi bor yo'qligini aniqlaydigan va shu komanda ma'lumotlarini chiqaradigan dastur tuzing 
# va agar bo'lmasa 'Bunday komanda yo'q' deb chiqsin.

# Komandalar = [Komanda("Barselona",35,"Xavi Ernandes","Lewandowski"),
#               Komanda("Real Madrid",33,"Karlo Anchelotti","Vinisius"),
#               Komanda("Arsenal",27,"Arteta","Teo"),
#               Komanda("Chelsea",35,"Lampard","Rudiger"),
#               Komanda("Atletiko",21,"Simyone","Suares"),]

# def check_by_name(ls : list):
#     komanda = input("Qidirmoqchi bo'lgan komandangizni ayting : ")
#     check = False
#     os.system("clear")
#     for x in Komandalar:
#         if x.nomi == komanda:
#             check = True
#             return x.get_info()
#     if check == False:
#         print("Bunday komanda listda mavjud emas!")

# check_by_name(Komandalar)
