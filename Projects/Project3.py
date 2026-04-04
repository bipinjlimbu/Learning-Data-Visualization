import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ipl_csv import df

check = df['match_winner'] == df['toss_winner']
count = df[check]['match_id'].count()
percentage = (count / df['match_id'].nunique()) * 100
print(f"Percentage of matches where the toss winner also won the match: {percentage:.2f}%")