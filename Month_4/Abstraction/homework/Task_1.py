# TASK - 1: EMPLOYEE => DONE by Azizbek

# Employee nomli class yarating va uning property elementlari quyidagilardan iborat:
# -        Surname(Familiyasi);
# -        Position(Lavozimi);
# -        Salary(Oyligi).

# Enterprise_employee nomli class Employee classidan voris bo'lib keladi va uning property elementlari quyidagilardan iborat:
# -        Surname(Familiyasi);
# -        Position(Lavozimi);
# -        Salary(Oyligi);
# -        Rating(Reytingi 100 ballik tizimda).
# Enterprise_employee nomli classining 5ta obyektini yarating. Sizning vazifangiz ushbu obyektlar orasidagi ishchilarning 
# reytingi 60dan 75ballgacha(75 kirmaydi) bo'lganlarni oyligini 20%ga, 75dan 90ballgacha(90 kirmaydi) bo'lganlarni 
# oyligini 40%ga va 90dan 100gacha(100 kiradi) bo'lganlarni oyligini 60%ga oshiring.

import os
from abc import ABC, abstractmethod
os.system("clear")

class Employee:
    def __init__(self,Surname : str, Position : str, Salary : int):
        self.Surname = Surname
        self.Position = Position
        self.Salary = Salary

    @abstractmethod
    def EnterpriseByRating(self):
        pass

class EnterPrise_Employee(Employee):
    def __init___(self,Surname : str, Position : str, Salary : int, Rating : int):
        self.Surname = Surname
        self.Position = Position
        self.Salary = Salary
        self.Rating = Rating

    def EnterpriseByRating(self):
        if self.Rating >= 60 and self.Rating < 75:
            self.Salary += self.Salary * 0.2
        elif self.Rating >= 75 and self.Rating < 90:
            self.Salary += self.Salary * 0.4
        elif self.Rating >= 90 and self.Rating <= 100:
            self.Salary += self.Salary * 0.6

    def show_info(self):
        return f"Surname : {self.Surname}; Position : {self.Position}; Salary : {self.Salary}; Rating : {self.Rating}"
    
employee_1 = EnterPrise_Employee("Ziyodullayev","CEO",1500)
employee_2 = EnterPrise_Employee("Almirzayeva","HomeLady",400)
employee_3 = EnterPrise_Employee("Alisherova","Baby",200)
employee_4 = EnterPrise_Employee("Amonov","Worker",2000)
employee_5 = EnterPrise_Employee("Isroilov","Railway",3000)

employee_1.EnterpriseByRating()
employee_2.EnterpriseByRating()
employee_3.EnterpriseByRating()
employee_4.EnterpriseByRating()
employee_5.EnterpriseByRating()

# employee_1.show_info()
# employee_2.show_info()
# employee_3.show_info()
# employee_4.show_info()
# employee_5.show_info()