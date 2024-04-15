import os
os.system("clear")
    
class Weapon:
    def __init__(self,turi : str):
        self.turi = turi

        if self.turi == "Avtomat":
            self.count = 30
        elif self.turi == "Pistolet":
            self.count = 14
    
    def Oqlash(self,count : int):
        if self.turi == "Avtomat":
            self.count = 30
        elif self.turi == "Pistolet":
            self.count = 14

class Player:
    def __init__(self,nick : str):
        self.__nick = nick
    
    def Otish(obj : Weapon):
        obj.count -= 1
        if obj.count == 0:
            obj.Oqlash()

player1 = Player("Leo")
player2 = Player("BekOripov")

weapon1 = Weapon("Avtomat")
weapon2 = Weapon("Pistolet")

op = int(input("Otishma sonini kiriting: "))
while op > 0:
    player1.Otish(weapon1)

print(weapon1.count)