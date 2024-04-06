import math
def calculate_mean(numbers):
    return sum(numbers)/len(numbers)
def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    return sum((x-mean)**2 for x in numbers)/len(numbers)
def calculate_standard_deviation(variance):
    return math.sqrt(variance)
n=int(input("Enter the number if elements:"))
numbers=0
for i in range(n):
 num= float(input(f"Enter number {i+1}:"))
numbers.append(num)
mean=calculate_mean(numbers)
variance=calculate_variance(numbers)
std_dev=calculate_standard_deviation(variance)
print(f"Mean:{mean}")
print(f"variance:{variance}")
print(f"Standard deviation:{std_dev}")