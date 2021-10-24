import os, random
from random import randint


class Game(object):
    def rps_comp():
        # Get random number form 1 to 3
        computer = randint(1,3)
        return computer

    def rps_win(player, computer):
        # Now to check who has won....
        # Paper beats Rock
        # Rock beats Scissors
        # Scissors beats Paper
        win = ""

        if player == computer:
            win = "We have a Tie"
            print("It's a tie")
        elif player == 1 and computer == 3:
            win = "Player Won"
            print('You have won')
        elif player == 1 and computer == 2:
            win = "Computer Won"
            print('You loose')
        elif player == 2 and computer == 1:
            win = "Player Won"
            print('You have won')
        elif player == 2 and computer == 3:
            win = "Computer Won"
            print('You loose')
        elif player == 3 and computer == 1:
            win = "Player Won"
            print('You have won')
        elif player == 3 and computer == 2:
            win = "Computer Won"
            print('You loose')
        return win
