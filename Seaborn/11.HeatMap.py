import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

# Heat Map
tipscorr = tips[['tip', 'total_bill', 'size']]
sns.heatmap(tipscorr.corr(), annot=True)
plt.show()