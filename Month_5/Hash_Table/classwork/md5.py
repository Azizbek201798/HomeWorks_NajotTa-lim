from hashlib import sha256,md5

def Hashlash(data:str):
    data = data.encode('utf-8')
    return md5(data).hexdigest()

if __name__ == "__main__":
    satr = input("Satrni kiriting : ")
    print(f"{Hashlash(satr)}")
    print(f"Len : {len(Hashlash(satr))}")
    