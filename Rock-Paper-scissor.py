import random

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock Paper Scissors!")
print("Choose: rock, paper, or scissors")

user_choice = input("Enter your choice: ").lower()

computer_choice = random.choice(choices)

print("Computer chose:", computer_choice)

if user_choice not in choices:
    print("Invalid choice!")

elif user_choice == computer_choice:
    print("It's a tie!")

elif (
    (user_choice == "rock" and computer_choice == "scissors")
    or (user_choice == "paper" and computer_choice == "rock")
    or (user_choice == "scissors" and computer_choice == "paper")
):
    print("You win!")

else:
    print("Computer wins!")