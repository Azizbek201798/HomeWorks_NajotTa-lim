# DONE BY AZIZBEK

import os
import mysql.connector as myc
os.system("clear")

class data_base:
    def __init__(self,db_name = "Techno_db"):
        try:
            self.mdb = myc.connect(host = "localhost", user = "root", password = "Najot1995!",database = f"{db_name}")
            self.kur = self.mdb.cursor()
        except: 
            self.mdb = myc.connect(host = "localhost", user = "root", password = "Najot1995!")
            self.kur = self.mdb.cursor()
            self.kur.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

    def CreateTable_Product(self,tableName = 'Product'):
        self.kur.execute(f"""CREATE TABLE IF NOT EXISTS {tableName}
                         (maker varchar (10) NOT NULL , model varchar (50) NOT NULL PRIMARY KEY ,type varchar (50) NOT NULL);""")
        
    def InputInfo_Product(self):
        op = 1
        while op == 1:
            os.system("clear")
            maker =       input("Maker:  >>> ")
            model =       input("Model:  >>> ")
            type =         input("Type:   >>> ")
            
            sql = """INSERT INTO Product(maker,model,type) VALUES (%s,%s,%s);"""
            self.kur.execute(sql,(maker,model,type))
            self.mdb.commit()
            op = int(input("Yana ma'lumot qo'shasizmi?"))

    def ShowInfo_Product(self,sql = "SELECT * FROM Product;"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"{x[0]}; {x[1]}; {x[2]};")

    def CreateTable_PC(self,tableName = 'PC'):
        self.kur.execute(f"""CREATE TABLE IF NOT EXISTS {tableName}
                         (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,model varchar(50) NOT NULL ,speed smallint NOT NULL ,
                         ram smallint NOT NULL ,hd real NOT NULL ,cd VARCHAR(10),price decimal(12,2) NULL,
                         foreign key (model) references Product(model));""")
        self.kur.execute(f"ALTER TABLE PC ADD CONSTRAINT FK_pc_product FOREIGN KEY (model) REFERENCES Product (model));")
        
    def InputInfo_PC(self):
        op = 1
        while op == 1:
            os.system("clear")
            model =       input("Model:  >>> ")
            speed =       input("Speed:  >>> ")
            ram =         input("Ram:    >>> ")
            hd =          input("Hd:     >>> ")
            cd =          input("CD:     >>> ")
            price =   float(input("Price:  >>> "))

            sql = """INSERT INTO PC(model,speed,ram,hd,cd,price) VALUES (%s,%s,%s,%s,%s,%s);"""
            self.kur.execute(sql,(model,speed,ram,hd,cd,price))
            self.mdb.commit()
            op = int(input("Yana ma'lumot qo'shasizmi?"))

    def ShowInfo_PC(self,sql = "SELECT * FROM PC;"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"{x[0]} - {x[1]}; {x[2]}; {x[3]}; {x[4]}; {x[5]}; {x[6]}")



    def CreateTable_Printer(self,tableName = 'Printer'):
        self.kur.execute(f"""CREATE TABLE IF NOT EXISTS {tableName}
                         (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,model varchar (50) NOT NULL ,color char (1) NOT NULL ,
                         type varchar (10) NOT NULL ,price decimal(12,2) NULL ,foreign key (model) references Product(model));""")

    def InputInfo_Printer(self):
        op = 1
        while op == 1:
            os.system("clear")
            model =       input("Model:  >>> ")
            color =       input("Color:  >>> ")
            type =        input("Type:   >>> ")
            price =   int(input("Price:  >>> "))
            
            sql = """INSERT INTO Printer(model,color,type,price) VALUES (%s,%s,%s,%s);"""
            self.kur.execute(sql,(model,color,type,price))
            self.mdb.commit()
            op = int(input("Yana ma'lumot qo'shasizmi?"))

    def ShowInfo_Printer(self,sql = "SELECT * FROM Printer;"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"{x[0]}; {x[1]}; {x[2]};")

    def CreateTable_Laptop(self,tableName = 'Laptop'):
        self.kur.execute(f"""CREATE TABLE IF NOT EXISTS {tableName}
                             (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                             model VARCHAR(50) NOT NULL,
                             speed SMALLINT NOT NULL,
                             ram SMALLINT NOT NULL,
                             hd REAL NOT NULL,
                             price DECIMAL(12,2) NULL,
                             screen SMALLINT NOT NULL,
                             FOREIGN KEY (model) REFERENCES Product(model)
                        );"""
)
        self.kur.execute(f"""ALTER TABLE Laptop ADD 
	                        CONSTRAINT FK_Laptop_product FOREIGN KEY (model) 
                            REFERENCES Product (model);""")    
        
    def InputInfo_Laptop(self):
        op = 1
        while op == 1:
            os.system("clear")
            model =       input("Model:  >>> ")
            speed =       input("Speed:  >>> ")
            ram =         input("Ram:    >>> ")
            hd =          input("Hd:     >>> ")
            price =   float(input("Price:  >>> "))
            screen =  int(input("Screen: >>> "))

            sql = """INSERT INTO Laptop(model,speed,ram,hd,price,screen) VALUES (%s,%s,%s,%s,%s,%s);"""
            self.kur.execute(sql,(model,speed,ram,hd,price,screen))
            self.mdb.commit()
            op = int(input("Yana ma'lumot qo'shasizmi?"))

    def ShowInfo_Laptop(self,sql = "SELECT * FROM Laptop;"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"{x[0]} - {x[1]}; {x[2]}; {x[3]}; {x[4]}; {x[5]}; {x[6]}")

