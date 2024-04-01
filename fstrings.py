name=input("Enter the name of the candidate:")
weight=int(input("enter the weight in kg:"))
height=int(input("Enter the height in meters:"))
bmi=weight/height**2
print("I am ",name,"and my BMI is",round(bmi,2))