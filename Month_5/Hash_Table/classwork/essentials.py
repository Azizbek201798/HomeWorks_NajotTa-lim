import os
os.system("clear")

def hash_function(data : str):
    return hash(data)

if __name__ == "__main__":

    s = input("Satr kiriting: ")
    print(f"Kiritilgan satr   : {s}")
    print(f"Hashlangan qiymat : {hash_function(s)}")
