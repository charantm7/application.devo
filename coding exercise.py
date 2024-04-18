print("SGPA CALCULATOR")
name = input("name: ")
tot_sub = int(input("Total Subjects: "))
tot_credits = 0
sum1 = 0

for i in range(1, tot_sub + 1):
    credits_points = int(input(f"{i} subject credit point: "))
    marks = int(input(f"{i} subject marks: "))
    grade_points = (marks // 10) + 1
    sum = credits_points * grade_points
    sum1 += sum
    print(f"Grade Points: {grade_points}")

# Calculate total credits
tot_credits = sum(credits_points for _ in range(tot_sub))

# Calculate SGPA
sgpa = sum1 / tot_credits
print("SGPA:", sgpa)
