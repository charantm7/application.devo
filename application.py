a=input("Enter the student name: ")
b=int(input("Enter the student marks subject 1: "))
c=int(input("Enter the student marks subject 2: "))
d=int(input("Enter the student marks subject 3: "))
e=int(input("Enter the student marks subject 4: "))
total_marks=b+c+d+e
percentage=(total_marks*100/400)
print("Name:",a)
print("Total marks:",total_marks)
print("Percentage:",percentage)
if percentage>=90 and percentage<=100:
 print("Grade:A")
elif percentage>=80 and percentage<=90:
 print("Grade:B")
elif percentage>=70 and percentage<=80:
 print("Grade:C")
else:
 print("Grade:Fail")