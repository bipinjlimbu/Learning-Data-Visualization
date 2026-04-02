import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
y = x**2

plt.plot(x,y)
plt.title('Plot Title')
plt.xlabel('X Side')
plt.ylabel('Y Side')

plt.savefig('Plot.png')