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

#Write your code below this line 👇

ascii = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player <= 2 and player >= 0:
    print(ascii[player])
    opponent = random.randint(0, 2)
    print("Computer chose:")
    print(ascii[opponent])
    if player >= 3 or player < 0: 
        print("Not a valid number. You lose!") 
    elif player == 0 and opponent == 2:
        print("You win!")
    elif opponent == 0 and player == 2:
        print("You lose")
    elif opponent > player:
        print("You lose")
    elif player > opponent:
        print("You win!")
    elif opponent == player:
        print("It's a draw")
else:
    print("Not a valid number. You lose!")

