#day12ofpython

#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
print("""                           ,,         
     __                   o-°°|\_____/)
(___()'`; Guess the Number \_/|_)     )
/,    /`                      \  __  / 
\\"--\\                       (_/ (_/ """)
print("")
print("")
print("Welcome to the Number Guessing Game!")
print("I'm thicking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts = 0
if difficulty == "easy":
  attempts = 10
else:
  attempts = 5
number = random.randint(1,101)

def num(attempts,number):
 print(f"You have {attempts} attempts remaining to guess the number.")
 if attempts == 0:
   print("You've run out of Guessess, you lose.")
   print("GAME OVER!  ")
   return 
 guess = int(input("Make a Guess: "))
 if guess > number:
  print("Too High.")
  print("Guess again.")
  attempts = attempts - 1
  num(attempts,number)
 elif guess < number:
  print("Too Low.")
  print("Guess again.")
  attempts = attempts - 1
  num(attempts,number)
 else :
  print(f"You got it! the answer was {number}")
  return 
num(attempts,number)
