# Task - 3 => DONE by Azizbek
 
# Write a Python program to create a class called Circle with a private instance variable radius. 
# Provide public getter and setter methods to access and modify the radius variable. 
# However, provide two methods called calculateArea() and calculatePerimeter() that return the calculated 
# area and perimeter based on the current radius value.

import os
import math
os.system("clear")

class Circle:
    def __init__(self,__radius : int):
        self.__radius = __radius
    
    def set_info(self):
        self.__radius = int(input("Radius : "))
    
    def get_info(self):
        return self.__radius
    
    def calculateArea(self):
        return math.ceil(self.__radius ** 2 * math.pi)

    def calculatePerimetr(self):
        return math.ceil(2 * math.pi * self.__radius)

# USING calculatePerimetr() and set_info() method

circle_1 = Circle(1)
circle_1.set_info()
os.system("clear")
print("Perimetr :",circle_1.calculatePerimetr())

# USING calculateArea() and set_info() method

# circle_1 = Circle(1)
# circle_1.set_info()
# os.system("clear")
# print("Yuza :",circle_1.calculateArea())

# USING get_info() and set_info() method

# circle_1 = Circle(1)
# circle_1.set_info()
# os.system("clear")
# print("Radius :",circle_1.get_info())