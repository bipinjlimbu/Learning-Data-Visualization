import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Swarm Plot = Strip Plot but with non-overlapping points
df = sns.load_dataset('tips')
sns.swarmplot(x='day', y='total_bill', data=df)
plt.show()