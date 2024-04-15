from random import choice
import os
os.system("clear")

class Weapon:
    def __init__(self, turi, name):
        self.turi = turi
        self.name = name

        if self.turi == "Avtomat":
            self.__magazin = 30
        elif self.turi == "pp":
            self.__magazin = 14
    
    def oqlash(self):
        if self.turi == "Avtomat":
            self.__magazin = 30
        elif self.turi == "pp":
            self.__magazin = 14
    
    def otish(self):
        self.__magazin -= 1
        if self.__magazin == 0:
            self.oqlash()

class Player:
    def __init__(self, types, nick, qurol : Weapon):
        self.types = types
        self.nick = nick
        self.qurol = qurol
        self.__health = 100

    def oqlash_weapon(self):
        self.qurol.oqlash()
    
    def get_health(self):
        return f"{self.nick} -> {self.__health}"

    def set_health(self, obj):
        dct = {'bosh':100, 
               'yurak':99,
               'yelka':30, 
               'oyoq':20,
               'qol':20,
               "":0}
        rnd = choice(list(dct))
        obj.__health -= dct[rnd]

        if rnd == "":
            print(f"{self.nick} {obj.nick}'ning hech qayeriga tekkaza olmadi 🤣")
        else:
            print(f"{self.nick} {obj.nick}'ning {rnd}'siga tekkazdi 😒🔫😎")

        print(obj.get_health())

        if obj.__health < 1:
            print(f"{obj.nick} is dead by {self.nick} 🛌")
            exit()

    def otish_weapon(self, obj):
        self.qurol.otish()
        self.set_health(obj)

w1 = Weapon('pp', 'deagle')
w2 = Weapon('Avtomat', "Ak-47")

p1 = Player('tt', 'cuba', w2)
p2 = Player('ct', 'Leo Messi', w1)


while True:
    # lst = [1,2]
    # natija = choice(lst)
    # if natija==1:
    #     p1.otish_weapon(p2)
    #     p2.otish_weapon(p1)
    # else:
    #     p2.otish_weapon(p1)
    #     p1.otish_weapon(p2)

    lst = [p1,p2]
    a = choice(lst)
    lst.remove(a)
    a.otish_weapon(lst[0])        