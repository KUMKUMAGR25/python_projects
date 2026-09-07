balance = 10000

while True:
    print("\n===== ATM SIMULATOR =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is: ₹", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Money deposited successfully!")
            print("New balance: ₹", balance)
        else:
            print("Invalid amount!")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount!")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print("Please collect your money.")
            print("Remaining balance: ₹", balance)

    elif choice == "4":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice!")