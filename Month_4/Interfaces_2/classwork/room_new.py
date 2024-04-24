import os
os.system("clear")

class Room:
    def __init__(self,lenght : int, height : int, widgth : int):
        self.lenght = lenght
        self.height = height
        self.widgth = widgth

    def Count_windows(self):
        count = 0 
        if room.lenght >= 2:
            if room.lenght * room.height >= 30:
                count += (room.lenght * room.height) // 30
                count += (room.lenght * room.height) // 30
            if room.lenght * room.widgth >= 30:
                count += (room.lenght * room.widgth) // 30
                count += (room.lenght * room.widgth) // 30
        else:
            return 0 
        return count

    def Hajm(self,room):
        return room.lenght * room.height * room.widgth

total = 0
rooms = []
for x in range(5):
    total += 1
    balnadligi = int(input(f"{total} - Uy balandligini kiriting : "))
    eni = int(input(f"{total} - Uy enini kiriting : "))
    boyi = int(input(f"{total} - Uy bo'yini kiriting : "))
    rooms.append(Room(balnadligi,eni,boyi))
    os.system("clear")

# Task 1 => Jami Har bir xonadonning yon devorlariga 2 x 15 o'lchamli oynadan nechta ishlatilishini hisoblash;
print("Oynalar soni => \n")
total = 1
for room in rooms:
    print(f"{total} - xonaga {room.Count_windows()} ta oyna ketadi!")
    total += 1

# Task 2 => Har bir xonaning hajmini chop etish;
print("\nHajm => \n")
total = 1
for room in rooms:
    print(f"{total} - xonaning hajmi : {room.Hajm(room)} ga teng")
    total += 1

# unset GTK_PATH