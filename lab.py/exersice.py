#number=int(input("Enter the numer:"))
#if number % 2 == 0:
#    print("The number is even number")
#else :
#    print("The number is odd number")
weight=int(input("Enter the weight in kg:"))
height=float(input("enter the height in meters:"))
bmi=weight/height**2
print("BMI:",round(bmi,2))
if bmi<16.0:
    print("Underweight(Severe thinness)")
elif bmi>=16.0 and bmi<=16.9:
    print("Underweight(Moderate thiness)")
elif bmi>=17.0 and bmi<=18.4:
    print("Underweight(Mild thinness)")
elif bmi>=18.5 and bmi<=24.9:
    print("Normal Range")
elif bmi>=25.0 and bmi<=29.9:
    print("Overweight(Pre-obese)")
elif bmi>=30.0 and bmi<=34.9:
    print("Obese(Class 1)")
elif bmi>=35.0 and bmi<=39.9:
    print("Obese(class 2)")
elif bmi>=40.0:
    print("Obese(class 3)")
else :
    print("Invalid")