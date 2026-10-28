print("Welcome to the Treasure Island")
print("\nYour mission is to find the treasure.")
print("You're at a cross road. Where do you want to go? Type 'left' or 'right'")
choice = input().lower()
if choice == "left":
  print("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
  choice = input().lower()
  if choice == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        choice = input().lower()
        if choice == "red":
            print("It's a room full of fire. Game Over.")
        elif choice == "yellow" or choice == "blue":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
  else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")