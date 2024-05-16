def translate(lotin_text):
    lotin_kril = {
        'A': 'А', 'a': 'а', 'B': 'Б', 'b': 'б', 'D': 'Д', 'd': 'д', 'E': 'Е', 'e': 'е',
        'F': 'Ф', 'f': 'ф', 'G': 'Г', 'g': 'г', 'H': 'Ҳ', 'h': 'ҳ', 'I': 'И', 'i': 'и',
        'J': 'Ж', 'j': 'ж', 'K': 'К', 'k': 'к', 'L': 'Л', 'l': 'л', 'M': 'М', 'm': 'м',
        'N': 'Н', 'n': 'н', 'O': 'О', 'o': 'о', 'P': 'П', 'p': 'п', 'Q': 'Қ', 'q': 'қ',
        'R': 'Р', 'r': 'р', 'S': 'С', 's': 'с', 'T': 'Т', 't': 'т', 'U': 'У', 'u': 'у',
        'V': 'В', 'v': 'в', 'X': 'Х', 'x': 'х', 'Y': 'Й', 'y': 'й', 'Z': 'З', 'z': 'з',
        'Ch': 'Ч', 'ch': 'ч', 'Sh': 'Ш', 'sh': 'ш', 'Ya': 'Я', 'ya': 'я', 'Yo': 'Ё', 'yo': 'ё',
        'Yu': 'Ю', 'yu': 'ю', 'Ts': 'Ц', 'ts': 'ц', 'O‘': 'Ў', 'o‘': 'ў', 'G‘': 'Ғ', 'g‘': 'ғ'
    }

    kril_text = ""
    skip = 0
    for i in range(len(lotin_text)):
        if skip:
            skip -= 1
            continue

        if i + 1 < len(lotin_text):
            two_char = lotin_text[i:i + 2]
            if two_char in lotin_kril:
                
                kril_text += lotin_kril[two_char]
                skip = 1
                continue

        kril_text += lotin_kril.get(lotin_text[i], lotin_text[i])

    return kril_text

lotin_input = input("Lotincha matn kiriting: ")
print(translate(lotin_input))