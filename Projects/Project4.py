import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ipl_csv import df

# Analyze the winning margin trends in IPL

sns.countplot(x='won_by', data=df, palette='Set1')
plt.title('Winning Margin Trends in IPL')
plt.xlabel('Winning Margin Type')
plt.ylabel('Count')
plt.show()