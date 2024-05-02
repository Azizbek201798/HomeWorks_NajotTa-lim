import os
import mysql.connector as myc
os.system("clear")


def CreateBase(databasename):
    try:
        mdb = myc.connect(user = 'root',host = 'localhost',password = 'Najot1995!',)
        
        if mdb.is_connected():
            kur = mdb.cursor()
            kur.execute(f"CREATE DATABASE IF NOT EXISTS {databasename}")
            print(f"{databasename} nomli database yaratildi!")
    except:
        print("Baza bilan ishlashda xatolik!")
        print(mdb)

def CreateTable(tablename):
    mdb = myc.connect(user = 'root',host = 'localhost',password = 'Najot1995!',database = 'students')

    kur = mdb.cursor()
    kur.execute(f"""CREATE TABLE IF NOT EXISTS {tablename}
                (id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(30),age INT, gender VARCHAR(10), GDP float);""")

def InputInfo():
    op = 1
    while op == 1:
        os.system("")
        name = input("Name >>> ")
        age = int(input("Age >>> "))
        gender = input("Gender >>> ")
        GDP = float(input("GDP >>> "))

        sql = 'INSERT INTO talaba(name,age,gender,GDP) VALUES (%s,%s,%s,%s);'

        mdb = myc.connect(user = 'root',host = 'localhost',password = 'Najot1995!',database = 'students')
        kur = mdb.cursor()
        kur.execute(sql,(name,age,gender,GDP))
        op = int(input("Yana ma'lumot qo'shasizmi? 1.Yes 2.No"))
        mdb.commit()

def ShowInfo():
    mdb = myc.connect(user = 'root',host = 'localhost',password = 'Najot1995!',database = 'students')
    kur = mdb.cursor()
    kur.execute("SELECT * FROM talaba ORDER BY age DESC;")
    result = kur.fetchall()
    for x in result:
        print(x)
    # Tuple qaytaradi;

# CreateBase('students')
# CreateTable('talaba')
# InputInfo()
ShowInfo()