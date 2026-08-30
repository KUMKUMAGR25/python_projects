from datetime import date

day = int(input("Enter your birth day: "))
month = int(input("Enter your birth month: "))
year = int(input("Enter your birth year: "))

today = date.today()
birth_date = date(year, month, day)

age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print("Your age is:", age, "years")