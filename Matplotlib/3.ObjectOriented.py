import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,8), dpi=200)
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.2,0.4,0.4])

x = np.linspace(0,5,11)
y = x**2

axes1.plot(x,y)
axes1.set_title('Larger Plot')
axes1.set_xlabel('X Side')
axes1.set_ylabel('Y Side')

axes2.plot(y,x)
axes2.set_title('Smaller Plot')
axes2.set_xlabel('Y Side')
axes2.set_ylabel('X Side')

plt.show()