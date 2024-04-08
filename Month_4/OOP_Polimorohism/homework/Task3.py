# Task - 3 => DONE by Azizbek
 
# Point nomli class uchun dunder methodlar (__init__ dan tashqari 4 ta yarating) IZOH: Masalan __add__, __gt__

import os
os.system("clear")

class Futbolchi:
    def __init__(self,name : str, goals : int,salary : int,club : str):
        self.name = name
        self.goals = goals
        self.salary = salary
        self.club = club
    
    def __str__(self):
        return f"Ismi : {self.name} Jamoasi : {self.club} Gollari soni = {self.goals} Salary : {self.salary}"

    def __add__(self,additional):
        if isinstance(additional,int):
            self.salary += additional
        
        return self

    def __sub__(self,additional):
        if isinstance(additional,int):
            self.salary -= additional
        
        return self

futbolchi1 = Futbolchi("Messi",1560,2000000,"Barselona")

# 1) Using example : __str__    

# print(futbolchi1)

# 2) Using example : __add__
    
# print(futbolchi1)
# futbolchi1 += 1000
# print(futbolchi1)

# 3) Using example : __sub__

# futbolchi1 -= 2000
# print(futbolchi1)

# 3) Using example : 
