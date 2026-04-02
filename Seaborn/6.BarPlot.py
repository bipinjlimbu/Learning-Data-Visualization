import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Bar Plot
df = sns.load_dataset('tips')
sns.barplot(x='sex', y='total_bill' , estimator=np.mean, data=df)
plt.show()