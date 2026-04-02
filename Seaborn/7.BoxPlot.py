import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Box Plot = to 
df = sns.load_dataset('tips')
sns.boxplot(x='total_bill', y='day', data=df)
plt.show()