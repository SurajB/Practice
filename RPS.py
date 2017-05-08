"""This is rock paper and scissors game"""

from random import *
from time import sleep

options = ["R", "P", "S"]
lost= "You lost!"
win = "You won. That's cool"

def decide_winner(user_choice, computer_choice):
  print "The user choice is " + user_choice
  print "The computer is selecting..."
  sleep(1)
  print "The computer's choice is " + options[computer_choice]
  user_choice_index = options.index(user_choice)
  computer_choice_index = computer_choice
  
  if user_choice_index == computer_choice_index:
    print "It's a tie"
  elif (user_choice_index == 0 and computer_choice_index == 2) or (user_choice_index == 1 and computer_choice_index == 0) or (user_choice_index == 2 and computer_choice_index == 1):
    print win
  elif user_choice_index > 2:
    print "Enter a valid option"
  else:
    print lost
    
def play_RPS():
  print "This is rock paper scissors game"
  user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors: ").upper()
  computer_choice = randint(0, len(options)-1)
  decide_winner (user_choice, computer_choice)
                                    
play_RPS()
                                    
                                   
  
    
    
  
  
  
  

