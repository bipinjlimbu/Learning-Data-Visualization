import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ipl_csv import df

# Analyze the most used venues in IPL

count = df['venue'].value_counts()
sns.barplot(y=count.index, x=count.values, palette='coolwarm')
plt.title('Most Used Venues in IPL')
plt.xlabel('Number of Matches')
plt.ylabel('Venue')
plt.show()