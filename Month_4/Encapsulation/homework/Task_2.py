# Task - 2 => DONE by Azizbek

# Write a Python program to create a class called Car with private instance  variables company_name, model_name, year, and mileage. 
# Provide public getter and setter methods to access and modify the company_name, model_name, and year variables. 
# However, only provide a getter method for the mileage variable.

import os
os.system("clear")

class Car:
    def __init__(self,__company_name : str,__model_name : str,__year : int,__milage : int):
        self.__company_name = __company_name
        self.__model_name = __model_name
        self.__year = __year
        self.__milage = __milage
    
    def set_info(self):
        self.__company_name = input("Name : ")
        self.__model_name = input("Model : ")
        self.__year = int(input("Year : "))
        self.__milage = int(input("Milage : "))

    def get_info(self):
        print(f"Name : {self.__company_name}; Model : {self.__model_name}; Year : {self.__year}; Milage : {self.__milage}")

    def get_milage(self):
        return self.__milage

# USING SET and GET methods for Car Class

car1 = Car("GM","Onix",2024,1000)
car1.set_info()
os.system("clear")
car1.get_info()

# USING GET method for nilage

# car1 = Car("GM","Onix",2024,1000)
# car1.set_info()
# os.system("clear")
# print("Milage :",car1.get_milage())