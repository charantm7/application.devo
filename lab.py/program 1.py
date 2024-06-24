print("***Fibonacci Series***")

n = int(input("Enter the number of terms: "))

t1 = 0
t2 = 1

print(t1)
print(t2)

for i in range(n-2):
    next = t1 + t2
    print(next)
    t1 = t2
    t2 = next