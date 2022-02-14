# Charlotte Niblett
# January 13th, 2022
# This is the Rock Paper Scissors Game
# I don't know how to code

from random import randint #importing only random function
import random #importing from the whole library
from time import sleep



def decide_winner():
    uscore = 0
    cscore = 0
    
    while uscore < 3 and cscore < 3:
        
        user_choice = input("Choose between R, P, or S ").upper()
        options = ["R", "P", "S"]
        computer_choice = options[randint(0,2)]
        
        print ("Computer selecting...")
        sleep (2)
        print ("Computer chose " + computer_choice)
        sleep (1)
        if user_choice == computer_choice:
            print ("It is a tie!")
        elif user_choice == "P" and computer_choice == "R":
            print ("User wins!")
            uscore = uscore + 1
        elif user_choice == "S" and computer_choice == "P":
            print ("User wins!")
            uscore = uscore + 1
        elif user_choice == "R" and computer_choice == "S":
            print ("User wins!")
            uscore = uscore + 1
        else:
            print ("Computer wins.")
            cscore = cscore + 1
        print ("User Score: " + str(uscore) + " - " + "Computer Score: " + str(cscore))
    
    if uscore == 3:
        print("Game over, you won!")
    if cscore == 3:
        print("Game over, you lost.")
              
              
decide_winner()
