import os
os.system("clear")

os.chdir("/home/azizbek/go/src/NajotTalim/HomeWork/Month_3/function_3/classwork")

f = open("lola.mp3","rb")
f.seek(1000000)
p = open("me.mp3","wb")
p.write(f.read(902400))

# f = open("real.jpg","rb")
# p = open("copy.jpg","wb")
# p.write(f.read())
