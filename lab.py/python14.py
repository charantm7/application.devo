import sys

def divexp(a,b):
    assert a>0, "a should be greater than zero"
    try:
        c=a/b
    except ZeroDivisionError:
        print("b should not be equal to zero")
        sys.exit(0)
    else:
        return c

val1 = float(input("Enter the val1 : "))
val2 = float(input("Enter the val2 : "))
val3  = divexp(val1,val2)
print(f"{val1}/{val2}={val3}")
