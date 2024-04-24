import os
os.system("clear")

class Time:
    def __init__(self,day : int, month : int, year : int):
        self.day = day
        self.month = month
        self.year = year

    def show_info(self):
        if self.month > 12 or self.month < 1 or self.day > 31 or self.day < 1:
            return "Kiritilgan kun yoki oy mavjud emas!"
        return "{:02}-{:02}-{:02}".format(self.day,self.month,self.year)

    # 1 - shart uchun yilni birga oshirish methodi;
    def add_year(self):
        self.year += 1

    # 2 - task uchun kunni 2 ga kamaytirish methodi;
    def decrease_day(self):
        if self.day <= 2:
            if self.month == 1:
                self.month += 12 - 1
                self.year -= 1
            else :
                self.month -= 1

            if self.month == 1:
                self.day += 31 - 2
            elif self.month == 2:
                self.day += 28 - 2
            elif self.month == 3:
                self.day += 31 - 2
            elif self.month == 4:
                self.day += 30 -2
            elif self.month == 5:
                self.day += 31 - 2
            elif self.month == 6:
                self.day += 30 - 2
            elif self.month == 7:
                self.day += 31 - 2
            elif self.month == 8:
                self.day += 31 - 2 
            elif self.month == 9:
                self.day += 30 - 2
            elif self.month == 10:
                self.day += 31 - 2
            elif self.month == 11:
                self.day += 30 - 2
            elif self.month == 12:
                self.day += 31 - 2
            else:
                self.day -= 2

# 5 ta dateni foydalanuvchi kiritadi;
dates = []
for x in range(5):
    day = int(input(f"{x+1} - kunni kiriting : "))
    month = int(input(f"{x+1} - oyi kiriting : "))
    year = int(input(f"{x+1} - yilni kiriting : "))
    dates.append(Time(day,month,year))
    os.system("clear")

# 1 - Shart uchun;

# for x in dates:
#     print("Before : ",x.show_info())    
#     x.add_year()
#     print("After : ",x.show_info())    
#     print("")

# 2 - Shart uchun;

for x in dates:
    print("Before : ",x.show_info())    
    x.decrease_day()
    print("After : ",x.show_info())    
    print("")