# CodeWars_Medium_1 => DONE BY Azizbek;

# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters 
# after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are 
# numbers or special characters included in the string, they should be returned as they are. Only 
# letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.

def newLetter(letter : str) -> str:
    if str(letter).isdigit():
        return letter
    
    if 65 <= ord(letter) and ord(letter) <= 90:
        new_letter = ord(letter) + 13
        return chr(new_letter) if new_letter <= 90 else chr(64 + new_letter % 90)

    elif 97 <= ord(letter) and ord(letter) <= 122:
        new_letter = ord(letter) + 13
        return chr(new_letter) if new_letter <= 122 else chr(96 + new_letter % 122)

    return letter

def rot13(message : str) -> str:
    natija = []
    for letter in message:
        natija.append(newLetter(letter))

    return ''.join(natija)
