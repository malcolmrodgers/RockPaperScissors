import numpy as np
import random as rand
from Game import Game
def whoWon(a, b):
    winner = bool
    if a == 'R' and b == 'S':
        winner = True
    elif a == 'R' and b == 'P':
        winner = False
    elif a == 'P' and b == 'R':
        winner = True
    elif a == 'P' and b == 'S':
        winner = False
    elif a == 'S' and b == 'P':
        winner = True
    elif a == 'S' and b == 'R':
        winner = False
    elif a == b:
        return "Tie"

def playGame():
    newGame = Game(0, 0, '', '')

    newGame.myTurn()
    newGame.computerTurn()
    #print(newGame.myChoice, newGame.computerChoice)



playGame()


