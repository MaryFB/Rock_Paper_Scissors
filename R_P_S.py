import os
import re
import random

os.system('cls' if os.name=='nt' else 'clear')
while (1 < 2):
    print ("\n")
    print ("Rock, Paper, Scissors")
    player_choice = input("Pick R, P, or S: ([R]ock], [P]aper, or [S]cissors): ")
    if not re.match("[SsRrPp]", player_choice):
        print ("Your letter must be R, P, or S")

        continue
    # Echo the user's choice
    print ("You picked: " + player_choice)
    choices = ['R', 'P', 'S']
    machine_choice= random.choice(choices)
    print ("I picked: " + machine_choice)
    if machine_choice== str.upper(player_choice):
        print ("Tie! ")
    #if machine_choice== str("R") and str.upper(player_choice) == "P"
    elif machine_choice== 'R' and player_choice.upper() == 'S':      
        print ("Scissors beats rock, I win! ")
        continue
    elif machine_choice== 'S' and player_choice.upper() == 'P':      
        print ("Scissors beats paper! I win! ")
        continue
    elif machine_choice== 'P' and player_choice.upper() == 'R':      
        print ("Paper beat rock, I win! ")
        continue
    else:       
        print ("You win!")

