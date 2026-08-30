import random

print("🎲 Welcome to Dice Rolling Simulator")

while True:
    choice = input("\nPress Enter to roll the dice or type 'exit' to quit: ")

    if choice.lower() == "exit":
        print("Thanks for playing!")
        break

    dice = random.randint(1, 6)
    print("You rolled:", dice)