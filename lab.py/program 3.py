# Develop a program to print student name, usn, marks of three subjects, total marks of three subjects, and percentage

name = input("Enter the name of the student: ")
usn = input("Enter the USN of the student: ")
marks_sub1 = int(input("Enter the subject 1 marks: "))
marks_sub2 = int(input("Enter the subject 2 marks: "))
marks_sub3 = int(input("Enter the subject 3 marks: "))

total_marks = marks_sub1 + marks_sub2 + marks_sub3
percentage = total_marks / 3

print("Student details")
print("Student Name:",name)
print("student USN: ",usn)
print("Subject 1 Marks: ",marks_sub1)
print("Subject 2 Marks: ",marks_sub2)
print("Subject 3 Marks: ",marks_sub3)
print("Total Marks: ",total_marks)
print("percentege: ",percentage)