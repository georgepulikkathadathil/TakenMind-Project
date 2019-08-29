import numpy as np
import pandas as pd
from pandas import DataFrame,Series
import seaborn as sns
import matplotlib.pyplot as plt

df1 = pd.read_csv('employees.csv')
df2 = pd.read_csv('ex_employees.csv')
print df1.dtypes
print df2.head()
sns.scatterplot(x='last_evaluation', y='satisfaction_level', data=df2).get_figure().savefig('8.png')
sns.countplot(df2['salary']).get_figure().savefig('second.png')
sns.countplot(df1['dept']).get_figure().savefig('7.png')
sns.scatterplot(x='average_montly_hours', y='satisfaction_level', data=df2).get_figure().savefig('first.png')
