import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Rug Plot
df = sns.load_dataset('tips')
sns.rugplot(df['total_bill'])
plt.show()