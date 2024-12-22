import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = x*2
plt.plot(x,y,color='black')
plt.title('linear chart')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()