import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio

tips = sns.load_dataset('tips')

pio.renderers.default = 'browser'

# Using Plotly Express to create a scatter plot
fig = px.scatter(tips, x='total_bill', y='tip', color='sex', size='size',hover_data=['day'], title='Total Bill vs Tip')
fig.show()