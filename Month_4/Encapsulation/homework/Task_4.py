# Task - 4 => DONE by Azizbek

# Write a Python program to create a class called Employee with private instance 
# variables employee_id,employee_name, and employee_salary. Provide public getter and setter methods to 
# access and modify the id and name variables, but provide a getter method for the salary variable that returns a formatted string.

import os
from uuid import uuid4
os.system("clear")

class Employee:
    def __init__(self,__employee_id,__employee_name : str,__employee_salary : int):
        self.__employee_id = __employee_id
        self.__employee_name = __employee_name
        self.__employee_salary = __employee_salary
        
    def set_info(self):
        self.__employee_id = uuid4()
        self.__employee_name = input("Name : ")
        self.__employee_salary = int(input("Salary : "))

    def get_info(self):
        return f"ID : {self.__employee_id}; Name : {self.__employee_name}; Salary : {self.__employee_salary}"
    
    def get_salary(self):
        return f"Salary : {self.__employee_salary}"
    
# USING get_salary() method

employee_1 = Employee(1,"Azizbek",450)
employee_1.set_info()
os.system("clear")
print(employee_1.get_info())

# USING get_salary()

# employee_1 = Employee(1,"Azizbek",450)
# employee_1.set_info()
# os.system("clear")
# print(employee_1.get_salary())
