import os
os.system("clear")

class Product:
    def __init__(self, name : str, price : int, year_create : int):
        self.name = name
        self.price = price
        self.year_create = year_create

class License_product(Product):
    def __init__(self,name,price,year_create,date_price):
        super().__init__(name,price,year_create)
        self.date_price = date_price

    def count_days(self,date : str):
        date = date.split("-")
        day = int(date[0])
        month = int(date[1])
        year = int(date[-1])
        return (year - self.year_create)*365 + (12-month) * 30 +  (30-day)
    
product = Product("To'p",4000,2024)

# 5 ta product sanalarini kiritish;
total,products = 0,[]
for x in range(2):
    total += 1
    name = input(f"{total} - product ismini kiriting: ")
    price = input(f"{total} - product narxini kiriting: ")
    year_created = int(input(f"{total} - product yaratilgan yilni kiriting: "))
    date = input(f"{total} - product sanasini kiriting(dd-mm-yyyy): ")
    products.append(License_product(name,price,year_created,date))

# 5 ta product yaratilgandan kirib keldandan buyon qancha vaqt o'tganini topish;
total = 0
os.system("clear")
for x in products:
    total += 1
    print(f"{total} - tovar kelganiga {x.count_days(date)} kun bo'ldi!")