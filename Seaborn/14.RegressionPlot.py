import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o', 'x'])
plt.show()