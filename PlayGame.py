import numpy as np
import random as rand
from Game import Game
def whoWon(a, b, game):
    if a == 'R' and b == 'S':
        game.winner = True
    elif a == 'R' and b == 'P':
        game.winner = False
    elif a == 'P' and b == 'R':
        game.winner = True
    elif a == 'P' and b == 'S':
        game.winner = False
    elif a == 'S' and b == 'P':
        game.winner = True
    elif a == 'S' and b == 'R':
        game.winner = False
    elif a == b:
        game.tie = True

def keepScore(game):
    if game.winner:
        game.myScore += 1
    elif not game.winner:
        game.computerScore += 1
    elif game.tie == True:
        return

def playGame():
    newGame = Game(0, 0, '', '', bool, bool)

    newGame.myTurn()
    newGame.computerTurn()
    #print(newGame.myChoice, newGame.computerChoice)

playGame()