"""
Created March 2024
@author: Malcolm Rodgers
"""

from Game import Game


# Given game object, determine the winner and store the result
def whoWon(game):
    a = game.myChoice
    b = game.computerChoice

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


# Once game.winner is set (or .tie), update the score parameters
def keepScore(game):
    if game.tie:
        return
    elif (not game.tie) and game.winner:
        game.myScore += 1
    elif (not game.tie) and not game.winner:
        game.computerScore += 1


# Create a new game object
newGame = Game(0, 0, '', '', False, False)


# playGame runs each helper function, storing the results in the new game object
def playGame(myGame):
    myGame.myTurn()
    myGame.computerTurn()
    print('The computer chose: ' + myGame.computerChoice)

    whoWon(myGame, myGame.myChoice, myGame.computerChoice)
    keepScore(myGame)

    if myGame.tie:
        print("Its a tie!")
    else:
        if myGame.winner:
            print("You won!")
        elif not myGame.winner:
            print("You lose")

    print('Your score ' + str(myGame.myScore) + ' Computer score ' + str(myGame.computerScore))

    # Prompt the user to play again, if Y then reset parameters
    playAgain = input('Would you like to play again? (Y/n) ')
    if playAgain == 'Y':
        myGame.winner = False
        myGame.tie = False
        playGame(myGame)
    elif playAgain == 'n':
        print('Final score: You - ' + str(myGame.myScore)
              + ' Computer - ' + str(myGame.computerScore)
              + '\nThanks for playing!')
        return

# Call playGame
playGame(newGame)
