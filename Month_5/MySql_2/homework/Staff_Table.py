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
            name =        input("Ismi:              >>> ")
            surname =     input("Familiyasi:        >>> ")
            phone =       input("Phone number:      >>> ")
            job_id =      input("Job_id:            >>> ")
            salary =  int(input("Salary:            >>> "))

            sql = """INSERT INTO Staff(first_name,last_name,phone_number,job_id,salary) VALUES(%s,%s,%s,%s,%s);"""
            self.kur.execute(sql,(name,surname,phone,job_id,salary))
            self.mdb.commit()
            op = int(input("Yana ma'lumot qo'shasizmi?"))

    def ShowInfo(self,sql = "SELECT * FROM Staff;"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"{x[0]} - {x[1]}; {x[2]}; {x[3]}; {x[4]}; {x[5]}")

# Task 1.
# Staff jadvalidan  first_name va last_name larini ism, familiya   ko’rinishida chiqaradigan so’rov yozing.

    def Task_1(self,sql = "SELECT first_name,last_name FROM Staff;"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"Ismi : {x[0]}; Familiyasi: {x[1]};")

# Task 2.
# Staff jadvalida job_id si IT_PROG bo’lgan ishchilarning  first_name, last_name  va salary larini ism, familiya 
# va maosh ko’rinishida chiqaradigan so’rov yozing.

    def Task_2(self,sql = "SELECT first_name,last_name,salary FROM Staff WHERE job_id = 'IT_PROG';"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"Ismi: {x[0]}; Familiyasi: {x[1]}; Salary: {x[2]};")

# Task 3.
# Staff jadvalida salary lari 5000 dan katta va 20000 dan kichik bo’lgan ishchilarning job_id va salary larini 
# ekranga chiqaruvchi so’rov yozing.

    def Task_3(self,sql = "SELECT job_id,salary FROM Staff WHERE salary > 5000 and salary < 20000;"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"Job_id: {x[0]}; Salary : {x[1]};")

# Task 4.
# Staff jadvalida job_id lari IT_PROG va FI_ACCOUNT bo’lgan ishchilarning salarylarini o’sish tartibida chiqaruvchi so’rov yozing.

    def Task_4(self,sql = "SELECT * FROM Staff WHERE job_id = 'IT_PROG' OR job_id = 'FI_ACCOUNT' ORDER BY salary;"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"{x[0]} - {x[1]}; {x[2]}; {x[3]}; {x[4]}; {x[5]}")

# Task 5.
# Staff jadvalida telefon raqami oxirgi 4 ta raqami ‘8110’ bo’lgan ishcilarni hamma ma’lumotlarini ekranga chiqaruvchi so’rov yozing.

    def Task_5(self, sql = "SELECT * FROM Staff WHERE phone_number LIKE '%8110';"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"{x[0]} - {x[1]}; {x[2]}; {x[3]}; {x[4]}; {x[5]}")

# Task 6.
# Staff jadvalida hamma ishchilarga bir oyda umumiy qancha maosh to’lanishini aniqlovchi so’rov yozing.

    def Task_6(self,sql = "SELECT SUM(salary) AS total_salary FROM Staff;"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"Total salary : {x[0]}")

# Task 7
# Staff jadvalidan eng katta maosh to’lanadigan job_id si IT_PROG bo’lgan ischining hamma ma’lumotlarini chiqaruvchi so’rov yozing.

    def Task_7(self,sql = "SELECT * FROM Staff WHERE job_id = 'IT_PROG' ORDER BY salary DESC LIMIT 1;"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"{x[0]} - {x[1]}; {x[2]}; {x[3]}; {x[4]}; {x[5]}\n\n")

# Task 8
# Staff jadvalidan ishchilarning o’rtacha maoshidan katta maosh oladigan ishchilarning hamma ma’lumotlarini chiqaruvchi so’rov yozing.

    def Task_8(self,sql = "SELECT * FROM Staff WHERE salary > (SELECT AVG(salary) FROM Staff);"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"{x[0]} - {x[1]}; {x[2]}; {x[3]}; {x[4]}; {x[5]}")

# Task 9.
# Staff jadvalidan maoshi job_id si ‘IT_PROG ‘ bo’lgan ishchilarning o’rtacha maoshidan katta bo’lgan ishchilarning hamma ma’lumotlarini 
# ekranga chiqaring.

    def Task_9(self,sql = "SELECT * FROM Staff WHERE salary > (SELECT AVG(salary) FROM Staff WHERE job_id = 'IT_PROG');"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"{x[0]} - {x[1]}; {x[2]}; {x[3]}; {x[4]}; {x[5]}")

if __name__ == "__main__":
    db = data_base()
    # db.CreateTable()
    # db.InputInfo()
    # db.ShowInfo()

    # db.Task_1()
    # db.Task_2()
    # db.Task_3()
    # db.Task_4()
    # db.Task_5()
    # db.Task_6()
    # db.Task_7()
    # db.Task_8()
    db.Task_9()