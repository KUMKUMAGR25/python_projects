print("===== UNIT CONVERTER =====")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")
print("5. Kilograms to Pounds")
print("6. Pounds to Kilograms")

choice = input("Enter your choice (1-6): ")

value = float(input("Enter value: "))

if choice == "1":
    result = value * 0.621371
    print("Miles:", round(result, 2))

elif choice == "2":
    result = value * 1.60934
    print("Kilometers:", round(result, 2))

elif choice == "3":
    result = (value * 9/5) + 32
    print("Fahrenheit:", round(result, 2))

elif choice == "4":
    result = (value - 32) * 5/9
    print("Celsius:", round(result, 2))

elif choice == "5":
    result = value * 2.20462
    print("Pounds:", round(result, 2))

elif choice == "6":
    result = value * 0.453592
    print("Kilograms:", round(result, 2))

else:
    print("Invalid choice!")