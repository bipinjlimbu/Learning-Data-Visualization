import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio

tips = sns.load_dataset('tips')

pio.renderers.default = 'browser'

# Histogram
fig = px.histogram(tips, x='total_bill', nbins=20, title='Distribution of Total Bill')
fig.show()