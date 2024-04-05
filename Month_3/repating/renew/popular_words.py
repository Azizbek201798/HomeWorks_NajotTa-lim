import os
os.system("clear")

text = input("Text kiriting : ")
keys = ['I', 'was', 'three', 'near']

dct = {}
def popular_words(words, keys):
    sozlar = words.split()
    for i in range(len(keys)):
        dct[keys[i]] = sozlar.count(keys[i])

    print(dct)

popular_words(text, keys)