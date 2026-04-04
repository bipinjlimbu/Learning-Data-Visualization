import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ipl_csv import df

# Analyze the top 10 players with the most Player of the Match awards in IPL

count = df['player_of_the_match'].value_counts().head(10)
sns.barplot(y=count.index, x=count.values, palette='magma')
plt.title('Top 10 Players with Most Player of the Match Awards in IPL')
plt.xlabel('Number of Awards')
plt.ylabel('Player Name')
plt.show()