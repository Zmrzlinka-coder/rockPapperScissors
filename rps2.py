import random
from enum import Enum
import sys

class RPC(Enum):
    ROCK=2
    PAPPER=1
    SCISSORS=3

playagain=True

youWin="You win!"
pythonWins="Python Wins!"
tieGame="Tie game"

while playagain:

    playerChoise=input("Enter number \n1 for PAPPER,\n2 for ROCK,\n3 for SCISSORS...\n")
    player=int(playerChoise)

    python= random.randint(1,3)

    if player<1 or player>3:
        sys.exit("You must enter 1,2 or 3")

    print("You choose: "+ str(RPC(player)).replace('RPC.','') + ", Python choose: "+ str(RPC(python)).replace('RPC.',''))

    if player==1 and python==2:
        print(youWin)
    elif player==2 and python==3:
        print(youWin)
    elif player==3 and python==1:
        print(youWin)
    elif player==python:
        print(tieGame)
    else:
        print(pythonWins)
    
    playagain=input("\nPlay again? \nY for Yes or \nQ to Quit\n")

    if playagain.lower()=="y":
        continue
    else:
        break

