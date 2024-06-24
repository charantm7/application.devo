#Develop a program to give output as, a person is a senior citizen or not

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
current_year = 2024

age = birth_year - current_year

senior_citizen = age > 60

if senior_citizen:
    print(f"{name}, is senior citizen")

else:
    print(f"{name}, is not a senior citizen")