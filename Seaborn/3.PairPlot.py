import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Pair Plot
df = sns.load_dataset('tips')
sns.pairplot(df, hue='size', palette='rainbow')
plt.show()