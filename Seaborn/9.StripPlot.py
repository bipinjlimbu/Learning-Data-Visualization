import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Strip Plot
df = sns.load_dataset('tips')
sns.stripplot(x='day', y='total_bill', data=df)
plt.show()