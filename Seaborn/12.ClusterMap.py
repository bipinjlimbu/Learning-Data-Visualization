import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

# Cluster Map
tipscorr = tips[['tip', 'total_bill', 'size']]
sns.clustermap(tipscorr.corr(), annot=True)
plt.show()