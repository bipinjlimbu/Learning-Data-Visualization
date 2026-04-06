import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ipl_csv import df

# Best bowling figure in the IPL

df['wickets'] = df['best_bowling_figure'].apply(lambda x: int(x.split('--')[0]))
df['runs_conceded'] = df['best_bowling_figure'].apply(lambda x: int(x.split('--')[1]))
high = df['wickets'] == df['wickets'].max()
best = df[high]['runs_conceded'] == df[high]['runs_conceded'].min()
print(f"Best bowling figure in the IPL: {df[high][best]['best_bowling'].values[0]}")