"""
Created March 2024
@author: Malcolm Rodgers
"""

import random as rand

#create game class & necessary parameters
class Game:
    def __init__(self, myScore, computerScore, myChoice, computerChoice, winner, tie):
        self.tie = tie
        self.winner = winner
        self.computerScore = computerScore
        self.computerChoice = computerChoice
        self.myChoice = myChoice
        self.myScore = myScore

#Prompt user, record input in myChoice
    def myTurn(self):
        choice = input("Choose Rock, Paper, or Scissors (R/P/S): ")
        self.myChoice = choice

#Record a random choice in computerChoice
    def computerTurn(self):
        options = ['R', 'P', 'S']
        self.computerChoice = rand.choice(options)


