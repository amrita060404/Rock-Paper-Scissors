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
import random
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice != (0 or 1 or 2):
    print("You picked an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)
    print(f"Computer chose: \n     {game_images[computer_choice]}")

    if user_choice - computer_choice == -2:
        print("You win!")
    if user_choice - computer_choice == 2:
        print("You lose!")
    elif user_choice != (0 or 1 or 2):
        print("You picked an invalid number!")
    elif user_choice > computer_choice:
        print("You win!")
    elif user_choice < computer_choice:
        print("You lose!")
    elif user_choice == computer_choice:
        print("It's a draw!")
