import os
os.system("clear")

class Talaba:
    def __init__(self):
        self.__ism = None

    @property
    def name(self):
        return self.__ism
    
    @name.setter
    def name(self,ism):
        self.__ism = ism

    @name.deleter
    def name(self):
        del self.__ism

talaba = Talaba()
talaba.__ism = "Azizbek"
print(talaba.name)
# talaba.name("Messi")
# print(talaba.name)

