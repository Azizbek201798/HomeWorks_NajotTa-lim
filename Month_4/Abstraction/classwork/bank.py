import os
from abc import ABC,abstractmethod
os.system("clear")

class Bank(ABC):

    @abstractmethod
    def input(self):
        pass

    @abstractmethod
    def output(self):
        pass

class Client(Bank):
    def __init__(self,name : str, amount_money : str, password : str):
        self.name = name
        self.amount_money = amount_money
        self.password = password
    
    def input(self, money : int):
        self.amount_money += money

    def output(self, transaction_money : int, password : str):
        
        if self.password == password and transaction_money < self.amount_money:
            self.amount_money -= transaction_money
        else :
            print("Siz kiritgan parol xato yoki mablag'ingiz yetmaydi!")

    def show_info(self):
        print(f"""Name   : {self.name}; Money  : {self.amount_money}""")
        
client = Client("Azizbek",100,"tashiit2017")

client.input(200)
client.show_info()

print("\n***********************************\n")

client.output(10,"tashiit2017")
client.show_info()
