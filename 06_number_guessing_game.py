import random

system_guess = random.randint(1, 100)
attempts = 0
player_guess = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
while True:
  user_input = input("\nEnter your guess (or type 'exit'): ")
       
  if user_input.lower().strip() == "exit":
    print("game had been stopped")
    break
  try:
    guess = int(user_input)
    attempts += 1  
    if guess == system_guess:
      print(f"Congratulations! You guessed the number {system_guess} correctly in {attempts} attempts.")
      break
    elif guess < system_guess:
      print("Too low! Try again.")
    elif guess > system_guess:
      print("Too high! Try again.")
  except ValueError:
    print("Invalid input. Please enter a valid number.")
  