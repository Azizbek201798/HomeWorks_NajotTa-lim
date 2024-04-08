# Task - 1.1 => DONE by Azizbek

# Method overload bo'yicha 2 ta ixtiyoriy dastur yozing (class nomi ixtiyoriy) 

import os
os.system("clear")

# FIRST EXAMPLE:

class Murabbiy():
    def __init__(self,name,oyinlar_soni,lost,prise):
        self.name = name
        self.oyinlar_soni = oyinlar_soni
        self.lost = lost
        self.prise = prise
    
    def get_salary(self):
        return (self.oyinlar_soni-self.lost) * self.prise

class Futbolchi():
    def __init__(self,name,scored,per_goal):
        self.name = name
        self.scored = scored
        self.per_goal = per_goal
    
    def get_salary(self):
        return self.scored * self.per_goal

class Hakam():
    def __init__(self,name,total,succesfull_games_prise):
        self.name = name
        self.total = total
        self.succesfull_games_prise = succesfull_games_prise
    
    def get_salary(self):
        return self.succesfull_games_prise * self.total

if __name__ == "__main__":

    murabbiy1 = Murabbiy("Azizbek",1,1,1) 
    murabbiy1.__init__("Scaloni",30,3,1000)

    futbolchi1 = Futbolchi("Azizbek",1,1)
    futbolchi1.__init__("Leo Messi",45,2000)

    hakam1 = Hakam("Azizbek",1,1)
    hakam1.__init__("Ravshan Ermatov",5,2500)

    Jamoa = [murabbiy1,futbolchi1,hakam1]
    for x in Jamoa:
        print("Total salary = ",x.get_salary())
