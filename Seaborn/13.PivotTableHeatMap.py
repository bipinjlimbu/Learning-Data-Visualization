import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

flights = sns.load_dataset('flights')

pvtflights = flights.pivot_table(index='month', columns='year', values='passengers')
sns.heatmap(pvtflights)
plt.show()