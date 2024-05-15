import os 
os.system("cls")
import mysql.connector as myc


class data_base:
    def __init__(self,db_name = "Employee"):
        try:
            self.mdb = myc.connect(host = 'localhost',user = 'root', password = 'ali7808', database = f"{db_name}")

        except:
            self.mdb = myc.connect(host = 'localhost',user = 'root', password = 'ali7808')
            self.kur = self.mdb.cursor()
            self.kur.execute("Create  database if not exists {}".format(db_name))
        
        finally:
            self.kur = self.mdb.cursor()

    def create_table(self,tb_name = 'Staff'):
        self.kur.execute(f""" CREATE TABLE IF NOT EXISTS {tb_name}
                    (id int primary key auto_increment, first_name varchar(30),
                    last_name varchar(30), phone_number varchar(30), job_id varchar(20),salary int);""")
        
    def input_info(self):
        op = 1
        while op ==1:
            os.system("cls")
            name =      input("name:      >>>")
            surname =   input("surname:   >>>")
            ph_num =    input("ph_num:    >>>")
            jb_id =     input("job_id:    >>>")
            salary =int(input("salary:    >>>"))
            sql = """ INSERT INTO Staff(first_name, last_name, phone_number, job_id,salary) 
                      VALUES(%s,%s,%s,%s,%s)"""
            values = (name,surname,ph_num,jb_id,salary)
            self.kur.execute(sql,values)
            self.mdb.commit()
            op = int(input("yana info qo'shasizmi (1: YES 2: NO) >>>"))

    def show_info(self,sql = "select * from Staff"):
        self.kur.execute(sql)
        for x in self.kur.fetchall():
            print(f"{x[0]}.\t{x[1]}.\t{x[2]}.\t{x[3]}.\t{x[4]}.\t{x[5]}")

if __name__ == "__main__":
    db = data_base()
    db.create_table()
    db.input_info()
    dc = {"task1" : "select avg(price) from dori"}
    for x in dc:
        print(f"\tyechim {x}")
        db.show_info(dc[x])
    db.show_info(f"select * from Staff where salary >{int(input('maoshni kiriting:'))}" )