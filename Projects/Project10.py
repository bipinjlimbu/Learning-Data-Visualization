import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ipl_csv import df

# Player with the highest score in the IPL

high = df['highscore'] == df['highscore'].max()
scorer = df['top_scorer'][high].values[0]
print(f"Highest scorer in the IPL: {scorer}")