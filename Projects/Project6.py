import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ipl_csv import df

# Analyze the top scorers in IPL

count = df.groupby('top_scorer')['highscore'].sum().sort_values(ascending=False).head(10)
sns.barplot(y=count.index, x=count.values, palette='coolwarm')
plt.title('Top 10 Scorers in IPL')
plt.xlabel('Highest Score')
plt.ylabel('Player Name')
plt.show()