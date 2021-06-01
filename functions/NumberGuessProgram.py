#This is the number guess program
import random
secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20")
for guessesTaken in range(1, 7):
  print("Take a guess")
guess = int(input())
if guess < secretNumber:
  print("Your guess is too low!")
elif guess > secretNumber:
  print("Your guess is too high")
else:
  break
if secretNumber == guess:
  print("Congratulations! You have guessed it right!")
print("You have taken " + str(guessesTaken) + "guesses")
 
else:
  print("the number that I was thinking was " + str(secretNumber))