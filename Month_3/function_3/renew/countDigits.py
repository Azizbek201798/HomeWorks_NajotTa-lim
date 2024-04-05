import os
os.system("clear")

def countDigits(satr : str):
    count = 0
    for x in satr:
        if x.isdigit():
            count += 1

    print(f"Output : {count}")


word = input("So'z kiritng : ")

countDigits(word)