import os
os.system("clear")

class Bankomat:
    def __init__(self):
        self.bankomat() 
    
    @classmethod
    def bankomat(self):
        password = "2017"
        balancce = 300000
        pasword_User = input("Parolni kiriting : ")
        if password == pasword_User:
            os.system("clear")
            choose = input("Quyidagilardan birini tanlang : \n1.Sms xabarnoma\n2.Naqt pul yechish\n3.Balansni ko'rish")
            match int(choose):
                case 1:
                    os.system("clear")
                    tanlash = input("1. Sms habarnomani yoqish 2. Sms habarnomani o'chirish")
                    if int(tanlash) == 1:
                        print("Sms habarnoma yoqildi!")
                    elif int(tanlash) == 2:
                        print("Sms habarnoma o'chirildi")
                case 2:
                    os.system("clear")
                    tanlash = input("1. 10000 2. 50000 3. 100000 4. 200000")
                    if int(tanlash) == 1:
                        os.system("clear")
                        print("10000 so'm yechildi")
                    elif int(tanlash) == 2:
                        os.system("clear")
                        print("50000 so'm yechildi")
                    elif int(tanlash) == 3:
                        os.system("clear")
                        print("100000 so'm yechildi")
                    elif int(tanlash) == 4:
                        os.system("clear")                    
                        print("200000 so'm yechildi")
                case 3:
                    os.system("clear")
                    tanlash = input("1. Ekranga chiqarsinmi 2. Chekga chiqarsinmi")
                    if int(tanlash) == 1:
                        print(f"Balansingizda : {balancce}")
                    elif int(tanlash) == 2:
                        print(f"Balansingizda : {balancce}")
        else :
            print("Xato parol kiritildi")
    
bankomat = Bankomat()