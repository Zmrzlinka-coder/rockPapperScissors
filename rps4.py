import random
from enum import Enum
import sys

game_count=0

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

    def decide_winner(player,python):
        if player==1 and python==2:
            return youWin
        elif player==2 and python==3:
            return youWin
        elif player==3 and python==1:
            return youWin
        elif player==python:
            return tieGame
        else:
            return pythonWins
        
    game_result=decide_winner(player,python)
    print(game_result)

    global game_count
    game_count+=1

    print("\nGame count: "+ str(game_count))
    
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

