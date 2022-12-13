import random
from art import logo

def game(difficulty_of_the_game):
  if difficulty_of_the_game == "hard":
    number_of_lives = 5
  else:
    number_of_lives = 10

  number_to_guess = random.randint(1, 100)

  while number_of_lives != 0:
    make_a_guess = int(input("Make a guess: "))
    if number_to_guess == make_a_guess:
      print(f"You got it! The anwer was {make_a_guess}")
      break
    elif(number_to_guess > make_a_guess):
      number_of_lives -= 1
      print("Too low")
      try_again(number_of_lives)
    else:
      number_of_lives -= 1
      print("Too high.")
      try_again(number_of_lives)
      
def try_again(number_of_lives):
  print("Guess again.")
  if number_of_lives != 0:
    print(f"You have {number_of_lives} attempts remaining to guess the number.")
  else:
    print("You've run out of guesses,  you lose.")

def guess_the_number_game():
  print(logo)
  print(f"Welcome to the Number Guessing Game!")
  print(f"I'm thinking of a number between 1 and 100.")
  difficulty_of_the_game = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  while difficulty_of_the_game != "hard" and difficulty_of_the_game != "easy":
    print("Please type again the difficulty")
    difficulty_of_the_game = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  game(difficulty_of_the_game)

guess_the_number_game()