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
import random
choices = [rock,paper,scissors]

computer = random.randint(0,2)
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))

if user < 0 or user > 2:
  print("Choose a number: 0, 1 or 2")
else:
  print(f"{choices[user]}")
  print(f"Computer chose:\n {choices[computer]}")

  if user == computer:
    print("It is a tie.")
  elif user == 0 and computer == 1:
    print("Computer wins.")
  elif user == 0 and computer == 2:
    print("You win.")
  elif user == 1 and computer == 0:
    print("You win.")
  elif user == 1 and computer == 2:
    print("Computer wins.")
  elif user == 2 and computer == 0:
    print("Computer wins.")
  elif user == 2 and computer == 1:
    print("You win.")




