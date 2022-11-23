import random

rock = '''
  _______
--'   ____)
      (_____)
      (_____)
      (____)
--.__(___)
'''

paper = '''
    _______
---'   _____)___
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
game_image = [rock, paper , scissors]#index 0,1,2
user_choice = int(input("0 for rock,1 for paper, 2 for scissor"))

if user_choice>=3 or user_choice<0:
    print("you typed invalid number you lose")

else:

    print("user choice:-")
    print(game_image[user_choice])

    comp_choice = random.randint(0,2)
    print("computer chose")
    print(game_image[comp_choice])


    if user_choice == 0 and comp_choice==2:
        print("you win")

    elif comp_choice==0 and user_choice ==2:
        print("you lose")

    elif comp_choice > user_choice:
        print("you lose")

    elif user_choice > comp_choice:
        print("you win")

    elif comp_choice == user_choice:
        print("its a draw")
