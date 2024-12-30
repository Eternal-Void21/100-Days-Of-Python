# Rock, Paper, and Scissor Game
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

user_input = int(input("What do you choose? Type 0 for rock, 1 for Paper, or 2 for Scissors.\n"))
list_possibilities = [rock, paper, scissors]
name_possibilities = ["Rock", "Paper", "Scissors"]

#User Side
if user_input in (0, 1, 2):
    print("Your choice: " + name_possibilities[user_input])
    print(list_possibilities[user_input])
else:
    print("Wrong Number.")

#Computer Side
computer = random.randint(0,2)
print("Computer's choice: " + name_possibilities[computer])
print(list_possibilities[computer])

#Rules
# 0 for Rock, 1 for Paper, 2 for Scissors
if user_input == computer:
    print("Draw.")
else:
    if user_input == 0 and computer == 1:
        print("Computer Wins!")
    elif user_input == 0 and computer == 2:
        print("You Win!")
    elif user_input == 1 and computer == 0:
        print("You Win!")
    elif user_input == 1 and computer == 2:
        print("Computer Wins!")
    elif user_input == 2 and computer == 0:
        print("Computer Wins!")
    elif user_input == 2 and computer == 1:
        print("You Win!")



