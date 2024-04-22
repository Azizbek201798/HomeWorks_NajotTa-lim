# Task - 1 -> DONE by Azizbek

# CodeWars - 1; Degree Medium; Consider the following class:
# class Animal:
#     def __init__(self, name, number_of_legs):
#         self.name = name
#         self.number_of_legs = number_of_legs
# Write a method that accepts a list of objects of type Animal, and returns a new list. The new list should be a copy of the original list, 
# sorted first by the animal's number of legs, and then by its name.
# If an empty list is passed in, it should return an empty list back.

import os
os.system("clear")

class Animal:
    def __init__(self, name, number_of_legs):
        self.name = name
        self.number_of_legs = number_of_legs

# Hayvonlarni saralash methodi
def sort_animals(animals):
    if not animals:
        return []
    
    sorted_animals = sorted(animals, key=lambda x: (x.number_of_legs, x.name))
    return sorted_animals