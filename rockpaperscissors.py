import random

print("lets play a game!\
 rock, paper, scissors!")

status = True
while True:
    options = ['rock', 'paper', 'scissors']

    computer = random.choice(options)
    player= None

    while player not in options:
        player = input('rock, paper, or scissors? choice: ').lower()

        if player == computer:
            print(f"computer picked: {computer}")
            print(f"player picked: {player}")
            print("Draw!")

        elif player == "rock":
            if computer == "paper":
                print(f"computer picked: {computer}")
                print(f"player picked: {player}")
                print("Loser!!")
            if computer == "scissors":
                print(f"computer picked: {computer}")
                print(f"player picked: {player}")
                print("You win!")

        elif player == "paper":
            if computer == "scissors":
                print(f"computer picked: {computer}")
                print(f"player picked: {player}")
                print("Loser!!")
            if computer == "rock":
                print(f"computer picked: {computer}")
                print(f"player picked: {player}")
                print("You win!")

        elif player == "scissors":
            if computer == "rock":
                print(f"computer picked: {computer}")
                print(f"player picked: {player}")
                print("Loser!!")
            if computer == "paper":
                print(f"computer picked: {computer}")
                print(f"player picked: {player}")
                print("You win!")

    again = input("Wanna play again?: [y/n] ").lower()
#instead of if again == y use if not equal is much more efficient!
    if again != "y":
      break
print("bye loser!")
