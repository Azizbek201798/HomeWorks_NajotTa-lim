# Topshiriq_4 => DONE by LeoMessi

# Stringga bir nechta so'z va gaplar berilgan. Ushbu stringdagi ma'lumotlarni so'zlarni va gaplarni alohida listlarga 
# joylashtiradigan funksiya tuzing.
# Input: Salom Yoz. Olam juda ham go'zal. Imtihon bo'lyapti.
# Output:
# words: [Salom, Yoz, Olam, juda, ham, go'zal, Imtihon, bo'lyapti]
# sentence: [Salom Yoz, Olam juda ham go'zal, Imtihon bo'lyapti]

import os
os.system("clear")

text = "Salom Yoz. Olam juda ham go'zal. Imtihon bo'layapti"

word = text.replace(".","")
words = word.split(" ")

sentence = text.split(".")

print(f"Words     : {words}")
print(f"Sentence  : {sentence}")

