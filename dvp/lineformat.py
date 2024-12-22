import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x,y, linestyle='-', color='black', linewidth=2)
plt.title("Line formating chart")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show() 