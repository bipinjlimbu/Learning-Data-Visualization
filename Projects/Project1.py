import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ipl_csv import df

# Analyze the most winning teams in IPL

most = df['match_winner'].value_counts()
sns.barplot(y=most.index, x=most.values, palette='viridis')
plt.title('Most Winning Teams in IPL')
plt.show()