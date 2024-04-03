import math 
def calculate_mean(numbers):
    return sum(numbers)/len(numbers) 
def calculate_variance(numbers):
    mean=calculate_mean(numbers)
    return sum((x-mean)**2 for x in numbers)/len(numbers)
def calculate_standard_deviation(variance):
    return math.sqrt(variance)
n=int(input("enter the number of elements:"))
numbers=0
for i in range(n):
    num=float(input(f"Enter the elements{i+1}:"))
numbers.append(num)
mean=calculate_mean(numbers)
variance=calculate_variance(numbers)
std_dev=calculate_standard_deviation(variance)
print(f"Mean:{mean}")
print(f"Variance:{variance}")
print(f"Standard Deviation:{std_dev}")