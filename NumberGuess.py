"""This program is a guess game between user and computer"""

from random import randint
from time import sleep

def get_user_guess():
  user_guess=int(raw_input("Enter your guess: "))
  return user_guess

def roll_dice(number_of_sides):
  first_roll=randint(1,number_of_sides)
  second_roll=randint(1,number_of_sides)
  max_val=number_of_sides*2
  print "The maximum value of the outcome is " + str(max_val)
  
  sleep(1)
  user_guess=get_user_guess()
  if user_guess > max_val:
    print "Your guess is invalid"
    return exit()
  else:
    print "Rolling..."
    sleep(2)
    print "The first roll is %d" %(first_roll)
    sleep(1)
    print "The second roll is %d" %(second_roll)
    sleep(1)
    total_val=first_roll+second_roll
    print "Total value is %d" %(total_val)
    print "Result..."
    sleep(1)
    if user_guess==total_val:
      print "You won. That's great"
    else:
      print "Computer wins!"
      
roll_dice(6)
    
  
  
  
  