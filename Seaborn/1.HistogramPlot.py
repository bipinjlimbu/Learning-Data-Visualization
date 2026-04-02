import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Histogram Plot
df = sns.load_dataset('tips')
sns.displot(df['total_bill'], kde=False, bins=10)
plt.show()