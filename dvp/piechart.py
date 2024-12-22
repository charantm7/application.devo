import matplotlib.pyplot as plt

lable = ['A','B','C','D','E','F','G']
size = [30,12,7,3,36,29,60]
plt.pie(size, labels=lable, autopct='%1.1f%%')
plt.title('Pie chart')
plt.show()