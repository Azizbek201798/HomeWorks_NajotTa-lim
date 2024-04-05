import random,os
os.system("clear")

liga1 = ["Paxtakor","Nasaf","Surxon","Bunyodkor"]
liga2 = ["Barselona","Real Madrid","Bavariya","Arsenal"]

def qura(liga1 : list,liga2 : list):
    juftliklar = []
    for x in range(len(liga1)):
        a = random.choice(liga1)
        b = random.choice(liga2)
        juftliklar.append(a + " : " + b)
        liga1.remove(a)
        liga2.remove(b)
    return juftliklar

result = qura(liga1,liga2)
for x in result:
    print(x)

