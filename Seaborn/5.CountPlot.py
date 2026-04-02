import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Count Plot
df = sns.load_dataset('tips')
sns.countplot(x='sex', hue='smoker', data=df)
plt.show()