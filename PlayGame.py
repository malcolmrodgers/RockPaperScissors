import numpy as np
import random as rand
from Game import Game


def playGame():
    newGame = Game(0, 0, '', '')

    newGame.myTurn()
    newGame.computerTurn()
    #print(newGame.myChoice, newGame.computerChoice)



playGame()


