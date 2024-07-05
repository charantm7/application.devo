import sys

def DivExp(a,b):
    assert a>0, "a should be greater than zero"

    try:
        c=a/b
    except ZeroDivisionError:
        print("b must be not equal to zero")
        sys.exit(0)
    else:
        return c
    
val1 = int(input("Enter the value of a: "))
val2 = int(input("Enter the value of b: "))
val3 = DivExp(val1,val2)
print(f"{val1}/{val2}={val3}")