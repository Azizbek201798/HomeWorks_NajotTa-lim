#Done by => Azizbek

import os
os.system("clear")

class Bankomat:
    def __init__(self) -> None:
        self.user_password = "2017"
        self.user_balance = 1000000
        self.user_name = "Ziyodullayev Azizbek"
        self.show_menyu()

    def show_menyu(self):
        os.system("clear")
        t = 3
        for x in range(3):    
            input_Password = input("Passwordni kiriting : ")
            os.system("clear")
            t -= 1
            if input_Password == self.user_password:
                while(1):
                    os.system("clear")
                    op = 1
                    print("1. Sms xabarnoma\n2. Naqt pul yechish\n3. Balansni ko'rish")
                    choose = int(input("\nQuyidagilardan birini tanlang(1:3) : "))
                    match choose:
                        case 1:
                            os.system("clear")
                            print("1. Sms xabarnomani yoqish\n2. Sms xabarnomani o'chirish")
                            input_choose = int(input("\nQuyidagilardan birini tanlang(1-2) : "))
                            match input_choose:
                                case 1:
                                    os.system("clear")
                                    print("Sms xabarnoma yoqildi!")
                                case 2:
                                    os.system("clear")
                                    print("Sms xabarnoma o'chirildi!")
                                case _:
                                    os.system("clear")
                                    print("Faqatgina 1 yoki 2 ni kiriting!")
                                    exit()
                        case 2:
                            os.system("clear")
                            print("Miqdorni tanlang : \n1. 10000\n2. 50000\n3. 100000\n4. 200000\n5. 500000")
                            choose = int(input("\nQuyidagilardan birini tanlang(1:5) : "))
                            match choose:
                                case 1:
                                    if self.user_balance > 10000:
                                        self.user_balance -= 10000
                                    else :
                                        os.system("clear")
                                        print("Balansingiz yetarli emas!")
                                        exit()       
                                case 2:
                                    if self.user_balance > 50000:
                                        self.user_balance -= 50000
                                    else :
                                        os.system("clear")
                                        print("Balansingiz yetarli emas!")
                                        exit()       
                                case 3:
                                    if self.user_balance > 100000:
                                        self.user_balance -= 100000
                                    else :
                                        os.system("clear")
                                        print("Balansingiz yetarli emas!")
                                        exit()       
                                case 4:
                                    if self.user_balance > 200000:
                                        self.user_balance -= 200000
                                    else :
                                        os.system("clear")
                                        print("Balansingiz yetarli emas!")
                                        exit()       
                                case 5:
                                    if self.user_balance > 500000:
                                        self.user_balance -= 500000
                                    else :
                                        os.system("clear")
                                        print("Balansingiz yetarli emas!")
                                        exit()                                   
                                case _:
                                    os.system("clear")
                                    print("Faqat 1-5 oraliqdagi son kiritshingiz kerak edi!")
                                    exit()
                            os.system("clear")
                            print("Pulingizni oling!")
                        case 3:
                            os.system("clear")
                            print("1. Ekranga chiqarish\n2. Chek chiqarish")
                            input_choose = int(input("\nQuyidagilardan birini tanlang(1:2) : "))
                            match input_choose :
                                case 1:
                                    os.system("clear")
                                    print("Ekran : \n")
                                    print(f"Foydalanuvchi : {self.user_name}\nBalans : {self.user_balance} ")
                                case 2:
                                    os.system("clear")
                                    print("Chekni oling ... ")
                                case _:
                                    os.system("clear")
                                    print("Faqat 1-5 oraliqdagi son kiritshingiz kerak edi!")
                                    exit()
                        case _:
                            os.system("clear")
                            print("Faqat 1 dan 3 gacha son kiritishingiz kerak edi afsus!")  
                            exit()

                    op = int(input("\nYana operatsiya bajarishni xoxlaysizmi?(1 - Ha 2 - Yo'q) : "))
                    if op == 0:
                        os.system("clear")
                        print("Minnatdormiz! Tashrifingiz uchun rahmat!")
                        exit()
            elif t == 0 :
                print("3 ta urunishda ham xato parol kiritdingiz Kartangiz bloklandi!")
                exit()   
            print(f"Qolgan urinishlar soni : {t} ta. Urinishlar tugasa kartangiz bloklanadi!\n")         

bankomat = Bankomat()