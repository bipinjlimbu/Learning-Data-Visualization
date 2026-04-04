import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ipl_csv import df

# Analyze the match winner with the highest margin by Runs

check = df['won_by'] == 'Runs'
count = df['margin'] == df[check]['margin'].max()
print(f"Match winner with the highest margin by Runs: {df['match_winner'][count].values[0]}")