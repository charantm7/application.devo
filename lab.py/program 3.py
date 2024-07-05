name = input("Enter the name of the student: ")
usn = input("Enter the usn of the student: ").upper()
sub1 = int(input("Enter the marks in subject 1: "))
sub2 = int(input("Enter the marks in subject 2: "))
sub3 = int(input("Enter the marks in subject 3: "))
total_marks = sub1 + sub2 + sub3
percentage = total_marks / 3

print("\\Student Details\\")
print("Name:", name)
print("USN:", usn)
print("Subject 1 marks:", sub1)
print("subject 2 marks:", sub2)
print("subject 3 marks:", sub3)
print("Total marks:", total_marks)
print("Percentage:", percentage)
