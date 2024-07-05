import math
def mean(num):
    return sum(num)/len(num)

def variance(num):
    m = mean(num)
    return sum((x-m)**2 for x in num)/len(num)
def std_dev(variance):
    return math.sqrt(variance)

n = int(input("Enter the number of elements: "))
num = []
for i in range(n):
    a = float(input(f"Enter the element {i+1}: "))
    num.append(a)

Mean = mean(num)
Variance = variance(num)
Std_dev = std_dev(Variance)
print(f"Mean: {Mean}")
print(f"Variance: {Variance}")
print(f"Standard deviation: {Std_dev}")