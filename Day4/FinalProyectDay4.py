import random
from wsgiref.validate import InputWrapper

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
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

list = [rock, paper, scissors]
computer_choose = random.randint(0,2)

if choose < 0 or choose > 2:
    print("You typed an invalid number, you lose!")
else:
    print(list[choose])
    print("Computer chose:")
    print(list[computer_choose])

    if choose == computer_choose:
        print("Tie")
    elif choose == 0:
        if computer_choose == 2:
            print("You win")
        else:
            print("You lose")
    elif choose == 1:
        if computer_choose == 0:
            print("You win")
        else:
            print("You lose")

    else:
        if computer_choose == 1:
            print("You win")
        else:
            print("You lose")