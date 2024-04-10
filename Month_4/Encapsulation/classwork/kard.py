import os
os.system("clear")

class Card:
    def __init__(self,number : str,valid : str,type : str,__amount_money : int,__password : int):
        self.number = number
        self.valid = valid
        self.type = type
        self.__amount_money = __amount_money
        self.__password = __password
    
    def get_info(self):
        return f"Raqami : {self.number}; Muddat : {self.valid};Turi : {self.type}; Miqdori : {self.__amount_money}; Parol : {self.__password}"

    def give_permission(self):
        self.__transfer(100000)
        print(self.get_info())

    def __transfer(self,transfer_amount):
        self.__amount_money -= transfer_amount 

card1 = Card("8600 1111 2222 3333","11/25","Humo",350000,2705)

print(card1.get_info())
print("\n*****************************************\n")
print(card1.give_permission())