# Task - 1
# Modeli Product table modeliga teng bo’lgan PC larni hamma ma’lumotlarini ekranga chiqaruvchi so’rov yozing.

    def Task_1(self,sql = f"SELECT * FROM PC as p INNER JOIN Product as pr ON pr.model = p.model;"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"{x[0]}; {x[1]}; {x[2]}; {x[3]}; {x[4]}; {x[5]}; {x[6]}")        

# Task - 2
# Modeli Product table modeliga teng bo’lgan Laptop larni hamma ma’lumotlarini ekranga chiqaruvchi so’rov yozing.

    def Task_2(self,sql = f"SELECT * FROM Laptop as l INNER JOIN Product as p ON l.model = p.model;"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"{x[0]}; {x[1]}; {x[2]}; {x[3]}; {x[4]}; {x[5]}; {x[6]}")

# Task 3.
# Modeli Product table modeliga teng bo’lgan Printer larni hamma ma’lumotlarini ekranga chiqaruvchi so’rov yozing.

    def Task_3(self,sql = f"""SELECT * FROM Printer as p INNER JOIN Product as pr ON pr.model = p.model 
                              WHERE pr.type = 'Printer' ORDER BY id;"""):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"{x[0]}; {x[1]}; {x[2]}; {x[3]}; {x[4]}; {x[5]}; {x[6]}")

# Task - 4
# Rangli printerlarning maker,model va price ma’lumotlarini ekranga chiqazing;

    def Task_4(self,sql = f"""SELECT pr.maker,p.model,p.price FROM Printer AS p INNER JOIN Product AS pr ON pr.model = p.model
                              WHERE pr.type = 'Printer' AND p.color = 'y';"""):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"Maker : {x[0]}; Model : {x[1]}; Price : {x[2]};")

# Task - 5
# A maker tomonidan ishlab chiqilgan PC larning o’rtacha narxini hisoblang;

    def Task_5(self, sql = f"""SELECT AVG(p.price) FROM PC as p INNER JOIN Product as pr ON pr.model = p.model
                               WHERE pr.maker = 'A' AND pr.type = 'PC';"""):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"Average Price : {int(x[0])}")
            print("")

# Task - 6
# Tezligi(speed) 450 dan kichik bo’lmagan PC ishlab chiqazuvchi makerlarni toping;

    def Task_6(self, sql = f"""SELECT pr.maker FROM PC as p INNER JOIN Product as pr
                             ON pr.model = p.model WHERE p.speed >= 450 AND pr.type = 'PC';"""):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"Maker : {x[0]}")

# Task - 7;
# Har bir PC ishlab chiqaruvchi makerning  eng qimmat mahsulotining maker,price larini ekranga chiqaruvchi so’rov yozing.

    def Task_7(self,sql = f"""SELECT pr.maker,p.price FROM PC as p INNER JOIN Product as pr 
                              ON pr.model = p.model WHERE pr.type = 'PC' ORDER BY p.price DESC LIMIT 1;
                           """):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"Maker : {x[0]}; Price : {x[1]}")

if __name__ == "__main__":
    db = data_base()

    # db.CreateTable_Laptop()
    # db.InputInfo_Laptop()
    # db.ShowInfo_Laptop()

    # db.CreateTable_PC()
    # db.InputInfo_PC()
    # db.ShowInfo_PC()

    # db.CreateTable_Product()
    # db.InputInfo_Product()
    # db.ShowInfo_Product()

    # db.CreateTable_Printer()
    # db.InputInfo_Printer()
    # db.ShowInfo_Printer()

    db.Task_1()
    # db.Task_2()
    # db.Task_3()
    # db.Task_4()
    # db.Task_5()
    # db.Task_6()
    # db.Task_7()
