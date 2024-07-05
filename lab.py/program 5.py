def factorial(n):
    if n<0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1,n+1):
            result *= i
        return result
    
def bionomial_coeffiecient(n,r):
    return factorial(n)//(factorial(r)*factorial(n-r))

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

print(f"The factorial of {n} is {factorial(n)}")

if bionomial_coeffiecient is not None:
    print(f"The bionmial coefficent is {bionomial_coeffiecient(n,r)}")
else:
    print("Invalid input")