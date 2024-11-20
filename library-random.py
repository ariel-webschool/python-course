import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
papper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


choices = [rock,papper,scissor]

user = int(input("What do you choose? Type 0 for Rock, 1 for Papper, 2 for scissors. "))
computer = random.randint(0,2)

print(f"Computer {choices[computer]}")
print(f"User {choices[user]}")
if user == computer:
	print("Draw")
elif user == 0 and computer == 1 or user == 1 and computer == 2 or user == 2 and computer == 0 :
	print("You lose!")
else:
	print("You win!")
