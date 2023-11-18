import random
from enum import Enum
import sys

def play_rps():

    class RPC(Enum):
        ROCK=2
        PAPPER=1
        SCISSORS=3

    youWin="You win!"
    pythonWins="Python Wins!"
    tieGame="Tie game"

    playerChoise=input("Enter number \n1 for PAPPER,\n2 for ROCK,\n3 for SCISSORS...\n")
    
    if playerChoise not in ['1','2','3']:
        print("You must enter 1,2 or 3")
        return play_rps()

    player=int(playerChoise)

    python= random.randint(1,3)


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
    
    print("\nPlay again? ")
    while True:
        playagain=input("\nY for Yes or \nQ to Quit\n")
        if playagain.lower() not in ['y','q']:
            continue
        else:
            break            

    if playagain.lower()=="y":
        return play_rps()
    else:
        sys.exit("Bye!")

play_rps()

