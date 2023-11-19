rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


scissor=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

import random
choice=[rock,paper,scissor]
user_choice=int(input("enter 0 for rock,1 for paper and 2 for scissor\n"))
if user_choice>=3 or user_choice<0:
    print("invalid input,you lose!")
else:
    print(choice[user_choice])

    comp_choice=random.randint(0,2)
    print(choice[comp_choice])
    if user_choice==0 and comp_choice==2:
        print("you win!")
    elif  comp_choice==0 and user_choice==2:
        print("you lose!")
    elif user_choice==comp_choice:
        print("its a draw!")
    elif user_choice>comp_choice:
        print("you win!")
    elif comp_choice>user_choice:
        print("you lose!")
