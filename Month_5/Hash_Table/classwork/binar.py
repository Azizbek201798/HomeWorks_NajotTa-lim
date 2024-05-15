import os
import bcrypt
os.system("clear")

def hashlash_bycrypt(parol1):
    pr1 = parol1.encode('utf-8')
    tuz = bcrypt.gensalt()
    print(tuz)
    # result = bcrypt.hashpw(pr1,tuz)
    # return bcrypt.checkpw(pr1,result)

hashlash_bycrypt("Aznsa")
# if __name__ == "__main__":
    # print(hashlash_bycrypt("Salom","Aleykum"))