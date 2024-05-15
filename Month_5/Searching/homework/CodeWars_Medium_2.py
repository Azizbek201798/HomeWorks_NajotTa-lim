# CodeWars_Medium_2 => DONE by Azizbek

# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples

# pig_it('Pig latin is cool') igPay atinlay siay oolcay
# pig_it('Hello world !')     elloHay orldway !

def pig_it(text : str):
    
    massiv = []

    for i in list(text.split()):
        if i.isalpha():
            massiv.append(i[1:] + i[0] + "ay")
        else :
            massiv.append(i)

    natija = " ".join(massiv)

    return natija

print(pig_it("Pig latin is cool"))