import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ipl_csv import df

# Analyze the top bowlers with the most wickets in IPL

df['highest_wicket'] = df['best_bowling_figure'].apply(lambda x: x[0]).astype(int)
count = df.groupby('best_bowling')['highest_wicket'].sum().sort_values(ascending=False).head(10)
sns.barplot(y=count.index, x=count.values, palette='plasma')
plt.title('Top 10 Bowlers with Most Wickets in IPL')
plt.xlabel('Total Wickets')
plt.ylabel('Bowler Name')
plt.show()