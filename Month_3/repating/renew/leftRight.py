import os
os.system("clear")

ls = list(map(str,input("Satr kiriting : ").split()))

def right_join(lst: list):
    sozlar = list(map(lambda x: x.replace("left", "right"), lst))
    boshqa_ozgaruvchi = ",".join(sozlar)
    print(f'"{boshqa_ozgaruvchi}"')

right_join(ls)