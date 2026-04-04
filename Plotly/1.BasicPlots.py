import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio

tips = sns.load_dataset('tips')

pio.renderers.default = 'browser'

# Line Plot
fig = px.line(tips, x='total_bill', y='tip', title='Total Bill vs Tip')
fig.show()

# Scatter Plot
fig = px.scatter(tips, x='total_bill', y='tip', color='sex', size='size',hover_data=['day'], title='Total Bill vs Tip')
fig.show()

# Bar Plot
fig = px.bar(tips, x='day', y='total_bill', color='sex', title='Total Bill by Day and Gender')
fig.show()