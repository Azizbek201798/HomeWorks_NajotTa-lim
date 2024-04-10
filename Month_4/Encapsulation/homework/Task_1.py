# Task - 1 => DONE by Azizbek

# Write a Python program to create a class called Student with private 
# instance variables student_id, student_name, and grades. 
# Provide public getter and setter methods to access and modify the student_id 
# and student_name variables. 
# However, provide a method called addGrade() that allows adding a
# grade to the grades variable while performing additional validation.

import os
from uuid import uuid4
os.system("clear")

class Student:
    def __init__(self,__student_id, __student_name : str, __grades : list):
        self.__student_id = __student_id
        self.__student_name = __student_name
        self.__grades = __grades
    
    def get_info(self):
        print("Student ID     : ",self.__student_id)
        print("Student_Name   : ",self.__student_name)
        print("Student_Grades : ",self.__grades)

    def set_info(self):
        self.__student_id = uuid4()
        self.__student_name = input("Name : ")
        self.__grades = list(map(int,input("Baholarni kiriting : ").split()))

    def addGrade(self, grade : int):
        if grade >= 0 and isinstance(grade,int):
            self.__grades.append(grade)
        else :
            print("Manfiy baho yoki int toifasida bo'lmagan naho kiritdingiz!")

# USING addGrade() FUNCTION

# grade = int(input("Baho : "))
# os.system("clear")
# student_1 = Student(uuid4(),"Azizbek",[5,5,4,4,5])

# print("Old Info => \n")
# student_1.get_info()
# student_1.addGrade(grade)
# print("\nNew Info => \n")
# student_1.get_info()

# USING SET FUNCTION

# student1 = Student(75,"Kamosh",[3,4,3,4])
# student1.set_info()
# os.system("clear")
# student1.get_info()

# USING GET FUNCTION

# student_1 = Student(uuid4(),"Azizbek",[5,5,4,4,5])
# student_2 = Student(uuid4(),"Kamola",[4,4,3,5,3])

# student_1.get_info()
# print("\n********************************************************\n")
# student_2.get_info()