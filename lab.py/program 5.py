def factorial(n):
    if n<0:
        return None
    
    elif n== 0:
        return 1
    else:
        result = 1
        for i in range(1,n+1):
            result *= i
        return result
def bionomial_coefficients(n,r):
    return factorial(n) // (factorial(r) * factorial(n-r))

r = int(input("Enter the value of R: "))
n = int(input("Enter the value of N: "))

print("The factorial of", n ,"is", factorial(n))

if bionomial_coefficients is not None:
    print("The binomial coefficent is", bionomial_coefficients(n,r))
else:
    print("Invalid input")
