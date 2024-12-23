import math

angle = float(input("Enter the angle: "))

radians = math.radians(angle)

sin = math.sin(radians)
cos = math.cos(radians)

print(f"sin of angle: {angle}: {sin}")
print(f"cos of angle: {angle}: {cos}")