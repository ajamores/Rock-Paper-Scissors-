import random
flag = True

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

while flag:
    print("\nWelcome! Let's play Rock, Paper, Scissors!")
    user = int(input("Press 1 for Rock, 2 for Paper, 3 for Scissors: "))



    if user == 1:
        print(rock)
        print("You chose Rock!")
    elif user == 2:
        print(paper)
        print("You chose Paper!")
    elif user == 3:
        print(scissors)
        print("You chose Scissors!")
    else:
        print("Please input a valid response!")
        print(user)

    cpu = random.randint(1, 3)

    if cpu == 1:
        print(rock)
        print("The Computer chose Rock!")
    elif cpu == 2:
        print(paper)
        print("The Computer chose Paper!")
    elif cpu == 3:
        print(scissors)
        print("The Computer chose Scissors!")

    #winning with Rock
    if user == 1 and cpu == 1:
        print("\nIt's a Draw!")
    elif user == 1 and cpu == 2:
        print("\nYou lose! Loser! Haha!")
    elif user ==  1 and cpu == 3:
        print("\nYou Win!")

    #winning with Paper

    if user == 2 and cpu == 1:
        print("\nYou Win!")
    elif user == 2 and cpu == 2:
        print("\nIt's a Draw!")
    elif user ==  2 and cpu == 3:
        print("\nYou Lose!")

    #winning with Scissors
    if user == 3 and cpu == 1:
        print("\nYou lose! Loser! Haha!")
    elif user == 3 and cpu == 2:
        print("\nYou Win!")
    elif user ==  3 and cpu == 3:
        print("\nIt's a Draw!")

    again = input("Would you like to play again? (y/n): ").lower()

    if again == "n":
        print("Thanks for playing!")
        flag = False
    elif again != "y":
        print("Please input a valid response!")
        again = input("Would you like to play again? (y/n): ").lower()
