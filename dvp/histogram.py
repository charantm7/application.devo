import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(100,10,1000)
plt.hist(data, bins=20, edgecolor='black')
plt.title('Histogram plot')
plt.xlabel('value')
plt.ylabel('frequency')
plt.grid(True)
plt.show()