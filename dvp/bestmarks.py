mark1 =int(input("Enter the Mark 1: "))
mark2=int(input("Enter your marks 2: "))
mark3 = int(input("Enter your marks 3: "))
average =0

if mark2 > mark1 and mark3 > mark1:
    average =(mark2+mark3)/2
elif mark1 > mark2 and mark3 > mark2:
    average =(mark1+mark3)/2   
elif mark1 > mark3 and mark2> mark3:
    average =(mark1+mark2)/2

print("The average of best two numbers are: ",average)
