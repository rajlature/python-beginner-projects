import random

print("Welcome to Rock Paper Scissors!")

player_choice=str(input("Enter your choice (rock/paper/scissors) : ").lower().strip())
while player_choice not in ["rock", "paper", "scissors"]:
  print("Invalid choice. Please enter rock, paper, or scissors.")
  player_choice=str(input("Enter your choice (rock/paper/scissors) : ").lower().strip())

print("\nyou chose: ", player_choice)
computer_choice = random.choice(["rock", "paper", "scissors"])
print("computer choice: ", computer_choice)

if player_choice == computer_choice:
  print("It's a tie! try once more ")
elif player_choice == "rock" and computer_choice == "scissors":
  print("Rock beats Scissors! You win!")
elif player_choice == "paper" and computer_choice == "rock":
  print("Paper beats Rock! You win!")
elif player_choice == "scissors" and computer_choice == "paper":
  print("Scissors beats Paper! You win!")
else:
  print("You lose! like to try again")