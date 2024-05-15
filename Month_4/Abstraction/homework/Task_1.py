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

class Employee(ABC):
    def __init__(self, surname, position, salary):
        self.surname = surname
        self.position = position
        self.salary = salary
    
    @abstractmethod
    def add_salary(self):
        pass

class Enterprise_employee(Employee):
    def __init__(self, surname, position, salary, rating):
        super().__init__(surname, position, salary)
        self.rating = rating
    
    def add_salary(self):
        if self.rating >= 60 and self.rating < 75:
            self.salary += self.salary * 0.2
        elif self.rating >= 75 and self.rating < 90:
            self.salary += self.salary * 0.4
        elif self.rating >= 90 and self.rating <= 100:
            self.salary += self.salary * 0.6

    def show_info(self):
        return f"Surname : {self.surname}; Position : {self.position}; Salary : {self.salary}; Rating : {self.rating}"
    
employee_1 = Enterprise_employee("Ziyodullayev","CEO",1500,61)
employee_2 = Enterprise_employee("Almirzayeva","HomeLady",400,77)
employee_3 = Enterprise_employee("Alisherova","Baby",200,99)
employee_4 = Enterprise_employee("Amonov","Worker",2000,40)
employee_5 = Enterprise_employee("Isroilov","Railway",3000,88)

employees = [employee_1,employee_2,employee_3,employee_4,employee_5]

print("Before : \n")
for x in employees:
    print(x.show_info())

for x in employees:
    x.add_salary()

print("\nAfter : \n")
for x in employees:
    print(x.show_info())