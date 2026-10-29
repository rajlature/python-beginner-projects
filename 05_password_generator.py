import random
import string

print("Welcome to the Password Generator!")
user_choice = 0;
while user_choice <=0:
  try:
    user_choice = int(input("\nHow many characters should your password contain? "))
    # letter = string.ascii_letters
    # digits = string.digits
    # symbols = string.punctuation
    characters = (string.ascii_letters + 
                  string.digits + 
                  string.punctuation)
  except ValueError:
    print("INVALID INPUT PLEASE USE NUMBER")

password = ""
for i in range(user_choice):
  password += random.choice(characters)
print(password)