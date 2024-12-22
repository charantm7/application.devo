def fn(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fn(num -1)+fn(num-2)
    
num = int(input("Enter a number: "))
if num > 0:
    print("fn(",num,") = ",fn(num),)
else:
    print("Invalid Input")  