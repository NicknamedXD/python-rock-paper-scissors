# Rock, Paper, Scissors Game
# Author: Your Name
# Description: A simple console-based Rock, Paper, Scissors game in Python.

#imports
import random
#decloration of variales
possible_actions = ["rock","paper","scissors"]
#initialization of the variables
humanwins=0
computerwins=0


#winner selection
def game(ac1,ac2):
    if ac1==ac2:
        outcome="tie"
    elif ac1 == "rock":
        if ac2 == "scissors":
            print("Rock smashes scissors! You win!")
            outcome="win"
        else:
            print("Paper covers rock! You lose.")
            outcome="loss"
    elif ac1 == "paper":
        if ac2 == "rock":
            print("Paper covers rock! You win!")
            outcome="win"
        else:
            print("Scissors cuts paper! You lose.")
            outcome="loss"
    elif ac1 == "scissors":
        if ac2 == "paper":
            print("Scissors cuts paper! You win!")
            outcome="win"
        else:
            print("Rock smashes scissors! You lose.")
            outcome="loss"
    return outcome


#main
print("Lets play rock,paper,scissors!!!")

#asks the player how many wins are needed for the main loop to end
while True:
    number=input("Give the number of wins required to finish: ")
    if number.isnumeric():
        number=int(number)
        break
    
#loops until the game is over 
while humanwins!=number and computerwins!=number:
    computer_action = random.choice(possible_actions)
    human_action = input("choose rock ,paper or scissors: ")
    while human_action not in possible_actions:
        human_action = input("choose rock ,paper or scissors: ")
    outcome=game(human_action,computer_action)
    if outcome=="tie":
        print("Tie no one wins")
    elif outcome=="win":
        humanwins+=1
    else:
        computerwins+=1
#end screen
if humanwins==number:
    print("Congradulations you won against the computer :)")
else:
    print("You lost the game against the computer :(")
