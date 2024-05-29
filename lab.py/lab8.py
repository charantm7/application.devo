import sys

def DivExp(a,b):
    assert a>0, "a should be greater than 0"

    try:
        c=a/b

    except ZeroDivisionError:
        print("B must not be zero")

    else:
        return c
    
val1 = int(input("Enter the value of a: "))
val2 = int(input("Enter the value of b: "))
val3 = DivExp(val1,val2)

print(f"{val1}/{val2}={val3}")