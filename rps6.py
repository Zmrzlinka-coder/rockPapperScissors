import random
from enum import Enum
import sys

def rps():
    game_count=0
    player_wins=0
    python_wins=0
    
    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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


        print(f"\nYou choose: {str(RPC(player)).replace('RPC.','')} , Python choose: {str(RPC(python)).replace('RPC.','')}\n")

        def decide_winner(player,python):
            nonlocal player_wins
            nonlocal python_wins
            if player==1 and python==2:
                player_wins+=1
                return youWin
            elif player==2 and python==3:
                player_wins+=1
                return youWin
            elif player==3 and python==1:
                player_wins+=1
                return youWin
            elif player==python:
                return tieGame
            else:
                python_wins+=1
                return pythonWins
            
        game_result=decide_winner(player,python)
        print(game_result)

        nonlocal game_count
        game_count+=1

        print(f"\nGame count: { str(game_count)}")
        print(f"\nPlayer wins: : { str(player_wins)}")
        print(f"\nPython wins: : { str(python_wins)}")
        
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

    return play_rps

play=rps()
play()

