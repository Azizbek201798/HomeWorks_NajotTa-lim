import os
import mysql.connector as myc
os.system("clear")

class data_base:
    def __init__(self,db_name = "Employee"):
        try:
            self.mdb = myc.connect(host = "localhost", user = "root", password = "Najot1995!",database = f"{db_name}")
            self.kur = self.mdb.cursor()
        except: 
            self.mdb = myc.connect(host = "localhost", user = "root", password = "Najot1995!")
            self.kur.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            self.kur = self.mdb.cursor()

    def CreateTable(self,tableName = 'Staff'):
        self.kur.execute(f"""CREATE TABLE IF NOT EXISTS {tableName}
                         (id INT PRIMARY KEY AUTO_INCREMENT,first_name VARCHAR(20), last_name VARCHAR(20), phone_number VARCHAR(20),
                         job_id VARCHAR(20), salary INT);""")
        
    def InputInfo(self):
        op = 1
        while op == 1:
            os.system("clear")
            name =    input("Talaba ismi:        >>> ")
            surname = input("Talaba familiyasi:  >>> ")
            phone =   input("Phone number:       >>> ")
            job_id =  input("Job_id:             >>> ")
            salary =  int(input("Salary:         >>> "))

            sql = """INSERT INTO Staff(first_name,last_name,phone_number,job_id,salary) VALUES(%s,%s,%s,%s,%s);"""
            self.kur.execute(sql,(name,surname,phone,job_id,salary))
            self.mdb.commit()
            op = int(input("Yana ma'lumot qo'shasizmi?"))

    def ShowInfo(self,sql = "SELECT * FROM Staff;"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"{x[0]} - {x[1]}; {x[2]}; {x[3]}; {x[4]}; {x[5]}")

if __name__ == "__main__":
    db = data_base()
    # db.CreateTable()
    # db.InputInfo()
    db.ShowInfo()
    # db.ShowInfo("SELECT * FROM Staff WHERE salary > 5000000")