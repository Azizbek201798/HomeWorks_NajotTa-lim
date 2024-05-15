from hashlib import sha256

def Hashlash(data:str):
    data = data.encode('utf-8')
    return sha256(data).hexdigest()

if __name__ == "__main__":
    satr = input("Satrni kiriting : ")
    print(f"{Hashlash(satr)}")
    print(f"Len : {len(Hashlash(satr))}")
    print(type(Hashlash(satr)))