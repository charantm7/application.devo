import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


department_salaries = {
    'Sales': [50000, 60000, 55000, 70000, 45000],
    'Marketing': [65000, 75000, 60000, 80000, 55000],
    'Engineering': [80000, 90000, 75000, 100000, 85000],
}

data = []
for dept, salaries in department_salaries.items():
    for salary in salaries:
        data.append({'Department':dept, 'Salaries':salary})

df = pd.DataFrame(data)

sns.boxplot(x='Department',y='Salaries', data=df)
plt.title('Salary Distribution by Department')
plt.ylabel('Salaries')
plt.xlabel('Department')
plt.show()