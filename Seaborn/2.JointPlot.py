import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Joint Plot
df = sns.load_dataset('tips')
sns.jointplot(x='total_bill', y='tip', data=df, kind='scatter')
sns.jointplot(x='total_bill', y='tip', data=df, kind='hex')
sns.jointplot(x='total_bill', y='tip', data=df, kind='reg')
sns.jointplot(x='total_bill', y='tip', data=df, kind='kde')
plt.show()