import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Violin Plot
df = sns.load_dataset('tips')
sns.violinplot(x='day', y='total_bill', data=df)
plt.show()