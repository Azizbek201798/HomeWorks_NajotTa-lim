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
            self.kur.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
            self.kur = self.mdb.cursor()

    def CreateTable_Laptop(self,tableName = 'Laptop'):
        self.kur.execute(f"""CREATE TABLE IF NOT EXISTS {tableName}
                         (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,model varchar (50) NOT NULL ,speed smallint NOT NULL ,
                         ram smallint NOT NULL ,hd real NOT NULL ,price decimal(12,2) NULL ,screen smallint NOT NULL,
                         foreign key model references Product(model);""")
        
    def InputInfo_Laptop(self):
        op = 1
        while op == 1:
            os.system("clear")
            model =       input("Model:  >>> ")
            speed =       input("Speed:  >>> ")
            ram =         input("Ram:    >>> ")
            hd =          input("Hd:     >>> ")
            price =   int(input("Price:  >>> "))
            screen =  int(input("Screen: >>> "))

            sql = """INSERT INTO Laptop(first_name,last_name,phone_number,job_id,salary) VALUES(%s,%s,%s,%s,%s,%s);"""
            self.kur.execute(sql,(model,speed,ram,hd,price,screen))
            self.mdb.commit()
            op = int(input("Yana ma'lumot qo'shasizmi?"))

    def ShowInfo_Laptop(self,sql = "SELECT * FROM Staff;"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"{x[0]} - {x[1]}; {x[2]}; {x[3]}; {x[4]}; {x[5]}; {x[6]}")

if __name__ == "__main__":
    db = data_base()
    db.CreateTable_Laptop()
    db.InputInfo_Laptop()
    db.ShowInfo_Laptop()

    # db.Task_1()
    # db.Task_2()
    # db.Task_3()
    # db.Task_4()
    # db.Task_5()
    # db.Task_6()
    # db.Task_7()
    # db.Task_8()
    # db.Task_9()