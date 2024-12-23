import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\Charan TM\OneDrive\Desktop\python_test_file.csv")
data.fillna(data.mean(), inplace=True)
sns.pairplot(data, hue="species")
plt.show()
    