import os
os.system("clear")

def Kiril(satr: str):
    
    russian_to_english = {
    'а': 'a','б': 'b','с': 'c','д': 'd','е': 'e','ф': 'f','г': 'g','х': 'h','и': 'i','ж': 'j','к': 'k',
    'л': 'l','м': 'm','н': 'n','о': 'o','п': 'p','р': 'r','т': 't','у': 'u','в': 'v','й': 'y','з': 'z',
    'А': 'A','Б': 'B','С': 'C','Д': 'D','Е': 'E','Ф': 'F','Г': 'G','Х': 'H','И': 'I','Ж': 'J','К': 'K',
    'Л': 'L','М': 'M','Н': 'N','О': 'O','П': 'P','Р': 'R','Т': 'T','У': 'U','В': 'V','Й': 'Y','З': 'Z'
    }
    english_to_russian = {
        'a': 'а','b': 'б','c': 'с','d': 'д','e': 'е','f': 'ф','g': 'г',
        'h': 'х','i': 'и','j': 'ж','k': 'к','l': 'л','m': 'м','n': 'н','o': 'о','p': 'п',
        'q': 'к','r': 'р','s': 'с','t': 'т','u': 'у','v': 'в','w': 'w','x': 'х',
        'y': 'й','z': 'з','A': 'А','B': 'Б','C': 'С','D': 'Д','E': 'Е','F': 'Ф','G': 'Г',
        'H': 'Х','I': 'И','J': 'Ж','K': 'К','L': 'Л','M': 'М','N': 'Н','O': 'О',
        'P': 'П','Q': 'К','R': 'Р','S': 'С','T': 'Т','U': 'У','V': 'В','W': 'W','X': 'Х','Y': 'Й','Z': 'З'
    }

    reversed_text = ''

    for char in satr:
        if char in english_to_russian:
            reversed_text += english_to_russian[char]
        elif char in russian_to_english:
            reversed_text += russian_to_english[char]
        else:
            reversed_text += char


    return reversed_text

english_text = input("Satr kiriting: ")
reversed_russian_text = Kiril(english_text)
print(reversed_russian_text)