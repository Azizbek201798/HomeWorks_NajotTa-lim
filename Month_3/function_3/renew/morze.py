import os
os.system("clear")

MORSE = {".-" : "a", "-..." : "b", "-.-." : "c", "-.." : "d",
          "." : "e", "..-." : "f", "--." : "g", "...." : "h",
          ".." : "i", ".---": "j", "-.-" : "k", ".-.." : "l",
          "--" : "m", "-." : "n", "---" : "o", ".--." : "p",
          "--.-" : "q", ".-." : "r", "..." : "s", "-" : "t",
          "..-" : "u", "...-" : "v", ".--" : "w", "-..-" : "x",
          "-.--" : "y", "--.." : "z"}

word = input("So'z kiriting : ").split(" ")
newWord = ""

for x in word:
    if x == "":
        newWord += " "
    elif x in MORSE:
        newWord += MORSE[x]

print(newWord.capitalize())

# .. -  .-- .- ...  .-  --. --- --- -..  -.. .- -.-- -> Itwasagoodday