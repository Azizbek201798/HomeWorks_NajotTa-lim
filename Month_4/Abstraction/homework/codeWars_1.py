import os
os.system("clear")

# Degree 7

def rpsls(pl1, pl2):
    if (pl1 == "lizard" and pl2 == "spock") or (pl1 == "lizard" and pl2 == "paper") or (pl1 == "scissors" and pl2 == "lizard") or (pl1 == "scissors" and pl2 == "paper") or (pl1 == "paper" and pl2 == "rock") or (pl1 == "rock" and pl2 == "lizard") or (pl1 == "lizard" and pl2 == "spock") or (pl1 == "spock" and pl2 == "scissors") or (pl1 == "scissors" and pl2 == "lizard") or (pl1 == "paper" and pl2 == "spock") or(pl1 == "spock" and pl2 == "rock") or (pl1 == "rock" and pl2 == "scissors"):
        return "Player 1 Won!"
    elif pl1 == pl2:
        return "Draw!"
    else :
        return "Player 2 Won!"
    