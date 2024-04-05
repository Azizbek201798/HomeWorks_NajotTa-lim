import os
os.system("clear")

info = "BYD"

match(info) :
    case "GM"         : print("Uzbekistan")
    case "Revault"    : print("German")
    case "Chevrolete" : print("USA")
    case "BYD"        : print("China")
    case "Wolswagen"  : print("German")
    case _            : print("Default")
