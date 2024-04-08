import random
name=input("Enter everybody's name separated by commas:")
a=name.split(',')
b=random.choice(a)
print(f"{b} will pay the bill")