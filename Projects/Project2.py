import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ipl_csv import df

# Analyze the toss trend in IPL

sns.countplot(x='toss_decision', data=df, palette='Set2')
plt.title('Toss Decision Trends in IPL')
plt.xlabel('Toss Decision')
plt.ylabel('Count')
plt.show()