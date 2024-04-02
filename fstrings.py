#name=input("Enter the name of the candidate:")
#weight=int(input("enter the weight in kg:"))
#height=float(input("Enter the height in meters:"))
#bmi=weight/height**2
#print(f"I am {name} and my BMI is {bmi}")
age=int(input("Enter your age:"))

years_left=90-age
days_left=years_left*365
months_left=years_left*12
weeks_left=years_left*52
print(f"you have a {days_left} days, {weeks_left} weeks,and {months_left} months")