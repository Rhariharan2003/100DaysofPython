#day04ofpython

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

def  game():
  user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
  
  computer_input = random.randint(0,2)
  
  if(user_input == 0) :
   print("user choosed : \n"+ rock)
  elif (user_input == 1):
   print("user choosed : \n"+ paper)
  else :
    print("user choosed : \n"+ scissors)
  
  if(computer_input == 0) :
   print(f"computer choosed : {computer_input}\n"+ rock)
  elif (computer_input == 1):
   print(f"computer choosed : {computer_input}\n"+ paper)
  else :
    print(f"computer choosed :{computer_input}\n"+ scissors)
  
  if(computer_input == 0 and  user_input == 2) :
   print("You lose")
  elif computer_input == 2 and user_input == 0 :
   print("You wins!")
  elif(computer_input == 0 and  user_input == 1) :
   print("You wins!")
  elif computer_input == 1 and user_input == 0 :
   print("You lose")
  elif(computer_input == 1 and  user_input == 2) :
   print("You wins!")
  elif computer_input == 2 and user_input == 1 :
   print("You lose")
  else:
    print("Draws")

heart = True
while heart:
  game()
  interest = input("Do You Want a New Game? 'y' or 'n'")
  if(interest == 'n'):
    print("Exited...")
    heart = False
  
