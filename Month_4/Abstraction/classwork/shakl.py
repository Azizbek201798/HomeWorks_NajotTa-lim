# import os
# os.system("clear")
# from abc import ABC,abstractmethod

# class shape(ABC):
#     @abstractmethod
#     def draw(self):
#         pass

# class line(shape):
#     def draw(self):
#         print(20 * "*")
    
# class rectangle(shape):
#     def draw(self):
#         for x in range(10):s
#             for j in range(7):
#                 if x == 0 or x == 9 or j == 0 or j == 6:
#                     print("*",end = "  ")
#                 else:
#                     print("  ",end = "  ")
#             print("  ")

# class triangle(shape):
#     def draw(self):
#         for x in range(10):
#             for j in range(10):
#                 if x == j or j == 0 or x == 9:
#                     print("*",end= " ")
#                 else:
#                     print("  ",end = " ")
#             print("")

# if __name__ == "__main__":
#     line_1 = line()
#     rectangle_1 = rectangle()
#     triangle_1 = triangle()
#     a = input("Shaklni kiriting : ")
#     if a == "line":
#         line_1.draw()
#     elif a == "rectangle":
#         rectangle_1.draw()
#     elif a == "triangle":
#         triangle_1.draw()
#     else :
#         print("Bo'sh shakl")