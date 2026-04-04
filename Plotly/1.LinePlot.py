import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio

tips = sns.load_dataset('tips')

pio.renderers.default = 'browser'

# Using Plotly Express to create a line plot
fig = px.line(tips, x='total_bill', y='tip', title='Total Bill vs Tip')
fig.show()